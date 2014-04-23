<%inherit file="base.mako"/>

<%def name="title()">Home</%def>

<section class="blurb">
    <p>Welcome! The PKMN Map Project's goal is to gather map data from every game
    and relate that data to already-gathered Pok&eacute;mon encounter data.
    While this information is (hopefully) valuable to trainers, the primary
    drive of the project is to research the game data.</p>

    <p>To see how the site works, check out FireRed and LeafGreen's
    <a href="${request.route_url('map', region='kanto', gen_id='3', location_name='route 1')}">
    Route 1</a>. Then, head over to the 
    <a href="${request.route_url('locations')}">locations</a> page to peruse
    all the available data.</p>

    <p>With all that in mind, I need help. If you are looking for a project to
    become involved with, head over to the 
    <a href="${request.route_url('about')}">about</a> page to find out how you
    can help.</p>
</section>
