<%inherit file="base.mako"/>

<img class="route" src="/static/route/${c.gen_id}/${c.location.identifier}.png" alt="Route 1" usemap="#route1">

<map name="route1">
%for patch in patches:
    <area shape="rect" coords="${patch.x1},${patch.y1},${patch.x2},${patch.y2}"
        class="grass-patch" alt="grass" href="#">
%endfor
</map>

%for method in sorted_encounters:
<table class="${method.identifier}-encounters encounters">
    <thead>
        <tr>
            <th colspan="999">${method.name}</th>
        </tr>
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
