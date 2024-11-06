import os
import random
from math import sqrt
from NodoL import Nodo
class ListaSimple(object):
    #Inicializamos la lista
    def __init__(self):
        self.L = None
    #Adicionamos un elemento e al inicio de la Lista
    def adicionaInicio(self, e):
        q = Nodo()
        q.dato=e
        q.sigte = self.L 
        self.L = q
    #Adicionamos un elemento e al final de la Lista
    def adicionaFinal(self, e):
        q = Nodo()
        q.dato=e
        if self.L is None:
            self.L = q
        else:
            r = self.L
            while r.sigte!=None:
                r = r.sigte
            r.sigte = q
    # Adiciona un elemento e antes del elemento x 
    def adicionaAntes(self, e, a):
        if self.L != None:
            r = self.L
            w = None
            while r != None and r.dato != a:
                w = r
                r = r.sigte
            if r!=None:
                if r == self.L:
                    self.adicionaInicio(e)
                else:
                    q = Nodo()
                    q.dato=e
                    q.sigte = r
                    w.sigte = q
            else:
                print("No se encontro elemento...")
        else:
            print("Lista Vacia...")

    # Adiciona un elemento e despues del elemento d 
    def adicionaDespues(self, e, d):
        if self.L!=None:
            r = self.L
            while r != None and r.dato != d:
                r = r.sigte
            if r != None:
                if r.sigte == None:
                    self.adicionaFinal(e)
                else:
                    q = Nodo()
                    q.dato=e
                    q.sigte = r.sigte
                    r.sigte = q
            else:
                print("No se encontró el elemento en la lista...")
        else:
            print("Lista vacía...")
    
    # En una Lista llenar n datos
    # de forma aleatoria 
    
    def adicionaAleatorio(self):
        n=int(input("Cantidad de datos a generar:"))
        for i in range(1,n+1):
            e=random.randint(1,20)
            self.adicionaFinal(e)
    
    # Elimina un elemento de la lista del principio               
    def eliminaInicio(self):
        if self.L==None:
            print("Lista vacía")
        else:
            print("Elemento eliminado:", self.L.dato)
            self.L = self.L.sigte
    #Elimina un elemento de la lista del final        
    def eliminaFinal(self):
        if self.L==None:
            print("Lista vacía")
        else:
            r = self.L
            w = None
            while r.sigte!=None:
                w = r
                r = r.sigte
            print("Elemento eliminado:", r.dato)
            w.sigte = None
    def eliminaX(self,x):
        if self.L!=None:
            r=self.L
            w=r
            while r.dato!=x and r!=None:
                w=r
                r=r.sigte
            if self.L==r and r.dato==x:
                self.eliminaInicio()
            else:
                if r.sigte==None and r.dato==x:
                   self.eliminaFinal()
                else:
                    w.sigte=r.sigte
                    r=None
    # Listamos datos de la Lista
    def mostrar(self):
        r = self.L
        s = ""
        print("Datos de la Lista")
        while r != None:
            s = s + "  " + str(r.dato)
            r = r.sigte
        return s

#programa principal

lista=ListaSimple()
lista.adicionaInicio(5)
lista.adicionaInicio(4)
lista.adicionaInicio(2)

s=lista.mostrar()
print(s)

lista.adicionaFinal(5)
lista.adicionaFinal(4)
lista.adicionaFinal(1)
lista.adicionaFinal(1)
lista.adicionaFinal(4)
s=lista.mostrar()
print(s)
lista.eliminaX(1)
s=lista.mostrar()
print(s)
