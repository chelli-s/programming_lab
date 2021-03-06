class ExamException(Exception):

    pass

class CSVTimeSeriesFile:

    def __init__(self, name):

        self.name = name

    def get_data(self):

        j = 0
        output = []
        
        try:
            my_file = open(self.name, 'r') #apro il file con il nome scelto dall'utente 
        except:
            raise ExamException('imposibile aprire il file')
            

        for line in my_file:
            
            elements = line.split(',') #per ogni linea nell mio file vado a splittare in 2 elementi quando incontro la virgola
            if len(elements) >= 2:

                if elements[0] != 'epoch':
                        
                    timestamp  = elements[0] #salvo le timestamp in una variabile
                    value = elements[1] #le temperature nell'altra
                    
                    try:
                        timestamp = float(timestamp)
                        timestamp = int(timestamp)
                    except:
                        timestamp = j
                        j+=1           

                    if timestamp<0:
                        raise ExamException('valore negativo non accettato')
                    
                    try:
                        value = float(value) #e le temperature in float
                    except:
                        timestamp = j
                        j+=1
                        
                    values = [timestamp,value] #salvo le variabili in un vettore
                    
                    
                    output.append(values) #salvo questo vettore in un altro vettore in modo da creare un array annidato
            else:
                print('\nin questa linea mancano elementi\n')
                
        for i in range(1, len(output)):
            if output[i-1][0]>=output[i][0]:
                raise ExamException('Le date sono ordinate, è stato rivelato un errore di ordine')

        my_file.close()
        return output #ritorno il vettore finale
        

def daily_stats(self):

    if not isinstance(self,list):
        raise ExamException('L elemento inserito non è una lista')

    values = [] #values è il vettore in cui salvo i valori giornalieri
    output = [] #output serve per salvare le statistiche giornaliere
        
    for i in range(0,len(self)):
        
        epoch = self[i][0] #salvo in una variabile 
        day_start_epoch = epoch - (epoch % 86400) #salvo in una variabile  l’inizio di un giorno dato un timestamp epoch
        data = [] #inizializzo il vettore data, qui salvo tutte le temperature appartenenti allo stesso giorno
       # if i==0:
           # data.append(self[i][1])
        if epoch != 0:
            for j in range(i,len(self)):
                    timestamp = self[j][0]
                    condizione = day_start_epoch + 86400
                    if timestamp < condizione : #se siamo nello stesso giorno
                        data.append(self[j][1]) #aggiungo all'array data
                        self[j][0] = 0 #e assegno il valore 0 alla data
                
            values.append(data)
    
    for i in range(0,len(values)):
        somma = 0
        valore_massimo = values[i][0]
        valore_minimo = values[i][0]
        if len(values[i])<1:#controllo che ci sia almeno un valore per giorno
            raise ExamException('Ogni giorno ha almeno un dato')
        for j in range(0, len(values[i])):#valuto la giornata corrente
            somma += values[i][j]
            if valore_massimo<values[i][j]:
                valore_massimo = values[i][j]
            if valore_minimo>values[i][j]:
                valore_minimo = values[i][j]
        valore_medio = somma/len(values[i])#per fare la media approssimata a due cifre : round(somma/len(values[i]),2)
        statistiche = [valore_minimo,valore_massimo,valore_medio]
        output.append(statistiche)

    return  output

time_series_file = CSVTimeSeriesFile(name='dati2.csv')


time_series = time_series_file.get_data()
#print(time_series)
print(daily_stats(time_series))