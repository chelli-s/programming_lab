class Automobile:

    def __init__(self, casa_auto, modello, numero_posti, numero_portiere, kw, targa):
        self.casa_auto = casa_auto
        self.modello = modello
        self.numero_posti = numero_posti
        self.numero_portiere = numero_portiere
        self.kw = kw
        self.targa = targa

    def __str__(self):
        return 'automobile: {} {} {} {} {} {}'.format(self.casa_auto, self.modello, self.numero_posti, self.numero_portiere, self.kw, self.targa)

    def parla(self):
        print('broom broom')

    def confronta(self, a): #self e a corrispondono alle due macchine da confrontare
        if(self.casa_auto==a.casa_auto):
            print('stessa casa')
        else:
            print('case diverse')

        print('---------------------------')

        if(self.modello==a.modello):
            print('stesso modello')
        else:
            print('modelli diversi')

        print('---------------------------')

        if(self.numero_posti==a.numero_posti):
            print('stesso numero di posti')
        else:
            print('numero di posti diversi')

        print('---------------------------')

        if(self.numero_portiere==a.numero_portiere):
            print('stesso numero di portiere')
        else:
            print('numero di portiere diversi')

        print('---------------------------')

        if(self.kw==a.kw):
            print('stesso kw')
        else:
            print('kw diversi')

        print('---------------------------')

    def bollo(self, cat):
        if(cat=='Euro0'):
            if(self.kw<100):
                print('Euro0 con kw<100, bollo: ',self.kw*3)
            else:
                print('Euro0 con kw>100, bollo: ',self.kw*4.50)
        elif(cat=='Euro1'):
            if(self.kw<100):
                print('Euro1 con kw<100, bollo: ',self.kw*2.50)
            else:
                print('Euro1 con kw>100, bollo: ',self.kw*4.35)
        else:
            print('Euro2, bollo: ', self.kw*3)
            
         

automobile1 = Automobile(casa_auto='Fiat' , modello = '600' , numero_posti = 4 , numero_portiere = 3 , kw = 56 , targa = 'AB 456CD')

automobile2 = Automobile(casa_auto='Fiat' , modello = 'Panda' , numero_posti = 5 ,numero_portiere = 5 , kw = 69 , targa = 'CD 654AB')

automobile3 = Automobile(casa_auto='Audi' , modello = 'A1' , numero_posti = 5 , numero_portiere = 5 , kw = 90 , targa = 'FP 364UZ')

print(automobile1.__str__())
print(automobile2.__str__())
print(Automobile.confronta( automobile1 , automobile2))
print(automobile3.__str__())
print(automobile2.__str__())
print(Automobile.confronta( automobile3 , automobile2))
print(automobile1.bollo('Euro0'))