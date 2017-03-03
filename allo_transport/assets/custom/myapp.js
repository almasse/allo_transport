$(document).ready(function () {

    $.getJSON("http://localhost:8000/api/v2/pages/4/?format=json", function (page_data) {
        
        console.log(page_data); 
        var template = $('#template-partners').html();
        var rendered = Mustache.render(template, page_data);
        console.log(rendered);
        $('#partners').html(rendered);

    });


});




