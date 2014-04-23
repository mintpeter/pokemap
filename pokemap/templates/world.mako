<%inherit file="base.mako"/>

<%def name="title()">${c.region_identifier.title()}</%def>

<section class="blurb">
    Hover over the the map to see the route names. Click on a route to see more
    specific information.
</section>

<img src="/img/world/${c.gen_id}/${c.region_identifier}.png"
    class="world" usemap="#world">

<map name="world">
%for route in c.routes:
    <area shape="rect" coords="${route.x1},${route.y1},${route.x2},${route.y2}"
        class="${route.location.identifier} route"
        href="/map/${c.region_identifier}/gen${c.gen_id}/${route.location.name}">
%endfor
</map>

%for route in c.routes:
    <span class="${route.location.identifier} route">${route.location.name}</span>
%endfor
