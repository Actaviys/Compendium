# num = "+380123456789"

# if isinstance(num, str) and len(num) == 13 and num.startswith("+380"):
#     print(num)



# d = {}
# print(d)
# d.update({"d":"42135"})
# # print(d)
# d.update({"ddd":"444444"})
# print(d)


########################################
# import re

# text = """
#     Загальний дохід працівника складається з 
#     декількох частин: 1000.01 як основний дохід, 
#     доповнений додатковими надходженнями 27.45 і 324.00 доларів. +2000 ЗП
# """


# def generator_numbers(text_in: str): #Генератор чисел витягнутих з тексту
#     res = re.findall(r"\b[0-9.]+\b", text_in) #Витягаю в список всі числа з тексту
#     for n in res: #Встановлюю цикл для генератора
#         yield n #Повертаю значення з кожної наступної ітерації

# rr = generator_numbers(text)
# for tt in rr:
#    print(tt)








###########################################
# print("___Команди___ \
#     \n close -  вийти з цикла\
#     \n fibonacci - вирахувати число Фібоначчі\
#     \n cache - виводить повний словник з числами Фібоначчі")




# def caching_fibonacci():
#     fib_cache = {15: 987} # Кеш для функції
#     def fibonacci(f): #Функція для обчислення Фібоначчі
#         if f <= 1:
#             return 1
#         return fibonacci(f - 1) + fibonacci(f - 2)
    
    
#     while True:
#         inp = input("\nВведіть команду: \n-->")
#         inp_split = inp.split() #Розбиваю команду на список
#         if inp_split[0] == "close": #Команда виходу з цикла
#             break
        
#         if inp_split[0] == "fibonacci":
#             try: #Роблю перевірку якщо не ввели число після команди
#                 num = int(inp_split[1]) #Зберігаю в змінну як int       
#             except: print("Введіть число після команди fibonacci \nНаприклад: fibonacci 15") #Виводжу помилку
            
#             try:
#                 for cache in fib_cache: #Цикл для читання кешу
#                     if num == cache: #Якщо в кеші є число яке ввели то виводжу Фібогаччі з кешу
#                         print(f"{fib_cache[num]} ->Фібоначчі числа з кешу {num}") #Виводжу результат перевірки
#                         break
    
#                 fibs = fibonacci(num) #Якщо введеного числа числа немає в кеші то викликаю функцію обрахунку Фібоначчі
#                 fib_cache[num] = fibs
#                 print(f"{fibs} ->Фібоначчі числа {num}") 
                
#             except: next

            
#         if inp_split[0] == "cache":
#             print(fib_cache)
        




# caching_fibonacci()

            
        
    








###########################################
# fib_cache = {15: 987, 14: 610}

# for fib in fib_cache.keys():
#    # if 15 == int(fib):
#    print(fib_cache[fib])

# print(fib_cache.keys())



############################
# def fibonacci(f):
#    if f <= 1:
#       return 1
#    return fibonacci(f - 1) + fibonacci(f - 2)


# print(fibonacci(15))