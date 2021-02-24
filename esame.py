class ExamException(Exception):

    pass

class CSVTimeSeriesFile:

    def __init__(self, name):

        self.name = name

    def get_data(self):


        output = []
        
        try:
            my_file = open(self.name, 'r') #apro il file con il nome scelto dall'utente 
        except:
            raise ExamException('impossibile aprire il file')
            
        if my_file == None:
            raise ExamException('file vuoto')
        for line in my_file:
            
            error = 0
            elements = line.split(',') #per ogni linea nell mio file vado a splittare in 2 elementi quando incontro la virgola
            
            
            if len(elements) >= 2:

                if elements[0] != 'epoch':
                        
                    timestamp  = elements[0] #salvo le timestamp in una variabile
                    value = elements[1] #le temperature nell'altra
                    
                    try:
                        timestamp = int(timestamp) #vado a convertire le timestamp in int
                    except:
                        try:
                            timestamp=float(timestamp)
                            timestamp = round(timestamp)
                        except:
                            error = 1
                    
                    if error != 1:
                      if timestamp<0:
                        raise ExamException('valore negativo non accettato')
                    try:
                        value = float(value) #e le temperature in float
                    except:
                        error = 1
                     
                    if error != 1:
                      values = [timestamp,value] #salvo le variabili in un vettore
                    
                    
                      output.append(values) #salvo questo vettore in un altro vettore in modo da creare un array annidato

            else:
                print('\n  in questa linea "{}" mancano elementi \n'.format(line))
                
        for i in range(0, len(output)-1):
            if output[i][0]>=output[i+1][0]:
                raise ExamException('Le date sono ordinate, è stato rivelato un errore di ordine')

        my_file.close()
        return output #ritorno il vettore finale
        

def hourly_trend_changes(self):

    

    values = [] #values è il vettore in cui salvo i valori orari
    output = [] #output serve per salvare il numero di cambi di trend
        
    for i in range(0,len(self)):
        epoch = self[i][0] #salvo in una variabile 
        hour_start_epoch = epoch - (epoch % 3600) #salvo in una variabile  l’inizio di un ora dato un timestamp epoch
        data = [] #inizializzo il vettore data, qui salvo tutte le temperature appartenenti allo stessa ora
        if epoch != 0:
            for j in range(i,len(self)):
                    timestamp = self[j][0]
                    condizione = hour_start_epoch + 3600
                    if timestamp < condizione : #se siamo nella stessa ora
                        data.append(self[j][1]) #aggiungo all'array data
                        self[j][0] = 0 #e assegno il valore 0 alla data
                
            values.append(data)
    
    for i in range(0,len(values)):#in qusto ciclo calcolo se la funzione è crescente, decrescente o costante
        if len(values[i])<1:#controllo che ci sia almeno un valore per ora
            raise ExamException('Ogni giorno ha almeno un dato')
        statistiche = []
        for j in range(0, len(values[i])):#valuto l'ora corrente
            if j==0 and i==0:
                if len(values[i])==1:
                    if values[i+1][len(values[i+1])-1]<values[i][j]:
                        statistiche.append(-1)
                    else:
                        if values[i+1][len(values[i+1])-1] == values[i][j]:
                            statistiche.append(0)
                        else:
                            statistiche.append(1)
                else:
                    pass
            else:
                if j==0 and i!=0:
                    if values[i-1][len(values[i-1])-1]<values[i][j]:
                        statistiche.append(1)
                    else:
                        if values[i-1][len(values[i-1])-1] == values[i][j]:
                            statistiche.append(0)
                        else:
                            statistiche.append(-1)
                else:
                    if values[i][j-1]<values[i][j]:
                        statistiche.append(1)
                    else:
                        if values[i][j-1] == values[i][j]:
                            statistiche.append(0)
                        else:
                            statistiche.append(-1)
        output.append(statistiche)
    
    result = []
    for i in range(0,len(output)):
        conta=0
        for j in range(0, len(output[i])):
            if j==0 and i==0:
                pass
            else:
                if j==0 and i!=0:
                    #print(i,j)
                    if output[i-1][len(output[i-1])-1] != output[i][j]:
                        conta=conta+1
                        #print(output[i-1][len(output[i-1])-1] , output[i][j],i,j)
                else:
                    #print(i,j)
                    if output[i][j-1] !=  output[i][j] :
                        conta=conta+1
                        #print(output[i][j-1] , output[i][j],i,j)
        result.append(conta)
    
    
    return result
time_series_file = CSVTimeSeriesFile(name='data.csv')


time_series = time_series_file.get_data()
#print(time_series)
print(hourly_trend_changes(time_series))