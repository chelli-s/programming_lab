class ExamException(Exception):

        pass

class MovingAverage:
    def __init__(self,window):
        self.window = window

    def compute(self, lista):
        if len(lista)==0:
            raise ExamException('Errore, lista valori vuota')
        if isinstance(lista,str):
            raise ExamException('Errore, lista di stringhe')          
        if lista==None:
            raise ExamException('Errore, lista valori vuota')
    
        output = []
        i=0
        
        while(i<=len(lista)-self.window):
            j=i
            valore=0
            while(j<i+self.window):
                
                valore+=lista[j]
                j=j+1
            media=valore/self.window
            output.append(media)
            i=i+1
        return output

moving_average = MovingAverage(3)
result = moving_average.compute([6, 12, 24, 48, 96])
print(result)
