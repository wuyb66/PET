/**
 * Created by Yunbo on 2017/11/24.
 */
$(document).ready(function() {

    $.fn.setConfigureForCallType = function() {
        if ($("#id_configureForCallType").is(':checked')) {
            $('#calltypecounterconfiguration-group').show();
        } else {
            $('#calltypecounterconfiguration-group').hide();
        }
        // $('#id_averageActiveSessionPerSubscriber').parent().parent().parent().parent().parent().parent().hide();
    };

    $(this).setConfigureForCallType();

    $('#id_configureForCallType').change(function() {
        $(this).setConfigureForCallType();
    });

    $('#id_configureForCallType').load(function() {
        $(this).setConfigureForCallType();
    });

});

