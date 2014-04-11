<%inherit file="base.mako"/>

<img class="route" src="/static/route/${c.gen_id}/${c.location.identifier}.png" alt="Route 1" usemap="#route1">

<map name="route1">
%for patch_type in c.patches:
    %for patch in c.patches[patch_type]:
    <area shape="rect" coords="${patch.x1},${patch.y1},${patch.x2},${patch.y2}"
        class="${patch_type.name}-encounters" href="#">
    %endfor
%endfor
</map>



%for method in c.encounters:
<table class="${filter(lambda x: x.encounter_method_id == method.id, c.patch_types)[0].name}-encounters encounters">
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
    %for pokemon in c.encounters[method]:
        <tr>
            <td>${pokemon.name}</td>
        %for version in c.versions:
            <td>${c.encounters[method][pokemon][version]}%</td>
        %endfor
        </tr>
    %endfor
    </tbody>
</table>
%endfor
