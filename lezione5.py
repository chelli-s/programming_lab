
class Pagina:
    
    
    def __init__(self, numero, capitolo, testo):

        self.numero = numero
        self.capitolo = capitolo
        self.testo = testo

pagina1 = Pagina(numero=1, capitolo='primo capitolo', testo = 'bbbb')

pagina2 = Pagina(numero=1, capitolo='primo capitolo', testo = 'AO')

print(pagina1.testo)
print(pagina2.testo)

class PaginaDestra(Pagina):
    
    def posizione_numero(self):
        return 'destra'

class PaginaSinistra(Pagina):

    def posizione_numero(self):
        return 'sinistra'

libro = []

pagina1 = PaginaSinistra(numero=343, capitolo='unidicesimo capitolo', testo='fine')

libro.append(pagina1)

pagina2 = PaginaDestra(numero=343, capitolo='unidicesimo capitolo', testo='fine')

libro.append(pagina2)

try:
    print(pagina1.testo)
    print(pagina1.posizione_numero())
    print(pagina2.testo)
    print(pagina2.posizione_numero())
    print(libro)
except:
    print('impossibile stampare')