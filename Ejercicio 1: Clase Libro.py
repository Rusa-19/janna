class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.__numero_paginas = self._validar_paginas(numero_paginas)
        self.__prestado = False
        self.__cantidad_prestamos = 0  

    def _validar_paginas(self, paginas):
        if paginas < 10:
            print(f"🚨 Advertencia: El número de páginas para '{self.titulo}' es muy bajo. Ajustado a 10.")
            return 10
        return paginas

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            self.__cantidad_prestamos += 1 
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya ha sido prestado.")

    def devolver(self):
        if self.__prestado:
            self.__prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

    def mostrar_detalles(self):
        estado_prestamo = "Sí" if self.__prestado else "No"
        print(f"\n--- Detalles del Libro: '{self.titulo}' ---")
        print(f"Autor: {self.autor}")
        print(f"Número de Páginas: {self.__numero_paginas}")
        print(f"¿Está Prestado?: {estado_prestamo}")
        print(f"Cantidad de veces prestado: {self.__cantidad_prestamos}")  
        print("------------------------------------------")


print("--- Ejercicio 1: Clase Libro ---")
libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", 1200)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 5) 
libro3 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 496)

libro1.mostrar_detalles()
libro2.mostrar_detalles()
libro3.mostrar_detalles()

libro1.prestar()
libro1.prestar() 
libro1.mostrar_detalles()

libro1.devolver()
libro1.devolver() 
libro1.mostrar_detalles()

libro3.prestar()
libro3.prestar()
libro3.devolver()
libro3.prestar()
libro3.mostrar_detalles() 
