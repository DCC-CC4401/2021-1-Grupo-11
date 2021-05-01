
function open_comment_modal(modal){
    let cont = document.getElementById(modal);
    cont.style.display = "block";
}
function close_comment_modal(modal){
	let cont = document.getElementById(modal)
	cont.style.display = "none";
}

let cursos_departamento = [{"departamento": "Ingenieria Mecanica",
 "cursos": ["Ciencias de los materiales",
 			"Dibujo Mecanico",
 			" Mecanica Estatica"]},
 {"departamento": "Ingenieria Electrica",
  "cursos": ["Laboratorio de Ingenieria Electrica",
  			 "Circuitos Electronicos y Analogicos",
  			 "Señales y Sistemas 1"]},
 {"departamento": "Ciencias de la Computacion",
  "cursos": ["Herramientas Computacionales para Ingenierai y Ciencias",
  			 "Introducicon a la Programacion",
  			 "Algoritmos y Electricastructuras de Datos",
  			 "Ingenieria de Software"]}]



