def list_sum(the_list):
 somma=0
 for item in the_list:
    somma = somma + item
 print('Somma: {}'.format(sum))
print(list_sum([1,4,10]))

try:
                    from datetime import datetime

                    my_date = datetime.strptime(elements[0] , '%d-%m-%Y')

                except Exception as e:
                    
                    print('Errore nela conversione a formato data: "{}"'.format(e))
                    
                    continue