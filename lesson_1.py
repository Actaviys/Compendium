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

