print("Bienvenido a Aventura en el Bosque Encantado")
print("Tu historia se desarrollara segun las decisiones que tomes")
print("Escribe tu eleccion cuando se te presenten las opciones")

print("Estas caminando en un bosque oscuro y encuentras dos objetos: Un fosforo y una linterna. ¿Con cuál te quedas?")
opcion = input("(FOSFORO/LINTERNA)").lower()

if opcion == "fosforo":
    print("Tomas y enciendes el fosforo, el bosque se ilumina y te encuentras.... CON UN OSO GRIZZLY")
    print("¿Que haces?")
    opcion = input("(CORRER/ESCONDERTE/GRITAR)").lower()

    if opcion == "correr":
        print("Decides correr lo mas rapido posible, pero el oso aun te persigue. Ves un rio que podrias cruzar")
        print("¿Que decides hacer?")
        opcion = input("(NADAR/CRUZAR EL PUENTE/BUSCAR OTRO CAMINO)").lower()
    
        if opcion == "nadar":
            print("Nadas hacia el otro lado del rio, el oso ya no te persigue, pero estas agotado y mojado.")
            print("¿Que haras ahora?")
            opcion = input("(DESCANSAR/EXPRIMIR ROPA/EXPLORAR)").lower()
            
            if opcion == "descansar":
                print("Descansas debajo de un arbol, te despiertas a mitad de la noche escuchando aullidos de lobo.")
                print("¿Ahora que?")
                opcion = input("(QUEDARSE QUIETO/ARMAR TRAMPAS)").lower()
                
                if opcion == "quedarse quieto":
                    print("Te quedas quieto y los lobos no notan tu presencia")
                    print("Al amanecer, encuentras un camino seguro a casa. Buena decision!")
                elif opcion == "armar trampas":
                    print("Armas trampas pero los lobos las evitan y te atacan")
                    print("Game Over!")
                else:
                    print("Opcion no valida, los lobos te encuentran mientras dudas")
                    print("Game Over!")
            
            elif opcion == "exprimir ropa":
                print("Pierdes tiempo exprimiendo tu ropa y terminas resfriado, sin mas energias para salir del bosque")
                print("Game Over!")
            elif opcion == "explorar":
                print("Exploras tus alrededores y encuentras una cabaña con provisiones y pasas la noche ahi de forma segura")
                print("Exito!")
            else:
                print("Opcion no valida, pierdes tiempo valioso")
                print("Game Over!")
      
        elif opcion == "cruzar el puente":
            print("El puente es viejo y cruje con tus pisadas, el oso te encuentra y se detiene")
            print("¿Como lo cruzas?")
            opcion = input("(RAPIDO/CAUTELOSO/VOLVER)").lower()
            
            if opcion == "rapido":
                print("Cruzas rapidamente, llegas al otro lado del rio justo antes de que el puente se derrumbe")
                print("El oso ya no te persigue, Logras escapar!")
            elif opcion == "cauteloso":
                print("Caminas lentamente por el puente, pero este se derrumba")
                print("Te caes al rio y la corriente te lleva. Game Over!")
            elif opcion == "volver":
                print("Vuelves y el oso te atrapa. Game Over!")
            else:
                print("Opcion invalida, el oso te alcanza mientras dudas.")
                print("Game Over!")
        
        elif opcion == "buscar otro camino":
            print("Buscas otra ruta y encuentras unas rocas que puedes escalar.")
            print("El oso ya no puede seguirte. Bien hecho!")
        else:
            print("Opcion no valida, el oso te atrapa mientras dudas")
            print("Game Over!")
 
    elif opcion == "esconderte":
        print("Te escondes detras de un gran arbol. El oso pasa de largo sin verte")
        print("Crees que estas seguro y de pronto escuchas una melodia singular")
        print("¿Que haces?")
        opcion = input("(SEGUIR LA MUSICA/QUEDARSE QUIETO/GRITAR POR AYUDA)")
        
        if opcion == "seguir la musica":
            print("Sigues la musica y resulta ser un hada que te guia a un camino seguro")
            print("Magia!")
