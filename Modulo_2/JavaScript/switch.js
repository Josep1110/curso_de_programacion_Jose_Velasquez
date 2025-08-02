//Ejercicio 1

let diadelasemana = 4

switch (diadelasemana){
    case 1:
        console.log("Lunes");
        break;
    case 2:
        console.log("Martes");
        break;
    case 3:
        console.log("Miercoles");
        break;
    case 4:
        console.log("Jueves");
        break;
    case 5:
        console.log("Viernes");
        break;
    case 6:
        console.log("Sabado");
        break;
    case 7:
        console.log("Domingo");
        break;
    default:
        console.log("Numero invalido, ingresa un numero del 1 al 7")
        break;
} 

//Ejercicio 2

let opcionMenu = prompt("Ingresa una opcion: INICIAR/GUARDAR/SALIR:");

switch (opcionMenu.toLowerCase()){
    case "iniciar":
        console.log("Cargando nueva partida")
        break;
    case "guardar":
        console.log("Progreso guardado correctamente")
        break;
    case "salir":
        console.log("Cerrando el juego...")
        break;
    default:
        console.log("Opcion invalida, intentelo de nuevo")
        break;
}

//Ejercicio 3

let mes = prompt("Ingrese un mes:");

switch (mes.toLowerCase()){
    case "diciembre":
    case "enero":
    case "febrero":
        console.log("Invierno");
        break;
    case "marzo":
    case "abril":
    case "mayo":
        console.log("Primavera");
        break;
    case "junio":
    case "julio":
    case "agosto":
        console.log("Verano");
        break;
    case "septiembre":
    case "octubre":
    case "noviembre":
        console.log("Otoño");
        break;
    default:
        console.log("Error. Ingresa un nombre de mes valido")
}



