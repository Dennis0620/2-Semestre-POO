class personajes: #Creamos la clase donde contendra los datos de los personajes
    def __init__(self,nombre,habilidad,fuerza,IQ,vida,defensa): #Definimos las caracteristicas que tendras nuestros personajes
        self.nombre=nombre
        self.habilidad=habilidad
        self.fuerza=fuerza
        self.IQ=IQ
        self.vida=vida
        self.defensa=defensa
    def mostraratributos(self): #aqui definimos para que los atributos de nuestros personajes se muestren
        print(self.nombre, ":", sep="")
        print("Habilidad: ", self.habilidad)
        print("Fuerza: ", self.fuerza)
        print("IQ: ", self.IQ)
        print("Vida: ", self.vida)
        print("Defensa: ", self.defensa)
    def atacar(self,enemigo): # aqui definimos con una condicional para lograr hacer daño a un enemigo
        daño = self.fuerza - self.defensa
        if daño > 0:
            enemigo.vida -= daño
            print(f"{self.nombre} ha atacado a {enemigo.nombre} causando {self.daño}")
        else:
            print(f"{self.nombre} no ha causado daño a {enemigo.nombre} debido a su defensa")
    def esta_vivo(self):
        return self.vida > 0

class duelista(personajes): # aqui creamos un personaje duelista con sus habilidades propias y armas
    def __init__(self,nombre,habilidad,fuerza,IQ,vida,defensa, arma):
        super().__init__(nombre, habilidad, fuerza, IQ, vida, defensa)
        self.arma = arma
    def mostraratributos(self):
        super().mostraratributos()
        print(f" Arma: {self.arma}")
    def atacar(self,enemigo):
        daño = self.fuerza +10 - enemigo.defensa
        if daño > 0:
            enemigo.vida -= daño
            print(f"{self.nombre} ha atacado a {enemigo.nombre} causando {self,daño} de daño")
class apoyo(personajes):
    def __init__(self,nombre,habilidad,fuerza,IQ,vida,defensa, arma):
        super().__init__(nombre, habilidad, fuerza, IQ, vida, defensa)
        self.arma = arma
    def mostraratributos(self):
        super().mostraratributos()
        print(f"Arma: {self.arma}")
    def atacar(self,enemigo):
        daño = self.fuerza +8 - enemigo.defensa
        if daño > 0:
            enemigo.vida -= daño
            print(f"{self.nombre} ha atacado a {enemigo.nombre} causando {self.daño} de daño")

#aqui colocamos la informacion de los atributos de los personajes
Rush = duelista("Kratos", "Cegar enemigos", 50, 35, 250, 150, "Subfusil")
Curas = apoyo("Lily", "Curar al equipo", 25,60,250, 140,"fusil de asalto")
#aqui se muestran los atributos
Curas.mostraratributos()
Rush.mostraratributos()

Rush.atacar(Curas)
Curas.atacar(Rush)
#aqui para definir si despues de cada ataque siguen vivos o no
if Rush.esta_vivo():
    print(f"{Rush.nombre} sigue vivo")
else:
    print(f"{Rush.nombre} esta muerto")

if Curas.esta_vivo():
    print(f"{Curas.nombre} sigue vivo")
else:
    print(f"{Curas.nombre} esta muerto")