#Voy a ser honesto, la IA se metio tremendo viaje con esta opcion en la historia, pero no pense en una mejor, por lo que asi quedo
        elif opcion == "quedarse quieto":
            print("Decides quedarte quieto, la musica se desvanece y te pierdes en el bosque")
            print("Game Over!")
        elif opcion == "gritar por ayuda":
            print("Gritas pidiendo ayuda. El oso regresa atraído por el ruido.")
            print("Game Over!")
        else:
            print("Opción no válida. Pierdes la oportunidad de escapar.")
            print("Game Over!")
   
    elif opcion == "gritar":
        print("Gritas con todas tus fuerzas y logras espantar al oso, pero tus gritos alertan a unos bandidos que estaban cerca")
        print("¿Que haces ahora?")
        opcion = input("(HUIR/HABLAR/PELEAR)")
       
        if opcion == "huir":
            print("Huyes y logras perder a los bandidos en el bosque")
            print("Encuentras un camino que da hacia un pueblo. Estas a salvo!")
        elif opcion == "hablar":
            print("Les hablas y descubres que no son malos, solo estan asustados com tu")
            print("Se ayudan mutuamente para lograr salir del bosque y lo consiguen. Buena decision!")
        elif opcion == "pelear":
            print("Intentas pelear, pero son demasiados. Game Over!")
        else:
            print("Opción no válida. Los bandidos te capturan.")
            print("Game Over!")
    else:
        print("Opción no válida. El oso te ataca mientras dudas.")
        print("Game Over!")

elif opcion == "linterna":
    print("Enciendes la linterna y ves un camino iluminado. De pronto, oyes algo entre los arboles")
    print("¿Que decides hacer?")
    opcion = input("(SEGUIR/BUSCAR/APAGAR LINTERNA)").lower()

    if opcion == "seguir":
        print("Sigues el camino hasta un claro con un extraño circulo de piedras")
        print("¿Como procedes?")
        opcion = input("(INSPECCIONAR/RODEAR/IGNORAR)").lower()

        if opcion == "inspeccionar":
            print("Al acercarte, las piedras empiezan a brillar y se abre un portal magico")
#Otra fumada de la IA
            print("¿Que haces?")
            opcion = input("(ENTRAR/TOCAR/HUIR)").lower()

            if opcion == "entrar":
                print("Entras al portal y resulta ser un reino magico. El comienzo de una nueva aventura")
                print("Pero sera contada en otra ocasion")
            elif opcion == "tocar":
                print("Al tocar el portal, recibes una vision que te ayuda a escapar")
                print("Destino cumplido!")
            elif opcion == "huir":
                print("Huyes del portal, pero te quedas atrapado en el bosque para siempre")
                print("Game Over!")
            else:
                print("Opcion no valida. El portal desaparece y te quedas atrapado")
                print("Game Over!")

        elif opcion == "rodear":
            print("Rodeas el circulo con cuidado y encuentras un camino hacia un pueblo")
            print("Has escapado!")
        elif opcion == "ignorar":
            print("Ignoras el círculo y continúas, pero caes en una trampa oculta.")
            print("Game Over!")
        else:
            print("Opción no válida. Pierdes el camino correcto.")
            print("Game Over!")
  
    elif opcion == "buscar":
        print("Buscas entre los arboles y encuentras un ciervo herido")
        print("¿Que haces?")
        opcion = input("(AYUDAR/DEJARLO)").lower()
        
        if opcion == "ayudar":
            print("Decides ayudarlo y lo curas con hierbas. Como agradecimiento, te guia por el bpsque hasta la salida")
            print("Buen karma!")
        elif opcion == "dejarlo":
            print("Decides dejarlo. Mas adelante, te pierdes sin guia.")
            print("Game Over!")
        else:
            print("Opcion no valida. El ciervo muere y te maldice")
            print("Game Over!")
    elif opcion == "apagar linterna":
        print("Apagas la linterna y esperas en silencio. Escuchas voces susurrantes")
        print("¿Cual es tu siguiente movimiento?")
        opcion = input("(ENCENDER/ESCUCHAR/REZAR)").lower()

        if opcion == "encender":
            print("Al encender la linterna, las voces callan y ves un camino seguro ante ti")
            print("Logras salir del bosque sin problemas!")
        elif opcion == "escuchar":
            print("Escuchas atentamente y las voces resultan ser parte de tu imaginacion, has perdido la cordura")
            print("Game Over!")
        elif opcion == "rezar":
#este final me causa algo de gracia, literal se salvo por la gracia del Espiritu Santo  
            print("Rezas y sientes una paz interior. Cuando abres los ojos, estás fuera del bosque.")
            print("Milagro!")
        else:
            print("Opción no válida. Las voces se enfurecen y te atacan.")
            print("Game Over!")

print("¡Gracias por jugar Aventura en el Bosque Encantado! Sientete libre de intentar otra ruta")

   

            


    


