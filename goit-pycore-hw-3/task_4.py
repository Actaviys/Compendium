

from datetime import datetime


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    
    today = datetime.today().date() #Змінна з поточною датою
    results = [] #Змінна для результату
    
    
    for user in users: #Цикл для читання списку
        
        birthday = datetime.strptime(user["birthday"], '%Y.%m.%d').date() #Стріпаємо день народження в об'єкт datetime
        
        birt_this_year = birthday.replace(year=today.year) #Витягуємо рік з дати народження
        
        congr_date = user["birthday"] #Змінна для дати привітання
        
        
        res_bird = int((birt_this_year - today).days) #Віднімаємо теперішню дату від дня нородження
        
        r = int(birt_this_year.strftime("%u")) # День тижня від 1 до
        
        nam = user["name"] #Змінна для name
        
        s = {}
        s.update({"name": nam})
        s.update({"congratulation_date": congr_date})
        
        
        
        
        
        if res_bird <= 7 and res_bird >= 0:        
            results.append(s)
            
            
        # if r == 6 or r == 7:
        
        # if birt_this_year < today:
        #     print(f"{user}Next Year")
        # print(s)
                
        

    return results
    
 
 
users = [
    
    {"name": "Jane Smith", "birthday": "1990.07.18"},
    {"name": "Dima Ilin", "birthday": "1997.07.14"},
    {"name": "John Doe", "birthday": "1968.07.06"},
    {"name": "Bred Lohan", "birthday": "1985.01.23"},
    {"name": "Viktoria Lopes", "birthday": "2001.07.11"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

