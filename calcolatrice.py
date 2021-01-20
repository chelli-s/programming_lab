class Calcolatrice:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def somma(self):
        try:
            float(self.a)
            float(self.b)
        except Exception as e:
            print('i valori inseriti non sono numeri: {}'.format(e))
        else:
            print('somma: {}'.format(self.a+self.b))

    def sottrazione(self):
        try:
            float(self.a)
            float(self.b)
        except Exception as e:
            print('i valori inseriti non sono numeri: {}'.format(e))
        else:
            if self.a>self.b:
                print('sottrazione: {}'.format(self.a-self.b))
            else:
                print('sottrazione: {}'.format(self.b-self.a))

    def moltiplicazione(self):
        try:
            float(self.a)
            float(self.b) 
        except Exception as e:
            print('i valori inseriti non sono numeri: {}'.format(e))
        else:
            print('moltiplicazione: {}'.format(self.a*self.b))

    def divisione(self):
        try:
            float(self.a)
            float(self.b)        
        except Exception as e:
            print('i valori inseriti non sono numeri: {}'.format(e))
        else:
            if self.b==0:
                raise Exception('NON E AMMESSA LA DIVISIONE PER 0')
            else:
                print('divisione: {}'.format(self.a/self.b))

    def potenza(self):
        try:
            isinstance(self.a,int) 
            isinstance(self.b,int)
        except Exception as e:
            print('i valori inseriti non sono numeri: {}'.format(e))
        else:
            print('potenza: {}'.fomat(pow(self.a,self.b)))

    def modulo(self):
        try:
            float(self.a)
        except Exception as e:
            print('i valori inseriti non sono numeri: {}'.format(e))
        else:
            print('modulo: {}'.format(abs(self.a)))

    def radice(self):
        try:
            isinstance(self.a,int) 
            isinstance(self.b,int)
        except Exception as e:
            print('i valori inseriti non sono numeri: {}'.format(e))
        else:
            if a>0 and b>0:
                print('radice:{}'.format(pow(self.a,(1/self.b))))

    def conversione(self):
        try:
            float(self.a)
            float(self.b)
        except Exception as e:
            print('i valori inseriti non sono numeri: {}'.format(e))
        else:
            if self.b==10:
                from math import log
                y=log(self.a, self.b)
                print('log in base dieci: {}'.format(y))
                y=log(self.a, 2)
                z=log(self.b, 2)
                print('log in base due: {}'.format(y/z))

            else:
                raise Exception('base non valida')

numero1=Calcolatrice(12,10)
numero2=Calcolatrice(3.2,4)

numero1.somma()
numero1.sottrazione()
numero1.moltiplicazione()
numero1.divisione()
numero1.modulo()
numero1.conversione()    
numero2.somma()
numero2.sottrazione()
numero2.moltiplicazione()
numero2.divisione()
numero2.modulo()
numero2.conversione()    
