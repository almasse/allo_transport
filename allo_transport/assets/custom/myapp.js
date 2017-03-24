
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

function renderMenu(){
    $.when(
        $.get('http://localhost:8000/menus/menu/', function(menu){
            $('#dynamic-menu').html(menu);
        })
    ).done(function(){
        $('#dynamic-menu a').each(function(){
            console.log($(this).attr('href'));
            var arr = $(this).attr('href').split("/");
            console.log(arr);
            var slug = arr[arr.length-2];
            console.log(slug);
            this.getAttribute('href') = "#";
            console.log($(this).attr('href'));
        });
    });
}


function renderAbout(){
    renderMenu();
    var aboutpageids = [];
    var about = 0 ;
    $.getJSON("http://localhost:8000/api/v2/pages/?format=json", function (data) {
        
        for (var key in data.items){
            if (data.items[key].meta.type == "allo_transport.AboutPage"){
                aboutpageids.push(data.items[key].id);
            }
        }
        aboutpageids.sort(function(a,b){
            return b-a;
        });
        console.log(aboutpageids);

        for (var id in aboutpageids){
            about = aboutpageids[id];
            break;
        }

        $.getJSON("http://localhost:8000/api/v2/pages/"+about+"/?format=json", function (page_data) {
            page_data.body1 = page_data.body1.split('src=\"/media/').join('src="http://localhost:8000/media/');

            var template = $('#template-about').html();
            var rendered = Mustache.render(template, page_data);
        
            $('#about').html(rendered);

        });

    });



}

function renderNews(slug){
    renderMenu();
    var id;
    $.getJSON("http://localhost:8000/api/v2/pages/?format=json", function (data) {
        for (var key in data.items){
            if (data.items[key].meta.slug == slug){
                id =data.items[key].id;
            }
        }
        $.getJSON("http://localhost:8000/api/v2/pages/"+id+"/?format=json", function (page_data) {
            page_data.body1 = page_data.body1.split('src=\"/media/').join('src="http://localhost:8000/media/');

            var template = $('#template-news').html();
            var rendered = Mustache.render(template, page_data);
        
            $('#news').html(rendered);

        });

    });


}




function renderIndex(){
    renderMenu();
    var newspagesids = [];
    var latestsnewsids = [];
    $.getJSON("http://localhost:8000/api/v2/pages/4/?format=json", function (page_data) {
        page_data.body1 = page_data.body1.split('src=\"/media/').join('src="http://localhost:8000/media/');
        page_data.body_title1 = page_data.body_title1.split('src=\"/media/').join('src="http://localhost:8000/media/');
        page_data.blue_body1 = page_data.blue_body1.split('src=\"/media/').join('src="http://localhost:8000/media/');

        var template = $('#template-partners').html();
        var rendered = Mustache.render(template, page_data);
        $('#partners').html(rendered);

        template = $('#template-index-body').html();
        rendered = Mustache.render(template, page_data);
        $('#index-body').html(rendered);

        template = $('#template-index-blue-body').html();
        rendered = Mustache.render(template, page_data);
        $('#index-blue-body').html(rendered);


        $('#carousel-item-list').eq(0).addClass('active');


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

    });
}

