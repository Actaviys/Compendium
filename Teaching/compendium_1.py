            # Множини і Кортежі#

# #Видалення елемента (Без винятку)
# my_set = {1, 2, 3, 4, 5}
# my_set.discard(6)
# print(my_set)

# #Видалення елемента (З винятком)
# my_set = {1, 2, 3, 4, 5}
# my_set.remove(6)
# print(my_set)

# #Додавання елемента
# my_set = {1, 2, 3, 4, 5}
# my_set.add(6)
# print(my_set)


# #Перетворення списку в множину
# my_set = [1, 2, 3, 1, 2, 3]
# d_set = set(my_set)
# s_list = list(d_set)
# # my_set = {1, 2, 3, 1, 2, 3}
# # my_set = set("hello")
# # print(my_set)
# print(d_set)
# print(s_list)



#---------------------------------------------------------------
#Математичні операції над множинами

# ###     intersection() , '&'     ### - Перетин множин
# a = {1, 2, 3}
# b = {3, 4, 5}
# # print(a & b)
# print(a.intersection(b)) #{3}

# ###     difference() , '-'    ### - Різниця множин
# a = {1, 2, 3}
# b = {3, 4, 5}
# # print(a - b)
# print(a.difference(b)) #{1, 2}

# ###     symmetric_difference() , '^'    ### - Симетрична різниця множин
# a = {1, 2, 3}
# b = {3, 4, 5}
# # print(a ^ b)
# print(a.symmetric_difference(b)) #{1, 2, 4, 5}

# ###     union() , '|'   ### - Об'єднання двох множин без дублікатів
# a = {1, 2, 3}
# b = {3, 4, 5}
# # print(a | b)
# print(a.union(b)) #{1, 2, 3, 4, 5}




#---------------------------------------------------------------
#Заморожені множини

# a = frozenset([1, 2, 3])
# b = frozenset([3, 4, 5])

# union = a | b  # Об'єднання множин
# intersection = a & b  # Перетин множин
# difference = a - b  # Різниця множин
# symmetric_difference = a ^ b  # Симетрична різниця

# print(union)  # frozenset({1, 2, 3, 4, 5})
# print(intersection)  # frozenset({3})
# print(difference)  # frozenset({1, 2})
# print(symmetric_difference)  # frozenset({1, 2, 4, 5})





#---------------------------------------------------------------
    ### Кортежі ###


# my_tuple = tuple()
# # my_tuple = (1,)
# # my_tuple = (1, 2, 3)
# # my_tuple = (1, "Hello", 3.14)
# my_tuple = 1, "Hello", 3.14
# first_item = my_tuple[1]
# print(my_tuple)
# print(first_item)


#Словник(points), з ключами(0, 0):, і іменами/назвами("A")
# points = {
#     (0, 0): "O",
#     (1, 1): "A",
#     (2, 2): "B"
# }
# # print(points)
# print(points[(1, 1)])






#-------------------------------------------------------------------
    ### Методи рядків ###


# game_string = 'My favorite "Game"'
# print(game_string)

# s = "Hello world!"
# print(s[0])# H
# print(s[-1])# !

# s = "Hello World" 
# print(s.upper()) # Виведе "HELLO WORLD"

# s = "Some Text"
# print(s.lower())  # Виведе 'some text'

# s = "Hello Dima :)"
# print(s.startswith("He")) # Буде True

# s = "Hello Dima :)"
# print(s.startswith("Hello Dima :)")) # Буде True / Якщо("Hello Dima")-False

# s = "Hello.jpg"
# print(s.endswith("jpg")) # Буде True / Якщо("Hello.jp")-False

# s = "hello world".capitalize() 
# print(s) # Буде "Hello world"

# s = "hello world".title()
# print(s) # Буде "Hello world"


# print("12765".isdigit()) # True / Якщо("1543nj")-False
# print("hello".isalpha()) # True / Якщо("hello55")-False
# print(" ".isspace()) # True / Якщо("ff 2")-False


        ########
#   Форматування рядків
# name = 'Dima'
# age = 25

# #Просте форматування рядка
# print('1 Hello, {}!'.format(name))
# print(f'2 Hello, {name}! $')

# #Форматування з декількома аргументами
# print('1 Hello, {}. You are {} years old.'.format(name, age))
# print(f'2 Hello, {name}. You are {age} years old . $')

# #Використання іменованих аргументів
# print('1 Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))
# print(f'2 Hello, {name+"Smitt"}. You are {age+10} years old . &&&')

# #Використання індексів для вказівки порядку аргументів
# print('1 Hello, {1}. You are {0} years old.'.format(age, name))
# print(f'2 Hello, {name[2]}. You are {None} years old . $')



        ########
#   Зрізи у Python (Slice)

# #Елемент по індексу
# s = "Hello, World!"
# first_five = s[1]
# print(first_five)  # Виведе "e"

# #послідовність[початок:кінець:крок]
# s = "Hello, World!"
# first_five = s[2:9:2]
# print(first_five)  # Виведе "lo o"

# #Перші 5 літер рядка:
# s = "Hello, World!"
# first_five = s[:5]
# print(first_five)  # Виведе 'Hello'


# #НЕпарні числа
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = numbers[0:10:2]
# print(odd_numbers)
# #Коротко
# odd_numbers = numbers[::2]
# print(odd_numbers)

# #Парні
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = numbers[1:10:2]
# print(odd_numbers)
# #коротко
# odd_numbers = numbers[1::2]
# print(odd_numbers)

# #Кратні трьом
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = numbers[2:10:3]
# print(odd_numbers)
# #коротко
# odd_numbers = numbers[2::3]
# print(odd_numbers)

# #Зворотній порядок
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# r_numbers = numbers[::-1]
# print(r_numbers)

# #Копіювання
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# copy_numbers = numbers[:]
# print(copy_numbers)

