import re

pattern = '^[RDTAC]?x?[a-h][1-8]$'

def check_chess_syntax(self):
    if re.match(pattern,self) != None or self=='0-0' or self=='0-0-0':
        pass
    else:
        raise Exception('non valido')    


# TEST
for text in [
    # VALID SAMPLES
    'a2','xc5','0-0','Tg8','Rxb7',
    # INVALID SAMPLES
    'a9','Ga2','sbricci','']:
    try:
        check_chess_syntax(text)
    except:
        print("'{}' is INVALID:".format(text))
    else:
        print("'{}' is a valid move".format(text))

# Solo i primi cinque input devono risultare validi