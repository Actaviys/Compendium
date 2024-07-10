


from datetime import datetime



def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    today = datetime.today().date()
    
    
    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birt_this_year = birthday.replace(year=today.year)
        res_bird = int((today - birt_this_year).days)
        # print((today - birt_this_year).days)
        
        
        print(res_bird)
        
        # if birt_this_year < today:
        #     print(f"@@@{(today - birt_this_year).days}")
        # if birt_this_year == today:
        #     print("Happy Birthday!!!!")
        # if birt_this_year < 7:
        #     print("()()()()")
        
        print("-----------------")
    
    
    
                
    
    print(birthday)
    
    # return f"Список користувачів{happy_list}"


users = [
    {"name": "John Doe", "birthday": "1968.07.19"},
    {"name": "Dima Ilin", "birthday": "1997.06.14"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.07.11"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)






# import random


# def get_numbers_ticket(min, max, quantity):
#     save = []
#     res = []
    
#     def randon_range(min, max):  
#         nonlocal save
#         save = random.randrange(min, max, 1)
        
    
#     randon_range(min, max)
#     res.append(save)
#     quantity = quantity - 1 
    
    
        
#     print(save)
#     return res


# lottery_numbers = get_numbers_ticket(1, 36, 5)
# print("Ваші лотерейні числа:", lottery_numbers)




# ##_________________________________________###
# def clean_list(list_to_clean):
#     a=list_to_clean
#     b=[]
#     for i in a:
#         if i not in b:
#             b.append(i)
#         # else: b.append(0)
#     print(b)       
    
#     return b
# print(clean_list([1,1,2,3,3]))
# ##_________________________________________###
