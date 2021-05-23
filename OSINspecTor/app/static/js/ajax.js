const results_div = document.getElementById("results");
const res = window.location.pathname.split("/")[1]
const spinner = document.getElementById("spinner-div");

function messageBox(severity, message){
    return `<br><div class="alert alert-${severity}" role="alert">${message}<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>`
}


$('#btn_geo').click(function() {
    console.log("click");
    results_div.innerHTML = ""
    spinner.style.visibility= "visible";
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
            aux='<div class="container bg-light text-dark">'
            aux+='<table class="table table-striped">'
            aux+='<thead><tr><th scope="col">Tag</th> <th scope="col">Value</th></tr></thead>'
            aux+='<tbody>'
            aux+=`<tr><td>Latitude</td><td>${response.results.latitude}</td>`
            aux+=`<tr><td>Longitude</td><td>${response.results.longitude}</td>`
            aux+=`<tr><td>City</td><td>${response.results.city}</td>`
            aux+=`<tr><td>Region</td><td>${response.results.region}</td>`
            aux+=`<tr><td>Country</td><td>${response.results.country}</td>`
            aux+=`<tr><td>Flag</td><td>${response.results.flag}</td>`
            aux+='</tbody></table></div>'
            spinner.style.visibility= "hidden";
            results_div.innerHTML = aux
        },
        error: function(response){
            message=response.responseJSON.results;
            console.log(message);
            results_div.innerHTML=messageBox("danger",message)
            spinner.style.visibility= "hidden";
        }
    }); 
});

$('#btn_em').click(function() {
    results_div.innerHTML = messageBox("info", "La búsqueda de emails tarda aproximadamente 30 segundos.")
    document.getElementById("btn_em").disabled = true;
    spinner.style.visibility= "visible";
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
            aux='<div class="container bg-light text-dark">'
            aux+='<div class="table-wrapper-scroll-y my-custom-scrollbar">'
            aux+='<table class="table table-bordered table-striped mb-0">'
            aux+='<thead><tr><th scope="col">#</th><th scope="col">Email</th></tr></thead>'
            aux+='<tbody>'
            Object.keys(response.results).forEach(element => {
                aux+=`<tr><td>${element}</td><td>${response.results[element]}</td></tr>`     
            });

            aux+='</tbody></table></div>'
            spinner.style.visibility= "hidden";
            results_div.innerHTML = aux
            document.getElementById("btn_em").disabled = false;
        },
        error: function(response) {
            document.getElementById("btn_em").disabled = false;
            message=response.responseJSON.results;
            console.log(message);
            results_div.innerHTML=messageBox("danger",message)
            spinner.style.visibility= "hidden";
        },
    }); 
});

$('#btn_rev').click(function() {
    console.log("click");
    results_div.innerHTML = ""
    spinner.style.visibility= "visible";
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
            spinner.style.visibility= "hidden";
            if (response.results==null){
                results_div.innerHTML=messageBox("warning", "Esta ip no tiene un nombre de dominio asociado")
            } else {
                aux='<div class="container bg-light text-dark">'
                results_div.innerHTML= aux+`<p>El dominio al que pertenece la ip ${dir} es: ${response.results}</p></div>`
            }
        },
        error: function(response){
            message=response.responseJSON.results;
            console.log(message);
            results_div.innerHTML=messageBox("danger",message)
            spinner.style.visibility= "hidden";
        }
    }); 
});

$('#btn_sub').click(function() {
    document.getElementById("btn_sub").disabled = true;
    results_div.innerHTML = ""
    spinner.style.visibility= "visible";
    console.log("click");
    dir=$('#form_input').val();
    $.ajax({
        method: 'POST',
        url: `{% url '${res}' %}`,
        data: {
            'dir': dir, 
            'method': "sub",
        },
        dataType: "json",
        success: function(response) {
            tablejson=response.results.df_dict
            imagebase=response.results.graph
            aux=`<img id="mat-img" src="data:image/png; base64, ${imagebase}"><br><br>`
            aux+='<div class="container bg-light text-dark">'
            aux+='<div class="table-wrapper-scroll-y my-custom-scrollbar">'
            aux+='<table class="table table-bordered table-striped mb-0">'
            aux+='<thead><tr><th scope="col">#</th><th scope="col">Nombre</th><th scope="col">Dirección</th><th scope="col">Tipo</th></tr></thead>'
            aux+='<tbody>'
            pos=0
            Object.keys(tablejson.name).forEach(element => {
                aux+=`<tr><td>${element}</td><td>${tablejson.name[element]}</td><td>${tablejson.value[pos]}</td><td>${tablejson.type[pos]}</td></tr>` 
                pos+=1;    
            });
            aux+='</tbody></table></div>'
            spinner.style.visibility= "hidden";
            results_div.innerHTML = aux
            document.getElementById("btn_sub").disabled = false;
        },
        error: function(response) {
            document.getElementById("btn_sub").disabled = false;
            message=response.responseJSON.results;
            console.log(message);
            results_div.innerHTML=messageBox("danger",message)
            spinner.style.visibility= "hidden";
        },
    }); 
});