const results_div = document.getElementById("results");


$('#btn_rev').click(function() {
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