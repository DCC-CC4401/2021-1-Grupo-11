
function open_comment_modal(modal){
    let cont = document.getElementById(modal);
    cont.style.display = "block";
}
function close_comment_modal(modal){
	let cont = document.getElementById(modal)
	cont.style.display = "none";
}

function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
    results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

function setCourseName(){
  course_name = document.getElementById('course_name');
  course_name.innerHTML += getParameterByName('course_name');
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
  			 "Ingenieria de Software"]}];

function validateChecked(name){
  check = document.getElementsByName(name);
  //Ver posibilidad de revisar seleccion unica
  let checked = false;
  for (let i = 0; i < 5; i++) {
    checked = checked || check[i].checked;
  }
  return checked;
}

function mostrarError(msg){
  let cont = document.getElementById("error");
  let contmsg = document.getElementById("errormsg");
  contmsg.innerHTML = msg;
  cont.style.display = "flex";
  //setTimeout(function(){cont.style.display = "none";},10000);
}

function confBox(){
  if(validacionForm()){
    form = document.getElementById("form");
    form.submit();
  }
}

function salir(val){
  let cont = document.getElementById(val);
  cont.style.display = "none";
}

function validacionForm(){

  let msg =  `<div style="display:flex; align-items:flex-start;">
                <h2 style="display:inline-block; margin-right:15%;">¡Error!</h2>
                <div id='salir' style="padding: 1rem 1rem; margin: -1rem -1rem -1rem auto; cursor:pointer;" onclick="salir('error')"">x</div>
              </div>
              <ul class="errorList"style="padding:15px;">`;
  let validate = true;

  let year = document.getElementById("year").value;
  let semester = document.getElementById("semester").value;
  let section = document.getElementById("section").value;
  
  //Validacion Año
  if(year>2021 || year<2011){
    msg = msg.concat("<li>El año ingresado no esta dentro del rango valido [2011-2021].</li>");
    validate =  false;
  }

  //Validacion Semestre
  if(semester==="0"){
    msg = msg.concat("<li>Seleccione un Semestre.</li>");
    validate =  false;
  }

  //Validacion Seccion
  if(section==="0"){
    msg = msg.concat("<li>Seleccione una Seccion.</li>");
    validate =  false;
  }

  //Validacion recommendation_level
  if(!validateChecked("recommendation_level")){
    msg = msg.concat("<li>Seleccione una opcion para: 'Recomendación'.</li>");
    validate =  false;
  }

  //Validacion fondness_level
  if(!validateChecked("fondness_level")){
    msg = msg.concat("<li>Seleccione una opcion para: 'Interes en la materia'.</li>");
    validate =  false;
  }

  //Validacion difficulty_level
  if(!validateChecked("difficulty_level")){
    msg = msg.concat("<li>Seleccione una opcion para: 'Dificultad'.</li>");
    validate =  false;
  }

  //Validacion required_time_level
  if(!validateChecked("required_time_level")){
    msg = msg.concat("<li>Seleccione una opcion para: 'Tiempo de dedicacion'.</li>");
    validate =  false;
  }

  //Validacion content_adjustment_level
  if(!validateChecked("content_adjustment_level")){
    msg = msg.concat("<li>Seleccione una opcion para: 'Evaluaciones'.</li>");
    validate =  false;
  }

  //Validacion stress_level
  if(!validateChecked("stress_level")){
    msg = msg.concat("<li>Seleccione una opcion para: 'Estres'.</li>");
    validate =  false;
  }

  //Validacion usefulness_level
  if(!validateChecked("usefulness_level")){
    msg = msg.concat("<li>Seleccione una opcion para: 'Utilidad'.</li>");
    validate =  false;
  }

  //Validacion practicality_level
  if(!validateChecked("practicality_level")){
    msg = msg.concat("<li>Seleccione una opcion para: 'Enfoque del curso'.</li>");
    validate =  false;
  }

  //Validacion teamwork_level
  if(!validateChecked("teamwork_level")){
    msg = msg.concat("<li>Seleccione una opcion para: 'Modalidad de trabajo'.</li>");
    validate =  false;
  }

  msg = msg.concat("</ul>");
  if(!validate){
    mostrarError(msg)
  }

  return validate;

}
  



