class ExamException(Exception):

        pass

class MovingAverage:
    def __init__(self,window):

        if not isinstance(window,int):
            raise ExamException('non-integer value is not supported')

        

        if window<1:
            raise ExamException('La dimensione di window deve essere almeno 2')
        self.window = window

    def compute(self, lista):
        if lista==None:
            raise ExamException('Errore, lista valori vuota')
    
        if not isinstance(lista,list):
            raise ExamException('Errore, non e una lista') 

        if len(lista)<self.window:
            raise ExamException('La lunghezza della lista è minore della finestra')

                 
        
        output = []
        i=0
        
        while(i<=len(lista)-self.window):
            if not isinstance(lista[i],int):
                raise ExamException('Errore, lista di stringhe') 
            j=i
            valore=0
            while(j<i+self.window):
                if not isinstance(lista[j],int):
                    raise ExamException('Errore, lista di stringhe') 
                valore+=lista[j]
                j=j+1
            media=valore/self.window
            output.append(media)
            i=i+1
        return output

moving_average = MovingAverage(3)
result = moving_average.compute([6, 12, 24, 48, 96])
print(result)
