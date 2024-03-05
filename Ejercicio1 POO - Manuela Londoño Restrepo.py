
#Ejercicio de sistema de gestión o reserva de vuelos

#Defino la clase pasajero

class Pasajero:
    #No tengo atributos de clase

    #Defino los atributos de instancia dentro del init
    #Son privados
    def __init__(self, nombre, apellido, edad, numeroPasaporte):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.numeroPasaporte = numeroPasaporte
    
    #Defino los métodos de la clase pasajero
    #Este método será de instancia entonces se le debe poner el self para que pueda tomar
    #toda la información del pasajero
    def mostrarInformacion(self):
        print(f"\nEl pasajero es {self.nombre} {self.apellido} ")
        print(f"El pasajero tiene {self.edad} años de edad")
        print(f"Su número de pasaporte es {self.numeroPasaporte} ")

#Ahora, fuera de la clase, instancio los objetos
pasajero1  = Pasajero("Manuela", "Londoño", 18, "1234567890")

#Así puedo mostrar solo el valor de uno de los atributos del pasajero1
print(pasajero1.nombre)

#Ahora aplico el método de mostrarInformacion 
pasajero1.mostrarInformacion()

#Creo la clase Vuelo
class Vuelo:
    #Defino el init
    def __init__(self, numeroVuelo, origen, destino, capacidadTotal):
        self.numeroVuelo = numeroVuelo #Es el nombre despues del igual el que debe coincidir con algun parámetro dentro 
        #del paréntesis del init
        self.origen = origen
        self.destino = destino
        self.capacidadTotal = capacidadTotal
        self.asientosDisponibles = capacidadTotal #Aquí lo inicializo como un contador y luego le voy restando con cada reserva
        self.reservas = [] #Inicializo una lista de reservas para almacenar las reservas
        #reseervas es un atributo de instancia para que solo cuente las reservas pertenecientes a un vuelo como objeto
        #Si fuera de clase, contaría las reservas de todos los vuelos
        #Aquí se va a ir metiendo cada pasajero completo con su info

        #Aquí debo poner la dependencia con reserva vuelo apenas cree esa clase
        reservaVuelos.adicionVuelo(self)
    
    #Defino los métodos de la clase vuelo
    #Método de instancia ---> (self)
    def mostrarInformacion(self):
        print(f"\nEl vuelo número {self.numeroVuelo} saldrá desde {self.origen} y llegará a {self.destino}")
        print(f"El vuelo tiene un total de {self.capacidadTotal} asientos y, de ellos, {self.asientosDisponibles} se encuentran disponibles")

    #Al siguiente método el vuelo se lo dará el self, pero el pasajero lo debo pasar como parámentro
    #Esto indica la primera relación de asociación
    def reservarAsiento(self, pasajero):
        if pasajero in self.reservas:
            print(f'El pasajero {pasajero.nombre} {pasajero.apellido} ya tiene una reseva en este vuelo')
        elif self.asientosDisponibles > 0:
            self.reservas.append(pasajero)
            self.asientosDisponibles = self.asientosDisponibles - 1
            print(f'{pasajero.nombre} {pasajero.apellido} realizó una reserva')
        else:
            print('No hay asientos disponibles en este vuelo')
    
    #Relacion de asociación
    def removerAsiento(self, pasajero):
        if pasajero in self.reservas:
            self.reservas.remove(pasajero)
            self.asientosDisponibles = self.asientosDisponibles + 1
            print(f'El pasajero {pasajero.nombre} {pasajero.apellido} ha cancelado su reserva')
        else:
            print(f'El pasajero {pasajero.nombre} {pasajero.apellido} no tiene reservas, no es posible hacer una cancelación')



vuelo1 = Vuelo('MLR1832', 'Medellín', 'Miami', 60)

vuelo1.mostrarInformacion()
vuelo1.reservarAsiento(pasajero1)
vuelo1.mostrarInformacion()
vuelo1.removerAsiento(pasajero1)
vuelo1.mostrarInformacion()

class reservaVuelos:
    #Atributo de clase
    vuelos = []
    def __init__(self, aerolínea):
        self.aerolínea = aerolínea
    
    #Método de clase
    @classmethod
    def adicionVuelo(cls,vuelo):
        if vuelo in cls.vuelos:
            print(f'El vuelo {vuelo.numeroVuelo}')


