#----------------------------------------#
###         Аргументи функції          ###
#----------------------------------------#



# name = input("Як тебе звати? ")
# def greet(name, message="Привіт"):
#     print(f"{message}, {name}!")
# greet(name)



# def say(message, times=1):
#     print(message * times)
# say('Привіт') 
# say('Світ', 5)




# def real_cost(base: int, discount: float = 0) -> float:
#     return base * (1 - discount)

# price_bread = 15
# price_butter = 50
# price_sugar = 60

# current_price_bread = real_cost(price_bread)
# current_price_butter = real_cost(price_butter, 0.15)
# current_price_sugar = real_cost(price_sugar, 0.07)

# print(f'Нова вартість хліба: {current_price_bread}')
# print(f'Нова вартість масла: {current_price_butter}')
# print(f'Нова вартість цукру: {current_price_sugar}')




#__________________#
# #параметр (*args)

# def print_all_args(*args):
#     for arg in args:
#         print(arg)
# print_all_args(65, 'Hello', True)


# def concatenate(*args) -> str:
#     result = ""
#     for arg in args:
#         result += arg
#     return result
# print(concatenate("Hello", " ", "world", "!"))


# def concatenate(*strings) -> str:
#     result = ""
#     for arg in strings:
#         result += arg
#     return result
# print(concatenate("Hello", " ", "world", "!"))




#___________________#
# #Параметр (**kwargs)

# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# greet(name="Alice", age=25)


# def example_function(*args, **kwargs):
#     print("Позиційні аргументи:", args)
#     print("Ключові аргументи:", kwargs)
# example_function(1, 2, 3, name="Alice", age=25)



###
#Розпакування списків та словників#

# #Розпаковка списків
# my_list = [1, 2, 3]
# a, b, c = my_list
# a, _, c = my_list
# a, *rest = my_list


# #Розпаковка словників#
# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# person_info = {"name": "Alice", "age": 25}
# greet(**person_info)






