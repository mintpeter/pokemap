$(document).ready(function() {
    $('table.encounters').hide();
    $('area').hover(showSpan,
                    hideSpan);
});

function showSpan() {
    $('table.' + $(this).attr('class')).show();
}

function hideSpan() {
    $('table.' + $(this).attr('class')).hide();
}
