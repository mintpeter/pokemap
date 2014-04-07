<%inherit file="base.mako"/>

<img src="/static/route/${route_id}.png" alt="Route ${route_id}" usemap="#route${route_id}"/>

<map name="route${route_id}">
%for patch in patches:
    <area shape="rect" coords="${patch.x1},${patch.y1},${patch.x2},${patch.y2}" class="grass-patch" alt="grass" href="#"/>
%endfor
</map>

<span class="grass-patch">
Some talking about the grass stuff on route ${route_id}
</span>
<span class="water-patch">
This one talks about water. Water is great.
</span>
