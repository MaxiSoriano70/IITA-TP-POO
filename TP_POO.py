class Gato:
    def __init__(self, nombre, color_pelo, color_ojos):
        self.nombre = nombre
        self.color_pelo = color_pelo
        self.color_ojos = color_ojos
        self.cansancio = 0
        self.hambre = 0

    def comer(self):
        self.hambre = 0
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        self.cansancio = 0
        print(f"{self.nombre} está durmiendo.")

    def jugar(self):
        self.cansancio += 1
        self.hambre += 1
        print(f"{self.nombre} está jugando.")

    def acariciar(self):
        print(f"{self.nombre} está siendo acariciado.")

gato1 = Gato("Ñoqui", "blanco", "azules")
gato2 = Gato("Michi", "blanco y negro", "verde")
gato3 = Gato("Cloe", "dorado", "grises")

gato1.comer()
gato2.jugar()
gato3.dormir()