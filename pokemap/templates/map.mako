<%inherit file="base.mako"/>

<img src="/static/route/1.png" alt="Route 1" usemap="#route1"/>

<map name="route1">
%for patch in patches:
    <area shape="rect" coords="${patch.x1},${patch.y1},${patch.x2},${patch.y2}"
        class="grass-patch" alt="grass" href="#"/>
%endfor
</map>

<span class="grass-patch">
Some talking about the grass stuff on da route.

Encounter Pokemon:
##%for encounter in encounters:
##<p>
##    ${encounter.pokemon.name} &mdash; ${encounter.min_level} &ndash; ${encounter.max_level}<br/>
##    %for condition_value in encounter.condition_values:
##        ${condition_value.name}, default: ${condition_value.is_default}<br/>
##    %endfor
##    ${encounter.slot.rarity}<br/>
##</p>
##%endfor

%for method in sorted_encounters:
<table class="encounters">
    <thead>
        <tr>
            <th>Pokemon</th>
    %for version in c.versions:
            <th>${version.name}</th>
    %endfor
        </tr>
    </thead>
    <tbody>
    %for pokemon in sorted_encounters[method]:
        <tr>
            <td>${pokemon.name}</td>
        %for version in c.versions:
            <td>${sorted_encounters[method][pokemon][version]}%</td>
        %endfor
        </tr>
    %endfor
    </tbody>
</table>
%endfor
            

</span>
<span class="water-patch">
This one talks about water. Water is great.
</span>
