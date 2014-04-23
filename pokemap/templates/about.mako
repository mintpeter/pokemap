<%inherit file="base.mako"/>

<%def name="title()">About</%def>

<h3>Project Goals</h3>
<ul>
    <li>Gather map data from the game ROMs, with the following priority:
        <ol>
            <li>R/B/Y</li>
            <li>G/S/C</li>
            <li>FR/LG</li>
            <li>R/S/E</li>
            <li>D/P/Pt</li>
            <li>B/W/B2/W2</li>
            <li>X/Y</li>
        </ol>
    </li>
    <li>Render images from ripped map data</li>
    <li>Relate map images to PKMN encounters</li>
    <li>Make all data open-source and easily accessible on all platforms</li>
    <li>Display all map images on this web page</li>
</ul>

<h3>Help Us!</h3>
<p>At the moment, it's just me (Zack). I downloaded a hex editor for the first
time a couple of days ago. I've been programming for a couple of years now, but
I'm going to have to put a lot of time into research to implement this project.
These are the folks I'm asking to help:</p>

<ul>
    <li>Someone who knows their way around Pok&eacute;mon game ROMs<li>
    <li>Someone who wants to design things&mdash;I'm no website designer, and
    I can spend my time better writing Python</li>
</ul>

<p>I can handle the second part myself, it's just tedious to have to write up
all these templates when there's still so much to do with the rest of the
project. If I spend a lot of time on it, I'm sure I can do the first part, too.
I just want to finish this project without getting burned out on it.</p>

<p>If you want to help, please visit the
<a href="${request.route_url('contact')}">contact</a> page and email me. :)</p>
