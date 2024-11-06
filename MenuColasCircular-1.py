from ColaCir import ColaCircular

def menuPrinColaCir():
    while True:
        print("\nMenu Cola Circular")
        print("1. Crear")
        print("2. Adicionar")
        print("3. Genera Aleatorio cola ")
        print("4. Eiminar")
        print("5. Listar Cola 1")
           
        print("*   Salir")
        opcion=input("Elija Opcion: ")
        if opcion=="1":
            n=(int(input("Tamaño de cola circular: ")))+1
            col=ColaCircular(n)
        elif opcion=="2":
            e=int(input("Ingrese dato: "))
            col.adicionar(e)
        elif opcion=="3":
            col.adicionaAleatorio()
        elif opcion=="4":
            e=col.eliminar()
        elif opcion=="5":
            s=col.lista()
            print("datos Cola :",s)       
        elif opcion=="*":
            break
        else:
            print("opcion no valida")
            
menuPrinColaCir()
        
            
 