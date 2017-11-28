from django.db import models
from django.contrib.auth.models import User
from Service.models import Release, CallType, FeatureName, DBInformation
from Hardware.models import CPUTuning, MemoryUsageTuning, HardwareModel, VMType, HardwareType, CPU, CPUList, MemoryList
from Common.models import DBMode
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import Group
from django.conf import settings
from django.core.exceptions import ValidationError

# from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField, ChainedManyToManyField2


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

SERVER_STATUS = (
    (0, u"Normal"),
    (1, u"Down"),
    (2, u"No Connect"),
    (3, u"Error"),
)
SERVICE_TYPES = (
    ('moniter', u"Moniter"),
    ('lvs', u"LVS"),
    ('db', u"Database"),
    ('analysis', u"Analysis"),
    ('admin', u"Admin"),
    ('storge', u"Storge"),
    ('web', u"WEB"),
    ('email', u"Email"),
    ('mix', u"Mix"),
)


# class Province(models.Model):
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name

# class City(models.Model):
#     name = models.CharField(max_length=40)
#     province = models.ForeignKey(Province)

#     def __str__(self):
#         return self.name

# class SelectP(models.Model):
#     province = models.ForeignKey(Province)
#     city = ChainedForeignKey(
#         'City',
#         chained_field="province",
#         chained_model_field="province",
#         show_all=False,
#         auto_choose=True,
#         help_text='Location aaa',
#     )
    # city = models.ForeignKey(City)

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name


class City1(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State)

    def __str__(self):
        return self.name


class Address(models.Model):
    country = models.ForeignKey(Country)
    state = models.ForeignKey(State)
    city = models.ForeignKey(City1)
    street = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)

    def __str__(self):
        return self.street

