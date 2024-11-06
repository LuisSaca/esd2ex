from NodoL import Nodo
class ListaSimpleCircular(object):
    #Inicializamos la lista
    def __init__(self):
        self.L = None
    #Adicionamos un elemento e al inicio de la Lista
    def adicionaInicio(self, e):
        q = Nodo()
        q.dato=e
        if self.L==None:
            q.sigte = q
            self.L=q
        else:
            r=self.L
            while r.sigte!=self.L:
                r=r.sigte
            q.sigte=self.L
            r.sigte=q
            self.L=q
    #adiciona fina´l
    def adicionaFinal(self,e):
        q=Nodo()
        q.dato=e
        if self.L==None:
            q.sigte=q
            self.L=q
        else:
            r=self.L
            while r.sigte!=self.L:
                r=r.sigte
            r.sigte = q
            q.sigte = self.L
    #adiciona Antes de
    def adicionaAntes(self,e,x):
        if self.L!=None:
            r=self.L
            w=self.L
            while r.dato!=x and r.sigte!=self.L :
                w=r
                r=r.sigte
            if r==self.L and r.dato==x:
                self.adicionaInicio(e)
            else:
                if r.dato==x:
                    q=Nodo()
                    q.dato=e
                    q.sigte=r
                    w.sigte=q
     # adiciona despues
     
    def adicionaDespues(self,e,x):
        if self.L!=None:
            r=self.L
            while r.dato!=x and r.sigte!=self.L :
                 r=r.sigte
            if r.sigte ==self.L and r.dato==x:
                self.adicionaFinal(e)
            else:
                if r.dato==x:
                   q=Nodo()
                   q.dato=e
                   q.sigte = r.sigte
                   r.sigte = q
      #elimina inicio
    def eliminaInicio(self):
        if self.L!=None:
            if self.L.sigte==self.L:
                self.L=None
            else:
                r=self.L
                while r.sigte!=self.L:
                    r=r.sigte
                self.L = self.L.sigte
                r.sigte = self.L
                
      #elimina inicio
    def eliminaFinal(self):
        if self.L!=None:
            if self.L.sigte==self.L:
                self.L=None
            else:
                r=self.L
                w=self.L
                while r.sigte!=self.L:
                    w=r
                    r=r.sigte
                w.sigte=self.L    
      #elimina X
    def eliminaX(self,x):
          if self.L!=None:
              if self.L.sigte==self.L:
                  self.L=None
              else:
                  r=self.L
                  w=r
                  while r.dato!=x and r.sigte!=self.L:
                      w=r
                      r=r.sigte
                  if r==self.L and r.dato==x:
                      self.eliminaInicio()
                  else:
                      if r.sigte==self.L and r.dato==x:
                         self.eliminaFinal()
                      else:
                         w.sigte = r.sigte
      
    # Listamos datos de la Lista
    def mostrar(self):
        r = self.L
        s = ""
        print("Datos de la Lista")
        while r.sigte !=self.L:
            s = s + "  " + str(r.dato)
            r = r.sigte
        s = s + "  " + str(r.dato)    
        return s
       
    
lista=ListaSimpleCircular()
lista.adicionaInicio(1)
lista.adicionaInicio(4)
lista.adicionaInicio(1)
lista.adicionaInicio(7)
lista.adicionaInicio(9)
s=lista.mostrar()
print(s)
lista.adicionaFinal(1)
lista.adicionaFinal(4)
lista.adicionaFinal(7)
lista.adicionaFinal(10)
s=lista.mostrar()
print(s)
lista.eliminaInicio()
lista.eliminaInicio()
s=lista.mostrar()
print(s)
lista.eliminaFinal()
s=lista.mostrar()
print(s)
x=int(input("elemento a eliminar:"))
lista.eliminaX(x)
s=lista.mostrar()
print(s)

