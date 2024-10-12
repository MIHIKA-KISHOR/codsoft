import random
import string
import FreeSimpleGUI as fg

upper = random.sample(string.ascii_uppercase,2)
lower = random.sample(string.ascii_lowercase,2)
digits = random.sample(string.digits,2)
symbols = random.sample(string.punctuation,2)

total= upper+lower+digits+symbols
total= random.sample(total,len(total))
total= ''.join(total)
print(total)



fg.theme('Green')
#fg.set_option(font ='verdana 15')
layout = [
    [fg.Text('Uppercase: '), fg.Input(size=15, key ='-UP-')],
    [fg.Text('Lowercase: '), fg.Input(size=15, key ='-LOW-')],
    [fg.Text('Digits: '), fg.Input(size=15, key ='-DIG-')],
    [fg.Text('Symbols: '), fg.Input(size=15, key ='-SYM-')],
    [fg.Button('ok'),fg.Button('Cancel')],
    [fg.Text('Password'), fg.Multiline(size=15,no_scrollbar=True,disabled=True, key ='-PASS-')]
]

window = fg.Window('Password Generation ',layout)

while True:
    event, values = window.read()
    if event== 'cancel' or event == fg.WIN_CLOSED:
        break
    if event =='ok':
        try :
          
          u_upper = int(values['-UP-'])
          upper = random.sample(string.ascii_uppercase,u_upper)
          u_lower = int(values['-LOW-'])
          lower = random.sample(string.ascii_lowercase,u_lower)
          u_digits = int(values['-DIG-'])
          digits = random.sample(string.digits,u_digits)
          u_symbols = int(values['-SYM-'])
          symbols = random.sample(string.punctuation,u_symbols)

          total= upper+lower+digits+symbols
          total= random.sample(total,len(total))
          total= ''.join(total)
          window['-PASS-'].update(total)
        except ValueError:
          window['-PASS-'].update("NO VALID NUMBER")  

window.close()
