

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



# ############
# def clean_list(list_to_clean):
#     a=list_to_clean
#     b=[]
#     for i in a:
#         if i not in b:
#             b.append(i)
    
#     return b
# print(clean_list([1,1,1,2,2,3,4,5,6,6]))
# ##_________________________________________###





############
# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)

# def number_of_groups(n, k):
#     n = int(factorial(n) /(factorial(n - k)*factorial(k)))
#     print(n)
#     return n

# # print(factorial(140))
# number_of_groups(50, 7)
#############


#######--------------------------------------------------------
# def first(size, *arg):
#     count = 0
#     for art in arg:
#         count += 1
#     count = count + size
#     print(count)
#     return count
# first(5, 3, 4, 6)


# def second(size, **kwarg):
#     count = 0
#     for kw, value in kwarg.items():
#         count += 1
#     count = count + size
#     print(count)
#     return count
# second(10, com_one="first", com_two=2, com_tre=5)
#######----------------------------------------------------------




####
# str_t = "Dima!"
# leng = 15
# res = (leng - len(str_t)) // 2
# if len(str_t) < leng:
#     print(str_t)
# print(res)
# print(f"{" "*res}{str_t}")
####

# #########
# def format_string(string, length = 0):
#     res = (length - len(string)) // 2
    
#     if len(string) >= length:
#         string = string
#     if len(string) < length:
#         string = "{}{}".format(res*" ", string)
        
#     return str(string)
        
# format_string("Dima", 2)
# #########


#########
# def get_fullname(first_name: str, last_name: str, middle_name: str = None) -> str:
#     if middle_name:
#         return f"{first_name} {middle_name} {last_name}"
#     return f"{first_name} {last_name}"
    
# get_fullname("Dima","Ilin", "Mukolayovith")
#########    



#########
# def discount_price(price = 0, discount = 0):
#     def apply_discount():
#         nonlocal price
#         price = price * (1 - discount)
#     apply_discount()
    
#     print(price)
#     return price
# discount_price(150, 0.23)
#########


########
# def invite_to_event(username):
#     return (f"Dear {username}, we have the honour to invite you to our event")
    
# invite_to_event("Dima")
########



#####
# def greeting():
#     print("Hello world!")
# greeting()
#####


########
# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = int(pool / quantity)
# except ZeroDivisionError:
#     print('Divide by zero completed!')
# print(chunk)
#########


#######
# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for i in message:
#     if i == search:
#         result += 1
# print(result)
#######    



#####
# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# k = 0

# while k < num:
#     sum = (num * (num+1)) / 2
#     k += 1
# print(sum)

#_________________#
# k = 0
# while k < 10:
#     k = k + 1
#     print(k)
#^^^^^^^^^^^^^^^^^#
#####    
    




#####
# num = int(input("Enter a number: "))

# if num > 0:
#     if num % 2 != 0:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"
# print(result)
#####


#####
# work_experience = int(input("Enter your full work experience in years: "))

# if work_experience >= 2 and work_experience <= 5:
#     developer_type = "Middle"
# elif work_experience <= 1: 
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"

# print(developer_type)
#####



####функція "nonlocal"
# def func_outer():
#     x = 2

#     def func_inner():
#         nonlocal x
#         x = 5

#     func_inner()
#     return x

# result = func_outer()  # 5
###########



# x = 50
# def func() -> None:
#     x = 2
#     print('Зміна локального x на', x)  # Зміна локального x на 2
# func()
# print('Глобальний x як і раніше', x)  # x як і раніше 50




# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)  
#     return codes
# result = string_to_codes("Hello world!")
# print(result)




# def modify_list(lst: list) -> None:
#     lst = lst.copy()
#     lst.append(5)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3]



# def modify_list(lst: list) -> None:
#     lst.append(4)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3, 4]


# def modify_string(original: str) -> str:
#     original = "3442"
#     return original

# str_var = "оригінал"
# print(modify_string(str_var))  # виведе: змінено
# print(str_var)                # виведе: оригінал




