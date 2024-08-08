




# ################################
# #Декоратор вимірювання швидкості виконання функції

# import time

# def time_func(func):
#     def wrapper(*agrs, **kwargs):
#         s_time = time.time()
#         res = func(*agrs, **kwargs)
#         e_time = time.time()
#         print(f"Running time: {e_time - s_time}")
#         return res
#     return wrapper
            

# @time_func
# def calculate_sum(num: list[int]) -> int:
#     return sum(num)

# @time_func
# def square(num: int) -> int:
#     return ((num ** 2) * (num * 10000000)) * 100000000

# print(calculate_sum)
# print(square(3640))




# ###########################
# #[{'name': 'John', 'birthday': '21.07.2001'}, {'name': 'Dima', 'birthday': '05.03.1997'}]
# from datetime import datetime

# def find_users_with_birthday_this_year(users: list[dict]) -> list[dict]:
#     users_with_datetime = []
#     for user in users:
#         birthday_datetime = datetime.strptime(user['birthday'], '%d.%m.%Y')
#         users_with_datetime.append({'name': user['name'], 'birthday': birthday_datetime})



#     print(users_with_datetime)

# find_users_with_birthday_this_year([{'name': 'John', 'birthday': '21.07.2001'}, {'name': 'Dima', 'birthday': '05.03.1997'}])



# #################
# #Розрахунок об'єму
# from typing import Callable

# def calculate_volume(a: int) -> Callable[[int], Callable[[int], Callable[[int], int]]]:
#     def resive_height(b: int) -> Callable[[int], int]:
#         def resive_width(c: int) -> int:
#             return a * b * c
#         return resive_width
#     return resive_height

# print(calculate_volume(3)(4)(5))

# #[{'name': 'Josh'}, {'name': 'Dima'}]
# # fn (2, 3)('J')




###############
#Функція для генерування послідовних чисел

# def get_unique_id_closure() -> int:
#     id = 0
#     def get_next_id():
#         nonlocal id
#         id += 1
#         return id
#     return get_next_id
    
# next_numder_function = get_unique_id_closure()
# print(next_numder_function())
# print(next_numder_function())
# print(next_numder_function())

#########
# id = 0

# def get_unique_id() -> int:
#     global id
#     id += 1
#     return id

# print(get_unique_id())
# print(get_unique_id())
# print(get_unique_id())


    
    
    


































