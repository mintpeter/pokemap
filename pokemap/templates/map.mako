<%inherit file="base.mako"/>

<%block name="title">${c.location.name}</%block>

<section class="blurb">
    Hover over the route to see where you can encounter wild pokemon.
</section>

<div id="route-image">
    <img class="route" src="/img/route/${c.gen_id}/${c.location.identifier}.png" alt="${c.location.identifier}" usemap="#route">
</div>

<map name="route">
%for patch_type in c.patches:
    %for patch in c.patches[patch_type]:
    <area shape="rect" coords="${patch.x1},${patch.y1},${patch.x2},${patch.y2}"
        class="${patch_type.name}-encounters encounters" href="#">
    %endfor
%endfor
</map>



%for method in c.encounters:
<table class="${filter(lambda x: x.encounter_method_id == method.id, c.patch_types)[0].name}-encounters encounters">
    <thead>
        <tr>
            <th colspan="999">
                <img src="/img/method/${method.identifier}.png" alt="${method.identifier}">
                <span>${method.name}</span>
            </th>
        </tr>
        <tr>
            <th>
                <img src="/img/poke-ball.png" alt="poke-ball">
                <span>Pokemon<span>
            </th>
    %for version in c.versions:
            <th>
                <img src="/img/version/${version.identifier}.png" alt="${version.identifier}">
                <span>${version.name}</span>
            </th>
    %endfor
        </tr>
    </thead>
    <tbody>
    %for pokemon in c.encounters[method]:
        <tr>
            <td>
                <img src="/img/pokemon/${pokemon.id}.png" alt="${pokemon.identifier}">
                <span>${pokemon.name}</span>
            </td>
        %for version in c.versions:
            <td>${c.encounters[method][pokemon][version]}%</td>
        %endfor
        </tr>
    %endfor
    </tbody>
</table>
%endfor
