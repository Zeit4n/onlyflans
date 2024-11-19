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
    $('#enviarContacto').click(function(){
        alert("Su contacto ha sido recibido! Muchas gracias");
    });
    $('#valorar').click(function(){
        alert("Esta función todavía no la implemento")
    })
});
/*
const enviarContacto = document.getElementById('enviarContacto');
enviarContacto.addEventListener("click", function() {
    alert("Su contacto ha sido recibido! Muchas gracias")
    });*/
//enviarContacto.onclick = alert("Su contacto ha sido recibido! Muchas gracias");
