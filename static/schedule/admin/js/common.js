$(function () {
    function loadNotifications() {

        if (typeof toastr === 'undefined')
            return;

        toastr.options = {
            "closeButton": true
        };

        $('.toast-item').each(function (index, item) {
            var $item = $(item);
            var type = $item.data('type') || 'success';
            var title = type === 'success' ? 'Éxito' : 'Error';
            var message = $item.data('message');
            toastr[type](message, title);
        })
    }

    function initDatetimePickers() {
        if (!jQuery().datetimepicker) {
            return;
        }

        function getDate() {
            var d = new Date()
                .toLocaleString().split(',')[0]
                .split('/').reverse();
            var date = [d[0], d[2], d[1]].join('-');
            return date;
        }

        $(".fecha").datetimepicker({
            useCurrent: false,
            locale: 'es',
            format: "Y-MM-DD"
        });

        $(".fecha_inicio").datetimepicker({
            //  language: 'es',
            //  todayBtn: true,
            //  autoclose: true,
            //  showMeridian: true,
            // // startDate: getDate(),
            //  format: "yyyy-mm-dd hh:ii:ss"
            useCurrent: false, //Important! See issue #1075
            minDate: moment(),
            locale: 'es'
        });

        $(".fecha_limit").datetimepicker({
            //  language: 'es',
            //  todayBtn: true,
            //  autoclose: true,
            //  showMeridian: true,
            // // startDate: getDate(),
            //  format: "yyyy-mm-dd hh:ii:ss"
            useCurrent: false, //Important! See issue #1075
            // minDate: "-3D",
            maxDate: moment(),
            locale: 'es'
        });

        if ($('.fecha_fin_only_date').val() !== '') {
            $(".fecha_inicio_only_date").datetimepicker({
                useCurrent: false,
                minDate: moment(),
                locale: 'es',
                format: "YYYY-MM-DD",
                maxDate: $('.fecha_fin_only_date').val()
            });
        }
        else {
            $(".fecha_inicio_only_date").datetimepicker({
                useCurrent: false,
                minDate: moment(),
                locale: 'es',
                format: "YYYY-MM-DD"
            });
        }


        $(".fecha_inicio_update").datetimepicker({
            //  language: 'es',
            //  todayBtn: true,
            //  autoclose: true,
            //  showMeridian: true,
            // // startDate: getDate(),
            //  format: "yyyy-mm-dd hh:ii:ss"
            useCurrent: false, //Important! See issue #1075
            locale: 'es'
        });
        $(".fecha_fin").datetimepicker({
            //  language: 'es',
            //  todayBtn: true,
            //  autoclose: true,
            //  showMeridian: true,
            // // startDate: getDate(),
            //  format: "yyyy-mm-dd hh:ii:ss"
            useCurrent: false, //Important! See issue #1075
            minDate: moment(),
            locale: 'es'
            // format: "YYYY-MM-DD"
        });

        if ($('.fecha_inicio_only_date').val() !== '') {
            $(".fecha_fin_only_date").datetimepicker({
                useCurrent: false,
                locale: 'es',
                format: "YYYY-MM-DD",
                minDate: $('.fecha_inicio_only_date').val()
            });
        }
        else {
            $(".fecha_fin_only_date").datetimepicker({
                useCurrent: false,
                locale: 'es',
                format: "YYYY-MM-DD"
            });
        }

        $(".fecha_inicio_reporte").datetimepicker({
            useCurrent: false, //Important! See issue #1075
            locale: 'es',
            format: "YYYY-MM-DD"
        });

        $(".fecha_fin_reporte").datetimepicker({
            useCurrent: false, //Important! See issue #1075
            locale: 'es',
            format: "YYYY-MM-DD"
        });

        $(".hora").datetimepicker({
            useCurrent: false, //Important! See issue #1075
            locale: 'es',
            format: "HH:mm"
        });

        $("#fecha_inicio").on("dp.change", function (e) {
            $('#fecha_fin').data("DateTimePicker").minDate(e.date);
        });
        $("#fecha_fin").on("dp.change", function (e) {
            $('#fecha_inicio').data("DateTimePicker").maxDate(e.date);
        });

        $(".fecha_inicio").on("dp.change", function (e) {
            $('.fecha_fin').data("DateTimePicker").minDate(e.date);
        });
        $(".fecha_fin").on("dp.change", function (e) {
            $('.fecha_inicio').data("DateTimePicker").maxDate(e.date);
        });

        $(".fecha_inicio_only_date").on("dp.change", function (e) {
            $('.fecha_fin_only_date').data("DateTimePicker").minDate(e.date);
        });
        $(".fecha_fin_only_date").on("dp.change", function (e) {
            $('.fecha_inicio_only_date').data("DateTimePicker").maxDate(e.date);
        });

        $(".fecha_inicio_reporte").on("dp.change", function (e) {
            $('.fecha_fin_reporte').data("DateTimePicker").minDate(e.date);
        });

        $(".fecha_fin_reporte").on("dp.change", function (e) {
            $('.fecha_inicio_reporte').data("DateTimePicker").maxDate(e.date);
        });

        $(".fecha_aprobacion").datetimepicker({
            useCurrent: false, //Important! See issue #1075
            locale: 'es',
            format: "YYYY-MM-DD HH:mm",
        });

        $(".fecha_accidente").datetimepicker({
            //  language: 'es',
            //  todayBtn: true,
            //  autoclose: true,
            //  showMeridian: true,
            // // startDate: getDate(),
            //  format: "yyyy-mm-dd hh:ii:ss"
            useCurrent: false, //Important! See issue #1075
            locale: 'es'
        });

    }

    loadNotifications();
    initDatetimePickers();
});