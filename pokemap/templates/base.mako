<!DOCTYPE html>
<html>
<head>
    <title>Pok&eacute;map</title>
    <script type="text/javascript" src="/static/js/jquery-1.11.0.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function() {
            $('table.walk-encounters').hide();
            $('area.grass-patch').hover(showSpan,
                                        hideSpan);
        });

        function showSpan() {
//            $('div.' + $(this).attr('class')).show();
            $('table.walk-encounters').show();
        }

        function hideSpan() {
//            $('div.' + $(this).attr('class')).hide();
            $('table.walk-encounters').hide();
        }
    </script>

    <link rel="stylesheet" type="text/css" href="/css/style.css">
</head>

<body>

${next.body()}

</body>
