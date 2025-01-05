def outer(x):
    def inner(y):
        return x + y
    return inner


add_five = outer(5)
print(add_five(3))
print(add_five(10))





# (doc) add -> "Функція для створення новогокористувача..."


###     Оператор match      ###

# fruit = input("Sebd Fruit: ")
# match fruit:
#     case "apple":
#         print("This is an apple.")
#     case "banana":
#         print("This is a banana.")
#     case "orange":
#         print("This is an orange.")
#     case _: #Символ " _ " тут використовується як "заглушка" 
#             #для вказівки на будь-які інші випадки, які не відповідають переліченим
#         print("Unknown fruit.")



# point = (1, 5)
# match point:
#     case (0, 0):
#         print("Точка в центрі координат")  
#     case (0, y):
#         print(f"Точка лежить на осі Y: y={y}")  
#     case (x, 0):
#         print(f"Точка лежить на осі X: x={x}") 
#     case (x, y):
#         print(f"Точка має координати:  x={x}, y={y}") 
#     case _:
#         print("Це не точка")


# pets = ["dog", "fish", "cat"]

# match pets:
#     case ["dog", "cat", _]:
#         # Випадок, коли є і собака, і кіт
#         print("There's a dog and a cat.")
#     case ["dog", _, _]:
#         # Випадок, коли є тільки собака
#         print("There's a dog.")
#     case _:
#         # Випадок для інших комбінацій
#         print("No dogs.")




work_experience = int(input("Enter your full work experience in years: "))

if work_experience > 1:
    developer_type = "Middle"
elif work_experience <= 1: 
    developer_type = "Junior"
elif work_experience >= 6:
    developer_type = "Senior"



print(developer_type)
