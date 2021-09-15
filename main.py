from colorama import init
from colorama import Fore, Back, Style
init()
print (Fore.BLUE)

what = input('давай задачу (я тупой калькулятор): ')

a = float(input('ВНИМЕАНЕИ ПЕРВОЕ ЧИСЛО:'))
b = float(input('второе число полегче давай:'))

if what == '+':
          c = a + b
          print ("Ели решил:" + str(c))
elif what == "-":
    c = a - b
    print("Было сложно:" + str(c))
if what =='*':
    c = a * b
    print('слышь, я сам аж калькулятор достал, он сказал что будет:' + str(c))
if what == '/':
    c = a / b
    print ('вообще ахуел такое спрашивать, за отсос скажу:' + str(c))
else:
    print('СЛЫШЬ БЫДЛО, ОБОСНУЙ')
