from NodoLC import Nodo

class ListaCircular:
    def __init__(self):
        self.L = None

    def adicionaFinal(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.L:
            self.L = nuevo_nodo
            self.L.siguiente = self.L
        else:
            actual = self.L
            while actual.siguiente != self.L:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.L

    def adicionaInicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.L:
            self.L = nuevo_nodo
            self.L.siguiente = self.L
        else:
            nuevo_nodo.siguiente = self.L
            actual = self.L
            while actual.siguiente != self.L:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            self.L = nuevo_nodo

    def mostrar(self):
        if not self.L:
            return
        r = self.L
        s = ""
        while True:
            s += " " + str(r.dato)
            r = r.siguiente
            if r == self.L:
                break
        print(s)
        
            # 1. Dada una lista circular simple, insertar un elemento X después de cada elemento par.
    # L= [2, 3, 4, 5], X = 10
    # L= [2, 10, 3, 4, 10, 5]
    
    def insertar_par(self,x):
        r = self.L
        while True:
            e = int(r.dato)
            if (e%2==0):
                nuevo_nodo = Nodo(x)
                nuevo_nodo.siguiente = r.siguiente
                r.siguiente = nuevo_nodo
                r = r.siguiente
            r = r.siguiente
            if r == self.L:
                break
              
              
# 2. Dada una lista circular simple, ordenar los elementos de la lista.
# L: [4, 1, 3, 2]
# L [1, 2, 3, 4]


    def ordenar(self):
        if not self.L or self.L.siguiente == self.L:
            return  # La lista está vacía o tiene un solo elemento, ya está ordenada

        # Paso 1: Convertir la lista circular en una lista lineal de elementos
        elementos = []
        actual = self.L
        while True:
            elementos.append(actual.dato)
            actual = actual.siguiente
            if actual == self.L:
                break

        # Paso 2: Ordenar la lista de elementos
        elementos.sort()

        # Paso 3: Reconstruir la lista circular con los elementos ordenados
        actual = self.L
        for dato in elementos:
            actual.dato = dato
            actual = actual.siguiente
            
            
            # 3. Dada una lista circular simple ordenada, insertar un elemento X en el lugar que le corresponde.
# L: [1, 3, 5, 7], X = 4
# L: [1, 3, 4, 5, 7]

    def insertar_ordenado(self,x):
        self.ordenar()
        nuevo_nodo = Nodo(x)
        if not self.L:
            self.L = nuevo_nodo
            self.L.siguiente = self.L
        else:
            actual = self.L
            while True:
                if actual.dato <= x and actual.siguiente.dato >= x:
                    nuevo_nodo.siguiente = actual.siguiente
                    actual.siguiente = nuevo_nodo
                    break
                actual = actual.siguiente
                if actual == self.L:
                    break
                  
#                   4. Dada una lista circular simple, separar en dos listas A y B, los elementos primos en A y el resto en la lista B.
# L: [2, 4, 5, 6, 7, 8]
# A = [2, 5, 7], B = [4, 6, 8]

    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
      

    def separar(self):
        if not self.L:
            return None, None

        A = ListaCircular()
        B = ListaCircular()
        actual = self.L
        while True:
            e = int(actual.dato)
            if self.es_primo(e):
                A.adicionaFinal(e)
            else:
                B.adicionaFinal(e)
            actual = actual.siguiente
            if actual == self.L:
                break

        return A, B
      
      
      # 5. Dada dos listas circulares simples, realizar la suma de sus elementos.
# A = [1, 2, 3],
# B = [4, 5, 6]
# C = [5, 7, 9]
    def suma(self, otra):
        if not self.L or not otra.L:
            return None

        C = ListaCircular()
        actual1 = self.L
        actual2 = otra.L
        while True:
            e1 = int(actual1.dato)
            e2 = int(actual2.dato)
            C.adicionaFinal(e1 + e2)
            actual1 = actual1.siguiente
            actual2 = actual2.siguiente
            if actual1 == self.L or actual2 == otra.L:
                break

        return C
      
#       6. Dada una lista circular simple, calcular la media aritmética.
# L: [2, 4, 6, 8]
# M: 5.0
    def media(self):
        if not self.L:
            return None

        suma = 0
        contador = 0
        actual = self.L
        while True:
            suma += int(actual.dato)
            contador += 1
            actual = actual.siguiente
            if actual == self.L:
                break

        return suma / contador


# 7. Dada una lista circular simple, obtener el tamaño de la lista.
# L: [10, 20, 30]
# Tam: 3

    def tamano(self):
        if not self.L:
            return 0

        contador = 0
        actual = self.L
        while True:
            contador += 1
            actual = actual.siguiente
            if actual == self.L:
                break

        return contador

# 8. Dada una lista circular simple, intercambiar el elemento mayor con el menor.
# L=[3, 1, 4, 2]
# L=[4, 1, 3, 2]

    def intercambiar(self):
        if not self.L:
            return

        # Encontrar el elemento mayor y el menor
        mayor = self.L
        menor = self.L
        actual = self.L
        while True:
            if int(actual.dato) > int(mayor.dato):
                mayor = actual
            if int(actual.dato) < int(menor.dato):
                menor = actual
            actual = actual.siguiente
            if actual == self.L:
                break

        # Intercambiar los datos del mayor y el menor
        mayor.dato, menor.dato = menor.dato, mayor.dato

# 9. Dada una lista circular simple, eliminar los elementos repetidos de la lista.
# L= [1, 2, 2, 3, 4, 4, 5]
# L [1, 2, 3, 4, 5]
    def eliminar_repetidos(self):
        if not self.L:
            return

        actual = self.L
        while True:
            if actual.siguiente.dato == actual.dato:
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente
            if actual == self.L:
                break

# 10. En una lista circular generar la siguiente serie: s = 4, 7, 10, 13, 16, 19, …
# L: [4, 7, 10, 13, 16, 19]              
    def serie(self, n):
      aux = 4
      for i in range(n):
        self.adicionaFinal(aux)
        aux += 3
        
        
#         11. Invertir Cada Cadena en una Lista
# L=['hola', 'mundo', 'python']
# L=['aloh', 'odnum', 'nohtyp']
    def invertir_cadena(self):
        if not self.L:
            return

        actual = self.L
        while True:
          invertida = ""
          for char in actual.dato:
            invertida = char + invertida
          actual.dato = invertida
          actual = actual.siguiente
          if actual == self.L:
            break

# 12. Eliminar Cadenas que Contengan un Substring Específico
# L: ['apple', 'banana', 'cherry', 'mundo']
# subcadena = 'an'
# L: ['apple', 'cherry', 'date',’mundo’]

    def eliminar_subcadena(self, subcadena):
        if not self.L:
            return

        actual = self.L
        while True:
            if subcadena in actual.dato:
                actual.dato = actual.siguiente.dato
            else:
                actual = actual.siguiente
            if actual == self.L:
                break



# Ejemplo de uso:
def main():
    lc = ListaCircular()
    lc.adicionaInicio(1)
    lc.adicionaInicio(2)
    lc.adicionaInicio(6)
    lc.adicionaInicio(6)
    lc.adicionaInicio(4)
    
    lc2 = ListaCircular()
    lc2.adicionaInicio(2)
    lc2.adicionaInicio(1)
    lc2.adicionaInicio(5)
    lc2.adicionaInicio(4)
    # lc.mostrar()
    # lc.eliminar_repetidos()
    # lc.mostrar()
    lc3 = ListaCircular()
    lc3.serie(6)
    # lc3.mostrar()
    
    lc4 = ListaCircular()
    lc4.adicionaInicio('hola')
    lc4.adicionaInicio('mundo')
    lc4.adicionaInicio('python')
    lc4.adicionaInicio('banana')
    lc4.mostrar()
    lc4.eliminar_subcadena('on')
    lc4.mostrar()

main()
