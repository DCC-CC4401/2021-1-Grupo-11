function cerrarComentario(){
    let modal = document.getElementsByClassName("modal");
    modal.style.display = "none";
}

function abrirComentario(){
    let modal = document.getElementsByClassName("modal");
    modal.style.display = "block";
}


var modal = document.getElementsById("m1");

var cerrar = document.getElementsById("close");

var enviar = document.getElementsById("enviar_comentario");

var abrir = document.getElementsById("abrir_modal");


abrir.onclick = function() {
    modal.style.display = "block";
}

function confbox(){
    let cont = document.getElementById("abrir_modal");
    cont.style.display = "block";

}

cerrar.onclick = function() {
    modal.style.display = "none";
}
