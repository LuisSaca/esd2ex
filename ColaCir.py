import random
class ColaCircular (object):
    #Cosntructor para crear la cola circular
    def __init__(self, n):
        self.MAX = n
        self.C = [None] * n
        self.prin = 0
        self.fin = 0
    #verifica si una cola esta vacia
    def vacio(self):
        if self.prin == self.fin:
            return True
        else:
            return False;
    #verifica si una cola esta llena

    def lleno(self):
        if ((self.fin+1)% self.MAX == self.prin):
            return True
        else:
            return False
       
    #Adiciona un elemento en la cola
    def adicionar(self, e):
        if not self.lleno():
            self.C[self.fin] = e
            self.fin = (self.fin + 1) % self.MAX
        else:
            print("La cola está llena")
    
    # En una cola C llenar n datos
    # de forma aleatoria en la cola    
    def adicionaAleatorio(self):
        n=int(input("Cantidad de datos a generar: "))
        for i in range(1,n+1):
            e=random.randint(1,20)
            self.adicionar(e)
            
    #Elimina un elemento de la cola
    def eliminar(self):
        e=-1
        if not self.vacio():
            e = self.C[self.prin]
            self.C[self.prin] = None
            self.prin = (self.prin + 1) % self.MAX
        else:
            print("La cola está vacía")
        return e
    
    #lista los datos de cola
    def lista(self):
        s = "";
        aux = self.fin
        while (aux!=self.prin):
            e = self.eliminar()
            self.adicionar(e)
            s = s + " " + str(e)
        return s
   

    
   

   


                    


   



