class CSVFile:

    def __init__(self, name):

        self.name = name

    def somma(self, data):
        somma=0
        for i in range(2,len(data)):
            somma=somma+data[i]
        return somma

    def get_data_in_range(self, start=None , end=None):

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
                            float(value)
                        except Exception as e:

                            print('Errore nela conversione a float: "{}"'.format(e))
                        
                            continue

                        values.append(value)
                
                i=i+1
            
            my_file.close()
            return values

    def get_data(self):

        values = []
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
                    float(value)
                except Exception as e:

                    print('Errore nela conversione a float: "{}"'.format(e))
                        
                    continue

                values.append(value)
            
            
        
        my_file.close()
        return values

mio_file = CSVFile(name='shampoo_sales.csv')

data = mio_file.get_data_in_range(1,37)

print('dati: ',data)
sommatoria=mio_file.somma(mio_file.get_data())
print('somma: ', sommatoria)