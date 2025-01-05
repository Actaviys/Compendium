def factorial(n):
    if n == 0: # базовий випадок
        return 1
    else:
        print(n)
        return n * factorial(n-1) # рекурсивний випадок

print(factorial(5)) # виведе 120



# name = input("Your name? ")
# email = input("Your email: ") 
# age = int(input("Your age: "))
# height = float(input("Your height: "))
# is_active = True
