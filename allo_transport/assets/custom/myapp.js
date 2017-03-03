
var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};

function renderNews(id){

    $.getJSON("http://localhost:8000/api/v2/pages/"+id+"/?format=json", function (page_data) {

        var template = $('#template-news').html();
        var rendered = Mustache.render(template, page_data);
        
        $('#news').html(rendered);

    });
}

function renderIndex(){

    var newspagesids = [];
    var latestsnewsids = [];
    $.getJSON("http://localhost:8000/api/v2/pages/4/?format=json", function (page_data) {

        var template = $('#template-partners').html();
        var rendered = Mustache.render(template, page_data);
        
        $('#partners').html(rendered);

    });
    $.getJSON("http://localhost:8000/api/v2/pages/?format=json", function (data) {
        
        for (var key in data.items){
            if (data.items[key].meta.type == "allo_transport.NewsPage"){
                newspagesids.push(data.items[key].id);
            }
        }

        newspagesids.sort(function(a,b){
            return b-a;
        });
        console.log(newspagesids);

        var count = 0;
        for (var id in newspagesids){
            
            if (count == 4){
                break;
            }
            count = count + 1 ;
            latestsnewsids.push(newspagesids[id]);
        }
        console.log(latestsnewsids);
        for (var ids in latestsnewsids){
            $.getJSON("http://localhost:8000/api/v2/pages/"+latestsnewsids[ids]+"/?format=json", function(page){

                var template = $('#template-news').html();
                var rendered = Mustache.render(template, page);
                $('#news').append(rendered);
            });
        }
        //var template = $('#template-partners').html();
        //var rendered = Mustache.render(template, page_data);
        //console.log(rendered);
        //$('#partners').html(rendered);

    });
}

