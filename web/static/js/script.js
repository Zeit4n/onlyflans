/*
$(document).ready(function(){
    $('.navbar a').mouseenter(function() {
        $(this).addClass('text-primary fw-bold');
    });
    
    $('.navbar a').mouseleave(function() {
        $(this).removeClass('text-primary fw-bold');
    })
    });
*/
/*
// Espera a que el DOM se haya cargado completamente
document.addEventListener("DOMContentLoaded", function() {
    // Obtiene todos los enlaces del navbar
    const navbarLinks = document.querySelectorAll(".navbar-nav .nav-link");
    
    // Recorre cada enlace y agrega los eventos
    navbarLinks.forEach(function(link) {
        // Evento cuando el mouse pasa sobre el enlace
        link.addEventListener("mouseover", function() {
            link.style.color = "white";  // Cambia el color del texto a azul
            //link.style.backgroundColor = "#f0f0f0";  // Cambia el color de fondo (opcional)
        });

        // Evento cuando el mouse sale del enlace
        link.addEventListener("mouseout", function() {
            link.style.color = "";  // Restaura el color original
            link.style.backgroundColor = "";  // Restaura el color de fondo
        });
    });
});*/
$(document).ready(function(){
    $('.btn-primary').mouseenter(function() {
        $(this).removeClass('btn-primary');
        $(this).addClass('btn-danger');
    });
    $('.btn-primary').mouseleave(function() {
        $(this).removeClass('btn-danger');
        $(this).addClass('btn-primary');
    })
    $('#enviarContacto').click(function(){
        alert("Su contacto ha sido recibido! Muchas gracias");
    });
    $('.rate').click(function(){
        var user_rate = parseInt(prompt("Ingresa tu valoración para este flan (de 1 a 5)"));
        while (!Number.isInteger(user_rate) || user_rate < 1 || user_rate > 5){
            user_rate = parseInt(prompt("Debes ingresar un valor numérico entre 1 y 5 para tu valoración"));
        }
        if (user_rate) {
            var flan_id = $(this).attr('id');
            fetch(window.location.pathname, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ 
                    'user_rate': Number(user_rate),
                    'flan_id': flan_id})
            })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.log('Error:', error));
        }
        alert("Gracias por tu opinión! Para ver los cambios actualiza la página.")
    });
});
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
/*
const enviarContacto = document.getElementById('enviarContacto');
enviarContacto.addEventListener("click", function() {
    alert("Su contacto ha sido recibido! Muchas gracias")
    });*/
//enviarContacto.onclick = alert("Su contacto ha sido recibido! Muchas gracias");
