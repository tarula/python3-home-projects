# this is a calculator that does some cool math. check it out ;-)

from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.BLACK)
print(Back.GREEN) 
what = input("Что делаем? (+, -): " )
print(Back.YELLOW) 

number1 = int(input("Введите число: "))

number2 = int(input("Введите еще одно число: "))
print(Back.BLUE) 
if what == "+":
	result = number1 + number2
	print("Все, что нужно, чтобы вы были счастлив, username - " + str(result))

elif what == "-":
	result = number1 - number2
	print("Все, что нужно, чтобы вы были счастлив, username - " + str(result))

else:
	print("выбрана неверная операция")

input(	)