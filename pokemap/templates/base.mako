<%def name="title()"/>

<!DOCTYPE html>
<html>
    <head>
        <title>Pok&eacute;map &mdash; ${self.title()}</title>

        <script type="text/javascript" src="/js/jquery-1.11.0.min.js"></script>
        <script type="text/javascript" src="/js/map-hover.js"></script>
        
	<link href='http://fonts.googleapis.com/css?family=Roboto' rel='stylesheet' type='text/css'>
        <link type="text/css" rel="stylesheet" href="/css/style.css">
    </head>

    <body>
        <header>
            <img src="/img/town-map-gen3.png" alt="town map">
            <h1>Pok&eacute;map</h1>
            <p>your Pok&eacute;gear doesn't do this</p>
        </header>
        <nav>
            <ul>
                <li><a href="/"><img src="/img/escape-rope.png" alt="escape rope">Home</a></li>
                <li><a href="/locations"><img src="/img/town-map.png" alt="town map">Locations</a></li>
                <li><a href="/about"><img src="/img/photo-album.png" alt="photo album">About</a></li>
                <li><a href="/contact"><img src="/img/retro-mail.png" alt="retro mail">Contact</a></li>
            </ul>
        </nav>
        <div id="main">
            <h2>${self.title()}</h2>
            ${next.body()}
            <div class="clear">&nbsp;</div>
        </div>
        <footer>
            Pok&eacute;mon belongs to GameFreak, and <a href="http://zackmarvel.com">I</a> made this website.
        </footer>
    </body>
</html>
