import os
from dotenv import load_dotenv
from weather_sdk import get_new_event, SMSServer


load_dotenv()

token = os.getenv('SMS_TOKEN')
server = SMSServer(token)
token = os.getenv('FORECAST_TOKEN')

town_title = 'Курск'
new_event = get_new_event(token, town_title)

event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_message = """{town_title}: {event_time} {event_date} {event_area} \
ожидается {phenomenon_description}. Будьте внимательны и \
осторожны.""".format(phenomenon_description=phenomenon_description, \
town_title=town_title, event_time=event_time, event_date=event_date, \
event_area=event_area)

server.send(sms_message)

# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Выведу переменную new_event
# Код для проверки: print(new_event)
# Установленный факт: переменная не пуста
# Вывод: проблема не здесь

# Гипотеза 2.1: town_title на самом деле пуста
# Способ проверки: выведу переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: выводится название города
# Вывод: проблема не здесь

# Гипотеза 2.2: В town_title не название города
# Способ проверки: выведу переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: выводится название города
# Вывод: проблема не здесь

# Гипотеза 3.1: Переменная `event_time` пуста/в ней не время
# Способ проверки: Выведу переменную event_time
# Код для проверки: print(event_time)
# Установленный факт: переменная не пуста и корректна
# Вывод: проблема не здесь

# Гипотеза 3.2: Переменная `event_date` пуста/в ней не дата
# Способ проверки: Выведу переменную event_date
# Код для проверки: print(event_date)
# Установленный факт: переменная не пуста и корректна
# Вывод: проблема не здесь

# Гипотеза 3.3: Переменная `event_area` пуста/в ней не место
# Способ проверки: Выведу переменную event_area
# Код для проверки: print(event_area)
# Установленный факт: переменная не пуста и корректна
# Вывод: проблема не здесь

# Гипотеза 3.4: Переменная `phenomenon_description` пуста/в ней не описание погодного явления
# Способ проверки: Выведу переменную phenomenon_description
# Код для проверки: print(phenomenon_description)
# Установленный факт: переменная не пуста и корректна
# Вывод: проблема не здесь

# Гипотеза 4: Неправильно оформлен метод .format для переменных sms_message и sms_template
# Способ проверки: исключение переменной sms_template
# Код для проверки: sms_message = """{town_title}: {event_time} {event_date} {event_area} \
#ожидается {phenomenon_description}. Будьте внимательны и \
#осторожны.""".format(phenomenon_description=phenomenon_description, \
#town_title=town_title, event_time=event_time, event_date=event_date, \
#event_area=event_area)
# Установленный факт: прогноз выводится, хотя и не корректно
# Вывод: это не последняя ошибка

# Гипотеза 5: Переменная token пуста
# Способ проверки: Выведу переменную token
# Код для проверки: 
#token = os.getenv('FORECAST_TOKEN')
#town_title = 'Курск'
#print(token)
#token = os.getenv('SMS_TOKEN')
#server = SMSServer(token)
#print(token)
# Установленный факт: переменная не пуста и принимает два разных значения,\
# 85b98d96709fd49a69ba8165676e4592 и aGVsbG8gY3J5cHRvIGVudHVzaWFzdCA7KQ==
# Вывод: проблема не здесь

# Гипотеза 6: В переменную new_event = get_new_event(token, town_title)\
# попадает не тот агрумент token (их в коде два, token = os.getenv('SMS_TOKEN') и\
# token = os.getenv('FORECAST_TOKEN'))
# Способ проверки: изменим порядок строк кода
# Код для проверки:
#token = os.getenv('SMS_TOKEN')
#server = SMSServer(token)
#token = os.getenv('FORECAST_TOKEN')
# Установленный факт: прогноз выводится корректно
# Вывод: код работоспособен