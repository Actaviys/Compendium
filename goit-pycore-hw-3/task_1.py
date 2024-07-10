 
from datetime import datetime, date #Імпортуємо бібліотеку

def get_days_from_today(date_str):
    
    date_s = 0 #Сюди зберігаю вхідний список 

    date_s = date_str.split("-")#Робимо список вхідної дати і обрізаємо "-"
   
    #Розбиваємо список по змінних
    year_in = int(date_s[0])
    month_in = int(date_s[1])
    day_in = int(date_s[2])
    date_parameters = datetime(year=year_in, month=month_in, day=day_in).date()  #Створюємо змінну з параметрами вхідного списку

    now_date = datetime.today().date() #Створюємо змінну з поточною датою 
    date_str = now_date - date_parameters     # Шукаємо різницю
    
    
    return date_str  #Повертаємо значення


result = get_days_from_today("2021-12-09")
print(result)   #Виводжу результат