import pyowm

owm = pyowm.OWM('3171d33eb8ec7865bab3cac0af96ee01', language = "ru")

place = input("Я умею давать текущий прогноз погоды. Напиши город, где хочешь узнать погоду: ")

observation = owm.weather_at_place(place)

weather = observation.get_weather()

temp = weather.get_temperature('celsius')["temp"]

wind = weather.get_wind()["speed"]

print("\n")
print("В городе " + place + " сейчас " + weather.get_detailed_status() + ".")
print("Текущая температура " + str(temp) + " Цельсия.")
print("Ветер достигает " + str(wind) + " метров в секунду.")

if temp < 10:
	print("Надень пальто и погладь кота!")
	print("\n")
elif temp > 20:
	print("Одевайся потеплее и погладь кота два раза!")
	print("\n")
else:
	print("Надевай, что хочешь, но кота погладь! Без кота и жизнь не та.")
	print("\n")

while True:
   answer = input('Напиши "выйти" без кавычек и нажми Enter, чтобы выйти из программы:')
   if answer.lower().startswith("выйти"):
      print("Пока ;-)")
      exit()