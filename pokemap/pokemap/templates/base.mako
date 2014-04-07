<!DOCTYPE html>
<html>
<head>
    <title>Pok&eacute;map</title>
    <script type="text/javascript" src="/static/js/jquery-1.11.0.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function() {
            $('span').hide();
            $('area.grass-patch').hover(showSpan,
                                        hideSpan);
        });

        function showSpan() {
            $('span.' + $(this).attr('class')).show();
        }

        function hideSpan() {
            $('span.' + $(this).attr('class')).hide();
        }
    </script>
</head>

<body>

${next.body()}

</body>
