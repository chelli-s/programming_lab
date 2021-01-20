class CSVFile:

    def __init__(self, name):

        self.name = name

    def get_data(self, start=None , end=None):

        values = []
        i = start
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            
            print('Errore nella lettura del file: "{}"'.format(e))
            
            return None
        
        for line in my_file:
            
            elements = line.split(',')

            if i<=end+1:

                if elements[0] != 'Date':
                    
                    date  = elements[0]
                    value = elements[1]
                
                    try:
                        value = float(value)
                    except Exception as e:

                        print('Errore nela conversione a float: "{}"'.format(e))
                    
                        continue

                    values.append(value)
            
            i=i+1
        
        my_file.close()
        return values


    def get_data_vendite(self):

        dates = []
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            print('Errore nella lettura del file: "{}"'.format(e))
            return None
            
        for line in my_file:
            
            elements = line.split(',')

            if elements[0] != 'Date':
                    
                my_date  = elements[0]
                value = elements[1]
                
                try:
                    from datetime import datetime

                    my_date = datetime.strptime(elements[0] , '%d-%m-%Y')

                except Exception as e:
                    
                    print('Errore nela conversione a formato data: "{}"'.format(e))
                    
                    continue
                
                dates.append(my_date)
        
        my_file.close()
        
        print('Date contenute nel file: ')
        for data in dates:
            print(data.strftime('%d-%m-%Y'))

    def somma(self):

        values = []
        somma = 0
        i = 0

        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            
            print('Errore nella lettura del file: "{}"'.format(e))
            
            return None
        
        for line in my_file:
            
            elements = line.split(',')

            if elements[0] != 'Date':
                    
                date  = elements[0]
                value = elements[1]
                
                try:
                    value = float(value)
                except Exception as e:

                    print('Errore nela conversione a float: "{}"'.format(e))
                    
                    continue

                values.append(value)

                somma = somma + values[i]
                values.append(value)
        i=i+1
        
        my_file.close()
        return somma


    def fit(self, data):
        raise NotImplementedError('Questo modello non prevede fit')

    def predict(self, prev_month):
        
        somma=0

        for i in range(1,len(prev_month)):
            somma=somma+(prev_month[i]-prev_month[i-1])
        
        media=somma/len(prev_month)
        prev=prev_month[-1] + media

        return prev



mio_file = CSVFile(name='shampoo_sales.csv')

print('Nome del file: "{}"'.format(mio_file.name))
data = mio_file.get_data(2,7)
print(mio_file.get_data(2,7))
print(mio_file.predict(data))