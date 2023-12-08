/* definimos constantes simulando un usuario valido*/
const USER_TEMP= 'verocarlospaz'
const USER_EMAIL= 'veronica.guirin@oulook.es'
const USER_PASSWORD= '123456'

/*creamos un objeto literal para cargar los valores que el usuario vaya 
ingresando en la ficha de loguin*/
const user= {
    usuario: '',
    password:''
}

/* capturamos el usuario y password*/
const usuario= document.querySelector('#usuario')
usuario.addEventListener ('input',cargarObjeto)
const password= document.querySelector('#password')
password.addEventListener ('input',cargarObjeto)

/* funcion para cargar el objeto user (logueo de pacientes)*/
function cargarObjeto(e){
    user[e.target.name]=e.target.value;
    console.log(user);
}

/* capturamos boton Ingresar*/
document.addEventListener('submit',(event)=>{ /* "escuchamos el evento submit"*/
    event.preventDefault()   /* "anula lo q se haria por defecto con submit(ir al servidor)"*/
    
    const { usuario, password } = user

    if (usuario!==USER_TEMP || password!==USER_PASSWORD) {
        alert('Usuario o password incorrecto')
        return;
    }
    alert ('Bienvenido ' + usuario)
    location.href='./dashboard.html'
}) 
