const results_div = document.getElementById("results");
const res = window.location.pathname.split("/")[1]



$('#btn_geo').click(function() {
    results_div.innerHTML=""
    console.log("click");
    dir=$('#form_input').val();
    $.ajax({
        method: 'POST',
        url: `{% url '${res}' %}`,
        data: {
            'dir': dir, 
            'method': "geo",
        },
        dataType: "json",
        success: function(response) {
            aux='<table class="table table-striped">'
            aux+='<thead><tr><th scope="col">Tag</th> <th scope="col">Value</th></tr></thead>'
            aux+='<tbody>'
            aux+=`<tr><td>Latitude</td><td>${response.results.latitude}</td>`
            aux+=`<tr><td>Longitude</td><td>${response.results.longitude}</td>`
            aux+=`<tr><td>City</td><td>${response.results.city}</td>`
            aux+=`<tr><td>Region</td><td>${response.results.region}</td>`
            aux+=`<tr><td>Country</td><td>${response.results.country}</td>`
            aux+=`<tr><td>Flag</td><td>${response.results.flag}</td>`
            aux+='</tbody></table>'
            results_div.innerHTML = aux
        }
    }); 
});

$('#btn_em').click(function() {
    document.getElementById("btn_em").disabled = true;
    results_div.innerHTML="";
    console.log("click");
    dir=$('#form_input').val();
    $.ajax({
        method: 'POST',
        url: `{% url '${res}' %}`,
        data: {
            'dir': dir, 
            'method': "em",
        },
        dataType: "json",
        success: function(response) {
            aux='<div class="table-wrapper-scroll-y my-custom-scrollbar">'
            aux+='<table class="table table-bordered table-striped mb-0">'
            aux+='<thead><tr><th scope="col">#</th><th scope="col">Email</th></tr></thead>'
            aux+='<tbody>'
            Object.keys(response.results).forEach(element => {
                aux+=`<tr><td>${element}</td><td>${response.results[element]}</td></tr>`     
            });

            aux+='</tbody></table>'
            results_div.innerHTML = aux
            document.getElementById("btn_em").disabled = false;
        },
        error: function(response) {
            console.log("errroooor: ", response)
            document.getElementById("btn_em").disabled = false;
        },
    }); 
});

$('#btn_rev').click(function() {
    results_div.innerHTML=""
    console.log("click");
    dir=$('#form_input').val();
    $.ajax({
        method: 'POST',
        url: "{% url 'ip' %}",
        data: {
            'dir': dir, 
            'method': "rev",
        },
        dataType: "json",
        success: function(response) {
            results_div.innerHTML= `<p>El dominio al que pertenece la ip ${dir} es: ${response.results}</p>`
        }
    }); 
});
