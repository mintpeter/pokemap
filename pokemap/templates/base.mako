<!DOCTYPE html>
<html>
<head>
    <title>Pok&eacute;map &mdash; ${self.title()}</title>
    <script type="text/javascript" src="/static/js/jquery-1.11.0.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function() {
            $('table.encounters').hide();
            $('area').hover(showSpan,
                                        hideSpan);
        });

        function showSpan() {
            $('table.' + $(this).attr('class')).show();
        }

        function hideSpan() {
            $('table.' + $(this).attr('class')).hide();
        }
    </script>

    <link rel="stylesheet" type="text/css" href="/css/style.css">
</head>

<body>
    <h2><%block name="title"/></h2>
${next.body()}

</body>
