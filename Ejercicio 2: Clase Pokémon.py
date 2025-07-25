class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.__nivel = 1
        self.__salud = 100

    def atacar(self, objetivo, dano):
        if dano <= 0:
            print("El daño debe ser positivo.")
            return
        if self.__salud <= 0:
            print(f"{self.nombre} no tiene salud para atacar.")
            return

        print(f"{self.nombre} ({self.tipo}) ataca a {objetivo.nombre} con {dano} de daño.")
        objetivo.recibir_dano(dano)

    def recibir_dano(self, dano):
        if dano < 0:
            print("El daño recibido no puede ser negativo.")
            return

        self.__salud -= dano
        if self.__salud < 0:
            self.__salud = 0
        print(f"{self.nombre} recibe {dano} de daño. Salud actual: {self.__salud}")
        if self.__salud == 0:
            print(f"{self.nombre} ha sido debilitado.")

    def subir_nivel(self):
        self.__nivel += 1
        print(f"{self.nombre} subió a Nivel {self.__nivel}!")

    def estado(self):
        print(f"\n--- Estado de {self.nombre} ---")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.__nivel}")
        print(f"Salud: {self.__salud}/100")
        print("------------------------------")


class PokemonLegendario(Pokemon):
    def __init__(self, nombre, tipo, habilidad_especial):
        super().__init__(nombre, tipo)
        self.__habilidad_especial = habilidad_especial

    def atacar(self, objetivo, dano):
        dano_total = dano
        if self._Pokemon__nivel > 50:
            dano_adicional = 20
            dano_total += dano_adicional
            print(f"¡Habilidad de Leyenda! {self.nombre} añade {dano_adicional} de daño adicional.")
        
        
        super().atacar(objetivo, dano_total)

    def usar_habilidad(self):
        print(f"{self.nombre} usa su habilidad especial: ¡{self.__habilidad_especial}!")
        print("🤖✨ Un efecto épico sacude el campo de batalla.")


print("\n--- Ejercicio 2: Clase Pokémon ---")
pikachu = Pokemon("Pikachu", "Eléctrico")
charmander = Pokemon("Charmander", "Fuego")

pikachu.estado()
charmander.estado()

pikachu.atacar(charmander, 30)
charmander.estado()

charmander.recibir_dano(50) 
charmander.estado()


for _ in range(55):
    pikachu.subir_nivel()
pikachu.estado()


print("\n--- Pruebas de Pokémon Legendario ---")
mewtwo = PokemonLegendario("Mewtwo", "Psíquico", "Rayo Confusión")
groudon = PokemonLegendario("Groudon", "Tierra", "Filo del Abismo")

mewtwo.estado()
groudon.estado()

mewtwo.atacar(groudon, 40) 
groudon.estado()

mewtwo.subir_nivel() 
mewtwo.subir_nivel()
mewtwo.subir_nivel() 
for _ in range(48):
    mewtwo.subir_nivel()
mewtwo.estado()

mewtwo.atacar(groudon, 40) 

mewtwo.usar_habilidad()
