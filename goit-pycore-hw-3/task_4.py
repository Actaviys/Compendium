

from datetime import datetime




def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    today = datetime.today().date()
    
    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birt_this_year = birthday.replace(year=today.year)
        if birt_this_year < today:
            pass
            
        print((today - birt_this_year).days)
        print(birthday)
    
    # return f"Список користувачів{users}"

users = [
    {"name": "John Doe", "birthday": "1968.09.09"},
    {"name": "Dima Ilin", "birthday": "1997.06.14"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

