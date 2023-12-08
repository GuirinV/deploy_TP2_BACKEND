const botonPacientes=document.querySelector('#botonPacientes')
botonPacientes.addEventListener('click',cargarPacientes)

function cargarPacientes(){
    const result=fetch('https://jsonplaceholder.typicode.com/users')
      .then(response => response.json())
      .then(json => cargar(json))

}

function cargar(datos){
    // datos.forEach(element => {
    //     const {id,name,username,email, address: {street, suite, city}}=element
    //     //console.log(street)
    // });

    //Se crea la tabla
    let html= `<table>
                <thead>
                <tr>
                <th>Id</th>
                <th>Name</th>
                <th>Username</th>
                <th>Email</th>
                <th>Street</th>
                <th>Suite</th>
                <th>City</th>
                </tr>
                </thead>

                <tbody>`
    
    //se agregan los datos a la tabla
    html+=datos.reduce((ac,e)=>{
        const {id,name,username,email,address: {street, suite, city}}=e
        
        ac+=`
        <tr>
        <td>${id}</td>
        <td>${name}</td>
        <td>${username}</td>
        <td>${email}</td>
        <td>${street}</td>
        <td>${suite}</td>
        <td>${city}</td>
        </tr>
        
        `
        return ac
    },'')
    html+=  `
    </tbody>
    
    </table>`          
    console.log (html)
    const divdatos=document.querySelector('#datos')
    divdatos.innerHTML=html
}

