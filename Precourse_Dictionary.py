#-------------------------------------------------------------------------------
#Словники і методи

#Метод get()
# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# # my_dict["gender"] = "Female"
# gend = my_dict.get("gender")
# print("Ім'я:", my_dict.get("name"))
# print("Гендер:", gend)


#Метод clear()
# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# new_dict = my_dict.copy()
# my_dict.clear()
# print("Список перший:", my_dict)
# print("Копійований список:", new_dict)


#Метод pop()
# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# age = my_dict.pop("age")
# print(my_dict["name"])
# print(age, "Років")
# my_dict.clear()
# print("Весь список:", my_dict)


#Додавання нового елемента до списку і видалення оператором del()
# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# my_dict["name"] = "Dima"
# my_dict["age"] = "27"
# my_dict["email"] = "dima@gmail.com"
# print(my_dict)
# del my_dict["email"] #оператор del()
# print(my_dict)
# print("City :", "city" in my_dict)
# print("Email :", "email" in my_dict)

#Сортування методом reverse()
# words = ["banana", "apple", "cherry", "watermelon"]
# words.reverse()
# sorted_words = sorted(words, key=len)
# print(sorted_words)  # Виведе ['apple', 'banana', 'cherry']
# print(words)

#Сортування методом sorted()- копіює і сортує список
# nums = [3, 1, 4, 1, 5, 9, 2]
# # sorted_nums = sorted(nums)
# sorted_nums = sorted(nums, reverse=True)
# print(sorted_nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

#Сортування методом sort()- сортує оригінальний список
# words = ["banana", "apple", "cherry"]
# words.sort(key=len)
# print(words)


#Precourse
#----------------------------------------------------------------------------------

# a = int(input("Напиши число : "))
# b = 7
# res = 5 * (a / b)/2
# print(res)



# my_list = [1, 2, 3, 4, 2, 2, 5, 5, 2]
# count_2 = my_list.count(int(input("Number: ")))
# print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази



# # Встановлюємо ціни на продукти
# price_per_croissant = 1.04
# price_per_glass = 0.34
# price_per_coffee_pack = 4.42

# # Кількість кожного продукту
# num_croissants = int(input("Введіть кількість круасанів: "))
# num_glasses = int(input("Введіть кількість склянок: "))
# num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# # Обчислення загальної вартості
# total_cost = num_croissants * price_per_croissant + \
#              num_glasses * price_per_glass + \
#              num_coffee_packs * price_per_coffee_pack

# # Визначаємо кількість повних доларів і центів
# total_dollars = int(total_cost)
# total_cents = int(total_cost * 100)

# # Вивід результату
# print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
# print(f"Загальна вартість у центах: {total_cents} центів")





# num = 5  # приклад значення для num

# if num > 10:
#     print("num більше за 10")
# else:
#     print("num не більше за 10")


# a = input('Введіть число: ')
# a = int(a)

# if a > 0:
#     print('Число додатне:', a)
# if a == 1:
#     print('Число дорівнює 1')
# else:
#     print("a != 0")


# menu = ["wraps", "sandwiches", "soup", "salad"]
# for i in menu:
#      print(i)


#var1 = 12 + 34
#var1 = 46


#word = "hello"
#var2 = len("hello")
# var2 = 5
 
 
#name = "Wendy\'s dog"
#print(name)


#a = float(input("Enter number1: "))
#b = float(input("Enter number2: "))
#print(a+b)

#print("\n","Dima:")

#print("\t","TEST_commit")