@python_2_unicode_compatible
class IDC(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    contact = models.CharField(max_length=32)
    telphone = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    customer_id = models.CharField(max_length=128)
    groups = models.ManyToManyField(Group)  # many

    create_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"IDC"
        verbose_name_plural = verbose_name

@python_2_unicode_compatible
class Host(models.Model):
    idc = models.ForeignKey(IDC)
    name = models.CharField(max_length=64)
    nagios_name = models.CharField(u"Nagios Host ID", max_length=64, blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    internal_ip = models.GenericIPAddressField(blank=True, null=True)
    user = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    ssh_port = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField(choices=SERVER_STATUS)

    brand = models.CharField(max_length=64, choices=[(i, i) for i in (u"DELL", u"HP", u"Other")])
    model = models.CharField(max_length=64)
    cpu = models.CharField(max_length=64)
    core_num = models.SmallIntegerField(choices=[(i * 2, "%s Cores" % (i * 2)) for i in range(1, 15)])
    hard_disk = models.IntegerField()
    memory = models.IntegerField()

    system = models.CharField(u"System OS", max_length=32, choices=[(i, i) for i in (u"CentOS", u"FreeBSD", u"Ubuntu")])
    system_version = models.CharField(max_length=32)
    system_arch = models.CharField(max_length=32, choices=[(i, i) for i in (u"x86_64", u"i386")])

    create_time = models.DateField()
    guarantee_date = models.DateField()
    service_type = models.CharField(max_length=32, choices=SERVICE_TYPES)
    description = models.TextField()

    administrator = models.ForeignKey(AUTH_USER_MODEL, verbose_name="Admin")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Host"
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class MaintainLog(models.Model):
    host = models.ForeignKey(Host)
    maintain_type = models.CharField(max_length=32)
    hard_type = models.CharField(max_length=16)
    time = models.DateTimeField()
    operator = models.CharField(max_length=16)
    note = models.TextField()

    def __str__(self):
        return '%s maintain-log [%s] %s %s' % (self.host.name, self.time.strftime('%Y-%m-%d %H:%M:%S'),
                                               self.maintain_type, self.hard_type)

    class Meta:
        verbose_name = u"Maintain Log"
        verbose_name_plural = verbose_name

class Customer(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=120, verbose_name='Name', unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='User')
    release = models.ForeignKey(Release, on_delete=models.CASCADE, verbose_name='Release')

    hardwareModel = models.ForeignKey(HardwareModel, on_delete=models.CASCADE, verbose_name='Hardware Model')

    customer = models.ForeignKey(Customer, verbose_name='Customer')
    version = models.IntegerField(default=1, verbose_name='Version')
    createTime = models.TimeField(auto_now=True, verbose_name='Create Time')

    comment = models.TextField(default='', verbose_name='Comment', blank=True)

    database_type = models.ForeignKey(DBMode, verbose_name='Database Type')

    def __str__(self):
        # return u'%(hardwareType)s %(hardwareModel)s' % {
        #     'hardwareType': self.hardwareType,
        #     'hardwareModel': self.hardwareModel,
        # }
        return self.name

    @property
    def hardwareType(self):
        return self.hardwareModel.hardwareType

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Project'

class WorkingProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.name

class ProjectInformation(models.Model):
    NDB_DEPLOY_OPTION = (('individual', 'Individual'), ('combo', 'Combo'))

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    vmType = models.ForeignKey(VMType, on_delete=models.CASCADE, verbose_name='VM Type')
    cpuNumber = models.ForeignKey(CPUList, verbose_name='CPU Number',)

    memory = models.ForeignKey(MemoryList, verbose_name='Memory')
    clientNumber = models.IntegerField(verbose_name='Client Number')

    sigtranLinkSpeed = models.IntegerField(verbose_name='SIGTRAN Link Speed')
    sigtranLinkNumber = models.IntegerField(verbose_name='SIGTRAN Link Number')
    sigtranPortUtil = models.FloatField(verbose_name='SIGTRAN Port Utility')

    amaRecordPerBillingBlock = models.FloatField(default=1, verbose_name='AMA Record Number per Billing Block')
    numberReleaseToEstimate = models.IntegerField(default=0, verbose_name='Number of Release to Estimate')
    cpuImpactPerRelease = models.FloatField(default=0.05, verbose_name='CPU Impact per Release')
    memoryImpactPerRelease = models.FloatField(default=0.1, verbose_name='Memory Impact per Release')
    dbImpactPerRelease = models.FloatField(default=0.1, verbose_name='DB Impact per Release')
    deploy_option=models.CharField(max_length=16, choices=NDB_DEPLOY_OPTION, default='combo',
                                   verbose_name='NDB Deploy Option')

    averageAMARecordPerCall = models.FloatField(verbose_name='Average AMA Record per Call')
    amaStoreDay = models.FloatField(verbose_name='AMA Store Days')

    activeSubscriber = models.IntegerField(verbose_name='Active Subscriber')
    inactiveSubscriber = models.IntegerField(verbose_name='Inactive Subscriber')
    groupAccountNumber = models.IntegerField(verbose_name='Number of Group Account')

    cpuUsageTuning = models.ForeignKey(CPUTuning, on_delete=models.CASCADE, verbose_name='CPU Usage Tuning')
    memoryUsageTuning = models.ForeignKey(MemoryUsageTuning, on_delete=models.CASCADE,
                                          verbose_name='Memory Usage Tuning')


    def __str__(self):
        return self.project.name

    name = property(__str__)

    class Meta:
        verbose_name = 'Project General Information'
        verbose_name_plural = 'Project General Information'


class TrafficInformation(models.Model):
    DIAMETER_SESSION_TYPE = (('Volume', 'Volume Based Charging'), ('Time', 'Time Based Charging'))

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    callType = models.ForeignKey(CallType, on_delete=models.CASCADE, verbose_name='Call Type')

    activeSubscriber = models.IntegerField(verbose_name='Active Subscriber') # Need to set default=project.activeSubscriber
    inactiveSubscriber = models.IntegerField(verbose_name='Inctive Subscriber') # Need to set default=project.inactiveSubscriber

    trafficBHTA = models.FloatField(verbose_name='BHCA/BHTA', default=0)
    trafficTPS = models.FloatField(verbose_name='CPS/TPS', default=0)
    callHoldingTime = models.IntegerField(verbose_name='Call Holding Time', default=0)

    # Parameter for diameter session call
    averageActiveSessionPerSubscriber = models.FloatField(default=0)
    averageCategoryPerCCR = models.FloatField(default=1)
    averageCategoryPerSession = models.FloatField(default=1)
    volumeCCRiBHTA = models.FloatField(default=0)
    volumeCCRuBHTA = models.FloatField(default=0)
    volumeCCRtBHTA = models.FloatField(default=0)
    timeCCRiBHTA = models.FloatField(default=0)
    timeCCRuBHTA = models.FloatField(default=0)
    timeCCRtBHTA = models.FloatField(default=0)

    def validate_unique(self, exclude=None):
        if (not self.id) and WorkingProject.objects.all().count() > 0:
            qs = TrafficInformation.objects.filter(project=WorkingProject.objects.all()[0].project)
            if qs.filter(callType=self.callType).exists():
                raise ValidationError('Call Type: %s existed!'%self.callType)


    def save(self, *args, **kwargs):
        self.validate_unique()
        super(TrafficInformation, self).save(*args, **kwargs)

    def getTPS(self):
        return self.activeSubscriber * self.trafficBHTA / 3600

    def getBHTA(self):
        return self.trafficBHTA * 3600 / self.activeSubscriber if self.activeSubscriber > 0 else 0

    def getDefaultActiveSubscriber(self):
        return self.project.activeSubscriber

    def getDefaultInactiveSubscriber(self):
        return self.project.inactiveSubscriber

    def __str__(self):
        return self.project.name + '_' + self.callType.name

    name = property(__str__)

    class Meta:
        db_table = 'Traffic Information'
        unique_together = ("project", "callType")

class FeatureConfiguration(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    feature = models.ForeignKey(FeatureName, on_delete=models.CASCADE, verbose_name='Feature Name')
    featurePenetration = models.FloatField(default=0, verbose_name='Feature Penetration (%)')

    # For online hierarchy feature
    colocateMemberGroup = models.BooleanField(default=True)
    rtdbSolution = models.BooleanField(default=True)
    groupNumber = models.FloatField(default=1)
    ratioOfLevel1 = models.FloatField(default=1)

    def validate_unique(self, exclude=None):
        if (not self.id) and WorkingProject.objects.all().count() > 0:
            qs = FeatureConfiguration.objects.filter(project=WorkingProject.objects.all()[0].project)
            if qs.filter(feature=self.feature).exists():
                raise ValidationError('Feature Name: %s existed!'%self.feature)


    def save(self, *args, **kwargs):
        self.validate_unique()
        super(FeatureConfiguration, self).save(*args, **kwargs)

    def __str__(self):
        return self.project.name + "_" + self.feature.name

    name = property(__str__)

    class Meta:
        unique_together = (("project", "feature"),)

class DBConfiguration(models.Model):
    MEMBER_GROUP_OPTION = (('Member', 'Member'), ('Group', 'Group'))
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    dbInfo = models.ForeignKey(DBInformation, on_delete=models.CASCADE, verbose_name='DB Name')

    dbFactor = models.FloatField(default=0, verbose_name='DB Factor')
    placeholderRatio = models.FloatField(default=0, verbose_name='Placeholder Ratio (%)')
    memberGroupOption = models.CharField(max_length=10, choices=MEMBER_GROUP_OPTION,
                                         default='member', verbose_name='DB Option')
    @property
    def recordSize(self):
        return self.dbInfo.recordSize
    @property
    def subscriberNumber(self):
        if WorkingProject.objects.all().count() > 0:
            return ProjectInformation.objects.all().filter(
                project=WorkingProject.objects.all()[0])[0].activeSubscriber
        else:
            return 0
    @property
    def recordNumber(self):
        return self.subscriberNumber * self.dbFactor
    @property
    def cacheSize(self):
        dbOverhead = 1
        if self.dbInfo.name == 'RTDB':
            dbOverhead = self.dbInfo.rtdbOverhead
        return self.recordSize * self.recordNumber * dbOverhead
    @property
    def todoLogSize(self):
        return 0
    @property
    def mateLogSize(self):
        return 0
    @property
    def referencePlaceholderRatio(self):
        return 0


    def __str__(self):
        return self.project.name + "_" + self.dbInfo.db.name

    name = property(__str__)

    def getReferenceDBFactor(self):
        pass

    def getCacheSize(self):
        pass

    def getTodoLogSize(self):
        pass

    def getMateLogSize(self):
        pass

    def getRecordNumber(self):
        pass

    def getSubscriberNumber(self):
        pass

'''
    Define counter configuration for the project.
    Need to calculate the db impact for CTRTDB.
'''
class CounterConfiguration(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    averageBundleNumberPerSubscriber = models.FloatField(
        default=0,
        verbose_name='Number of Bundle',
    )
    average24hBundleNumberPerSubscriber = models.FloatField(
        default=0,
        verbose_name='Number of 24h Bundle',
    )
    nonAppliedBucketNumber = models.FloatField(
        default=0,
        verbose_name='Non Applied Bucket Number',
    )
    nonAppliedUBDNumber = models.FloatField(
        default=0,
        verbose_name='Non Applied UBD Number',
    )
    appliedBucketNumber = models.FloatField(
        default=0,
        verbose_name='Applied Bucket Number',
    )
    appliedUBDNumber = models.FloatField(
        default=0,
        verbose_name='Applied UBD Number',
    )
    groupBundleNumber = models.FloatField(
        default=0,
        verbose_name='Number of Group Bundle',
    )
    groupBucketNumber = models.FloatField(
        default=0,
        verbose_name='Group Bucket Number',
    )

    generateMultipleAMAForCounter = models.BooleanField(
        default=False,
        verbose_name='Generate Multiple AMA For Counter',
    )
    turnOnBasicCriteriaCheck = models.BooleanField(
        default=False,
        verbose_name='Enable Basic Criteria Check',
    )
    configureForCallType = models.BooleanField(
        default=False,
        verbose_name='Configure Counter For Call Types',
    )

    @property
    def totalBundleNumber(self):
        return self.averageBundleNumberPerSubscriber + self.average24hBundleNumberPerSubscriber

    @property
    def totalCounterNumber(self):
        return self.nonAppliedBucketNumber + self.nonAppliedUBDNumber + \
            self.appliedBucketNumber + self.appliedUBDNumber

    def __str__(self):
        return self.project.name

    name = property(__str__)

    class Meta:
        verbose_name = 'Counter Configuration'
        verbose_name_plural = 'Counter Configuration'

    def getTotalCounter(self):
        return self.nonAppliedBucketNumber + self.nonAppliedUBDNumber + self.appliedBucketNumber + self.appliedUBDNumber


class CallTypeCounterConfiguration(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    callType = models.ForeignKey(CallType, on_delete=models.CASCADE)

    averageBundleNumberPerSubscriber = models.FloatField(
        default=0,
        verbose_name='Number of Bundle',
    )
    average24hBundleNumberPerSubscriber = models.FloatField(
        default=0,
        verbose_name='Number of 24h Bundle',
    )
    nonAppliedBucketNumber = models.FloatField(
        default=0,
        verbose_name='Non Applied Bucket Number',
    )
    nonAppliedUBDNumber = models.FloatField(
        default=0,
        verbose_name='Non Applied UBD Number',
    )
    appliedBucketNumber = models.FloatField(
        default=0,
        verbose_name='Applied Bucket Number',
    )
    appliedUBDNumber = models.FloatField(
        default=0,
        verbose_name='Applied UBD Number',
    )

    @property
    def totalBundleNumber(self):
        return self.averageBundleNumberPerSubscriber + self.average24hBundleNumberPerSubscriber

    @property
    def totalCounterNumber(self):
        return self.nonAppliedBucketNumber + self.nonAppliedUBDNumber + \
               self.appliedBucketNumber + self.appliedUBDNumber

    class Meta:
        verbose_name = 'Counter Configuration For Call Type'
        verbose_name_plural = 'Counter Configuration For Call Type'

    def __str__(self):
        return super.__str__() + '_' + self.callType.name

    name = property(__str__)

    def getCounterCPUImpact(self):
        pass

    def getMultipleAMANumber(self):
        pass

    def getMultipleAMAImpact(self):
        pass

    def getTotalCPUImpact(self):
        pass
        #return getCounterCPUImpact() + getMultipleAMANumber() + getMultipleAMAImpact()

    class Meta:
        verbose_name = 'Counter Configuration for Call Type'
        verbose_name_plural = 'Counter Configuration for Call Type'
class SystemConfiguration(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    cabinetNumberPerSystem = models.IntegerField(
        default=1,
        verbose_name='Number of Cabinet Per System',
    )
    backupAppNodeNumberPerSystem = models.IntegerField(
        default=0,
        verbose_name='Number of Backup App Node Per System',
    )
    spareAppNodeNumberPerSystem = models.IntegerField(
        default=0,
        verbose_name='Number of Spare App Node Per System',
    )
    backupDBNodeNumberPerSystem = models.IntegerField(
        default=0,
        verbose_name='Number of Backup DB Node Per System',
    )
    spareDBNodePairNumberPerSystem = models.IntegerField(
        default=0,
        verbose_name='Number of Spare DB Node Pair Per System'
    )

    def __str__(self):
        return self.project.__str__()

    name = property(__str__)

