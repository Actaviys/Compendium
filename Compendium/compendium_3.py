#-------------------------------------#
###         Булева алгебра          ###
#-------------------------------------#

# #Оператор "and" (і)#
# a = True and True  # True
# a = True and False  # False
# a = False and True  # False
# a = False and False  # False


# #Оператор "or" (або)#
# a = True or True  # True
# a = True or False  # True
# a = False or True  # True
# a = False or False  # False


# #Оператор "not" (ні)#
# a = not 2 < 0  # True
# a = not 2 > 0  # False
# print(a)



#___________________________________________#
#-Приклади-#

# name = "Taras"
# age = 22
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")
# elif name and age >= 18:
#     print("Refusal")



# num = int(input("Введіть число: "))
# length = len(str(num))
# if length == 2 and num % 2 == 0:
#     print("Парне двозначне число")
# else:
#     print("Ні")



# #"FizzBuzz"#
# #Перевіряємо кратність
# num = int(input())
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)




#--------------------------------------#
#Блоки інструкцій та тернарні оператори#
#--------------------------------------#

#Тернарні операції:
# is_nice = True
# state = "nice" if is_nice else "not nice"
# print(state)

# some_data = None
# msg = some_data or "Не було повернено даних"
# print(msg) ##для скороченої форми використовується саме оператор or (АБО).













