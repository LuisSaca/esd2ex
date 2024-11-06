from ListasSimples import ListaSimple

def menuPrincipalLista():
    lista=ListaSimple()
    while True:
        print("\nMenu")
        print("1. Crear")
        print("2. Adicionar Inicio")
        print("3. Adiciona Final")
        print("4. Adiciona Antes de")
        print("5. Adiciona Despues de")
        print("6. Adiciona de forma ordenada")
        print("7. Elimina inicio")
        print("8. Elimina Final")
        print("9. Elimina Elemento X")
        print("10. Listar")
        print("*   Salir")
        opcion=input("Elija Opcion: ")
        if opcion=="1":
           lista=ListaSimple() 
        elif opcion=="2":
            e=int(input("Ingrese dato: "))
            lista.adicionaInicio(e)
        elif opcion=="3":
            e=int(input("Ingrese dato: "))
            lista.adicionaFinal(e)
        elif opcion=="4":
            e=int(input("Ingrese dato: "))
            a=int(input("Adicionar antes de:"))
            lista.adicionaAntes(e,a)
        elif opcion=="5":
            e=int(input("Ingrese dato: "))
            d=int(input("Adicionar despues de: "))
            lista.adicionaDespues(e,d)
        elif opcion=="6":
            e=int(input("Ingrese dato: "))
            lista.adicionaOrdenada(e)
        elif opcion=="7":
            lista.eliminaInicio()
        elif opcion=="8":
            lista.eliminaFinal()
        elif opcion=="9":
            x=int(input("elemento a eliminar"))
            lista.eliminaElementoX(x)
        elif opcion=="10":
            print(lista.mostrar())

        elif opcion=="*":
            break
        else:
            print("opcion no valida")

menuPrincipalLista()