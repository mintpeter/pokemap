$(document).ready(function() {
    $('table.encounters').hide();
    $('area.encounters').hover(showEncounterTables, hideEncounterTables);
    $('span.route').hide();
    $('area.route').hover(showRouteNameSpan, hideRouteNameSpan);
});

function showEncounterTables() {
    $('table.' + $(this).attr('class').split(' ')[0]).show();
}

function hideEncounterTables() {
    $('table.' + $(this).attr('class').split(' ')[0]).hide();
}

function showRouteNameSpan() {
    $('span.' + $(this).attr('class').split(' ')[0]).show();
}

function hideRouteNameSpan(){
    $('span.' + $(this).attr('class').split(' ')[0]).hide();
}
