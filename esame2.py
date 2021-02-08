class ExamException(Exception):

        pass

class Diff:
    
    def __init__(self,ratio=1):

        if ratio==None:
            raise ExamException('None non è supportato')
        
        if isinstance(ratio,str):
            raise ExamException('Sono supportati solo numeri')

        if ratio<0:
            raise ExamException('Ratio deve essere positivo')
        
        if ratio==0:
            raise ExamException('0 non e un valore supportato')
        
        self.ratio=ratio
        

    
    def compute(self,lista):
        if not isinstance(lista,list):
            raise ExamException('Non e una lista')
        if len(lista)<2:
            raise ExamException('La lunghezza della lista deve essere almeno 2')
        output = []
        i=0     
        while(i<len(lista)-1):
            if not (isinstance(lista[i], int) or  isinstance(lista[i], float)):
                raise ExamException('Il valore inserito non e un numero')

            if not (isinstance(lista[i+1], int) or  isinstance(lista[i+1], float)):
                raise ExamException('Il valore inserito non e un numero')

            if lista[i]>lista[i+1]:
                raise ExamException('la differenza e negativa')
            valore=lista[i+1]-lista[i]
            media=valore/self.ratio
            output.append(media)
            i=i+1
        return output

diff = Diff()
result = diff.compute([2,4,8,16])
print(result) # Deve stampare a schermo [2,4,8]