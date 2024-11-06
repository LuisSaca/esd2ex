from ListasCircular import ListaCircular

def menuPrincipalListaC():
    lista=ListaCircular()
    while True:
        print("\nMenu")
        print("1. Crear")
        print("2. Adicionar Inicio")
        print("3. Adiciona Final")
        print("4. Elimina inicio")
        print("5. Elimina Final")
        print("6. Contar elementos")
        print("7. Listar")
        print("8. Suma pares")
        print("9. Suma primos")
        print("*   Salir")
        opcion=input("Elija Opcion: ")
        if opcion=="1":
           lista=ListaCircular()
            
        elif opcion=="2":
            e=int(input("Ingrese dato: "))
            lista.adicionaInicio(e)
        elif opcion=="3":
            e=int(input("Ingrese dato: "))
            lista.adicionaFinal(e)
        elif opcion=="4":
            lista.eliminaInicio()
        elif opcion=="5":
            lista.eliminaFinal()
        elif opcion=="6":
            print("La lista tiene",lista.contar_elementos(), "elementos")
        elif opcion=="7":
            lista.mostrar()
        elif opcion=="8":
            lista.suma_pares()
        elif opcion=="9":
            lista.suma_primos()
        elif opcion=="*":
            break
        else:
            print("opcion no valida")

menuPrincipalListaC()
