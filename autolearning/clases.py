class Personaje:

    #metodo/s para asignar atributos
    def __init__(self, nombre, fuerza, velocidad, vida, defensa): #El método es como una funcion
        self.nombre = nombre # Acá asigno a la clase Personaje el nombre que recibo, o sea, LOS ATRIBUTOS
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.vida = vida
        self.defensa = defensa

    def atributos(self):
        print(self.nombre)
        print(self.fuerza)
        print(self.velocidad)
        print(self.vida)
        print(self.defensa)

    def subir_nivel(self, fuerza, velocidad, defensa):
        self.fuerza += fuerza
        self.velocidad += velocidad
        self.defensa += defensa

    def damage(self, enemigo):
        enemigo.vida -= jugador.fuerza

    # def atacar(self, enemigo):
    #     damage = self.damage(enemigo)
    #     enemigo.vida -= enemigo.damage

jugador = Personaje("Pedro", 10, 40, 100, 20)
enemy = Personaje("Fantasma", 1, 4, 100, 2)

#print(jugador.nombre)
jugador.atributos()
jugador.subir_nivel(5, 2, 3)
enemy.atributos()

jugador.damage(enemy)

enemy.atributos()



