/* Se instancia un objeto literal newUser para llenarlo 
con los valores que el usuaro cargue en el formulario*/
const newUser = {
    user: '',
    email: '',
    password:'',
    passwordConfirm:''
}

/* Mediante el DOM vamos a seleccionar los input del formulario*/
const user = document.querySelector ('#inputUsuario');
user.addEventListener('input',cargarObjeto);/* "escuchamos el evento input"*/

const email = document.querySelector ('#inputEmail');
email.addEventListener('input',cargarObjeto);/* "escuchamos el evento input"*/

const password = document.querySelector ('#passwordEmail');
password.addEventListener('input',cargarObjeto);/* "escuchamos el evento input"*/

const passwordConfirm = document.querySelector ('#passwordConfirm');
passwordConfirm.addEventListener('input',cargarObjeto);/* "escuchamos el evento input"*/

document.addEventListener('submit',(event)=>{ /* "escuchamos el evento submit"*/
    event.preventDefault()   /* "anula lo q se haria por defecto con submit(ir al servidor)"*/
    if (newUser.password != newUser.passwordConfirm){
        alert('Las contraseñas ingresadas no coinciden; por favor vuelva a ingresarlas')
        return;
    }
    alert('Usuario registrado correctamente')
}) 

function cargarObjeto(event){
    newUser[event.target.name]=event.target.value;
    console.log(newUser);
}