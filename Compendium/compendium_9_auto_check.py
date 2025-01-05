
# class Contacts:
#     current_id = 1

#     def __init__(self):
#         self.contacts = []

#     def list_contacts(self):
#         return self.contacts

#     def add_contacts(self, name, phone, email, favorite):
#         self.contacts.append(
#             {
#                 "id": Contacts.current_id,
#                 "name": name,
#                 "phone": phone,
#                 "email": email,
#                 "favorite": favorite,
#             }
#         )
#         Contacts.current_id += 1

#     def get_contact_by_id(self, id):
#         pass

#     def remove_contacts(self, id):
#         for c in self.contacts:
#             r = c["id"]
#             if r == id:
#                 self.contacts.remove(c)
#                 return c



# users = Contacts()   
# users.add_contacts("Dima", "234234", "dima@gmail.com", True)
# users.add_contacts("Wylie Pope", "3333333", "Wylie_Pope@gmail.com", True)


# print(Contacts.list_contacts(users))
# print(users.remove_contacts(2))
# # print(users.get_contact_by_id(1))

# print(Contacts.list_contacts(users))


#######################################
# class Contacts:
#     current_id = 1

#     def __init__(self):
#         self.contacts = []

#     def list_contacts(self):
#         return self.contacts

#     def add_contacts(self, name, phone, email, favorite):
#         self.contacts.append(
#             {
#                 "id": Contacts.current_id,
#                 "name": name,
#                 "phone": phone,
#                 "email": email,
#                 "favorite": favorite,
#             }
#         )
#         Contacts.current_id += 1

    # def get_contact_by_id(self, id):
    #     for c in self.contacts:
    #         r = c["id"]
    #         if r == id:
    #             return c
            
    #     # result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
    #     # return result[0] if len(result) > 0 else None


# users = Contacts()   
# users.add_contacts("Dima", "234234", "dima@gmail.com", True)
# users.add_contacts("Wylie Pope", "3333333", "Wylie_Pope@gmail.com", True)


# print(users.get_contact_by_id(3))

# # print(Contacts.list_contacts(users))





###############################################################
# class Contacts:
#     current_id = 1
#     contacts = []
    
#     def __init__(self):
#         self.contacts = []
        
#     def list_contacts(self):
#         return self.contacts

#     def add_contacts(self, name, phone, email, favorite):
#         self.contacts.append(
#             {
#                 "id": Contacts.current_id,
#                 "name": name,
#                 "phone": phone,
#                 "email": email,
#                 "favorite": favorite,
#             }
#         )
#         Contacts.current_id += 1
    
# user1 = Contacts()   
# user1.add_contacts("Dima", "234234", "dima@gmail.com", True)

# user2 = Contacts()   
# user2.add_contacts("Wylie Pope", "3333333", "Wylie_Pope@gmail.com", True)



# print(user1.list_contacts())


        # return str(self.contacts)

##########
# class Contacts:
#     current_id = 1
#     def __init__(self):
#         self.contacts = []
        
#     def list_contacts(self):
#         print(self.contacts)
    
#     def add_contacts(self, name, phone, email, favorite):
#         # self.name = name
#         # self.phone = phone
#         # self.email = email
#         # self.favorite = favorite
#         self.contacts.append(
#             {
#                 "id": Contacts.current_id,
#                 "name": name,
#                 "phone": phone,
#                 "email": email,
#                 "favorite": favorite,
#             }
#         )
#         Contacts.current_id += 1
        
#         # self.dict_contact = {}
#         # self.dict_contact["id"] = self.current_id
#         # self.dict_contact["name"] = name
#         # self.dict_contact["phone"] = phone
#         # self.dict_contact["email"] = email
#         # self.dict_contact["favorite"] = favorite

#     # def __str__(self) -> str:
#     #     return str(self.contacts)
        
            
# user1 = Contacts()   
# user1.add_contacts("Dima", "234234", "dima@gmail.com", True)

# user2 = Contacts()   
# user2.add_contacts("Wylie Pope", "3333333", "Wylie_Pope@gmail.com", True)

# Contacts().list_contacts()

# # Contacts.list_contacts
# # print(f"List_conact-> {Contacts().list_contacts()}")
# # print(f"User: {user2.list_contacts()}")



####
# class Contacts:
#     current_id = 1

#     def __init__(self):
#         self.contacts = []

#     def list_contacts(self):
#         return self.contacts

#     def add_contacts(self, name, phone, email, favorite):
#         self.contacts.append(
#             {
#                 "id": Contacts.current_id,
#                 "name": name,
#                 "phone": phone,
#                 "email": email,
#                 "favorite": favorite,
#             }
#         )
#         Contacts.current_id += 1

        
# user = Contacts()   
# user.add_contacts("Dima", "234234", "dima@gmail.com", True)
# user.add_contacts("Willy", "222222", "Willy@gmail.com", True)
# print(user.list_contacts())

##
# class Contacts:
#     current_id = 1
    
#     def __init__(self):
#         self.contacts = []
        
#     def list_contacts(self):
#         return print(self.contacts)
    

#     def add_contacts(self, name, phone, email, favorite):
#         self.contacts = self.contacts
#         self.contacts.append(
#             {
#                 "id": Contacts.current_id,
#                 "name": name,
#                 "phone": phone,
#                 "email": email,
#                 "favorite": favorite,
#             }
#         )
#         Contacts.current_id += 1
#         print(self.contacts)
    
        
        
        
#         # self.dict_contact = {}
#         # self.dict_contact["id"] = self.current_id
#         # self.dict_contact["name"] = name
#         # self.dict_contact["phone"] = phone
#         # self.dict_contact["email"] = email
#         # self.dict_contact["favorite"] = favorite
        
#         # self.contacts.__init__()
        
#     def __str__(self) -> str:
#         return self.contacts
        
            
# user1 = Contacts()   
# user1.add_contacts("Dima", "234234", "dima@gmail.com", True)

# user2 = Contacts()   
# user2.add_contacts("Wylie Pope", "3333333", "Wylie_Pope@gmail.com", True)


# # Contacts.list_contacts
# print(f"List_conact-> {Contacts().list_contacts()}")
# # print(f"User: {user2.list_contacts()}")





###########################################################
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Cat(Animal):
#     def say(self):
#         return "Meow"


# class CatDog:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#         self.say()
        
#     def say(self):
#         return "QQ"
    
#     def change_weight(self, weight):
#         self.weight = weight


# c = Cat("Grek", 8)
# cd = CatDog("CatDog", 12)

# print(c.say())
# print(cd.say())   


####
# class Mammal:
#     phrase = ''

#     def voice(self):
#         return self.phrase


# class Dog(Mammal):
#     phrase = 'Bark!'


# class Cat(Mammal):
#     phrase = 'Meow!'


# class Chupakabra:
#     def voice(self):
#         return 'Whooooo!!!'


# class Recorder:
#     def record_animal(self, animal):
#         voice = animal.voice()
#         print(f'Recorded "{voice}"')


# r = Recorder()
# cat = Cat()
# dog = Dog()
# strange_animal = Chupakabra()

# r.record_animal(cat)  # Recorded "Meow!"
# r.record_animal(dog)  # Recorded "Bark!"
# r.record_animal(strange_animal)  # Recorded "Whooooo!!!"





###########################################
# # txt = "0123"

# # x = txt.startswith("01")
# # print(x)

# ####
# class IDException(Exception):
#     pass

# id_list = ["01", "014"]  

# def add_id(id_list, employee_id): 
#     id_list = list(id_list)
#     swith = str(employee_id)
#     if swith.startswith("01") == False:
#         raise IDException
#         # pass
#     else: 
#         id_list.append(swith)
#         # print(id_list)
#         return id_list
    
# # res = add_id(id_list, "06")
# # print(res)


# try:
#     res = add_id(id_list, "06")
#     print(res)
    
# except IDException:
#     pass
    


##########################################
# import string

# class NameTooShortError(Exception):
#     pass


# class NameStartsFromLowError(Exception):
#     pass

# def enter_name():
#     name = input("Enter name: ")
#     if len(name) < 3:
#         raise NameTooShortError
#     if name[0] not in string.ascii_uppercase:
#         raise NameStartsFromLowError


# while True:
#     try:
#         name = enter_name()
#         break
#     except NameTooShortError:
#         print('Name is too short, need more than 3 symbols. Try again.')
#     except NameStartsFromLowError:
#         print('Name should start from capital letter. Try again.')


# ###########################################
# #Класи \ class
# import string

# class NameTooShortError(Exception):
#     pass

# class NameStartsFromLowError(Exception):
#     pass


# def enter_name():
#     name = input("Enter name: ")
#     if len(name) < 3:
#         raise NameTooShortError
#     if name[0] not in string.ascii_uppercase:
#         raise NameStartsFromLowError

# while True:
#     try:
#         name = enter_name()
#         break
#     except NameTooShortError:
#         print('Name is too short, need more than 3 symbols. Try again.')
#     except NameStartsFromLowError:
#         print('Name should start from capital letter. Try again.')


########
# def input_number():
#     while True:
#         try:
#             num = input("Enter integer number: ")
#             return int(num)
#         except:
#             print(f'"{num}" is not a number. Try again')
# num = input_number()



#############################################
# from collections import UserString
# import re

# class NumberString(UserString):
#     def __init__(self, seq: object) -> None:
#         super().__init__(seq)
#         self.number = re.findall(r"[0123456789]", seq)
        
#     def number_count(self):
#         cout = 0
#         for n in self.number:
#             cout += 1
       
#         return cout
        
# res = NumberString("wer234234")
# print(res.number_count())





######################################
# # payment = [1, -3, 4]
# # def amount_payment(payment):
# #     sum = 0
# #     for value in payment:
# #         if value > 0:
# #             sum = sum + value
# #     return print(sum)

# # amount_payment(payment)

# from collections import UserList

# payment = [1, -3, 4]

# class AmountPaymentList(UserList):
    
#     def amount_payment(payment):
#         sum = 0
#         for val in payment:
#             if val > 0:
#                 sum = sum + val
#         return sum

# res = AmountPaymentList(payment)
# print(res.amount_payment())



####################################
# from collections import UserDict
# class LookUpKeyDict(UserDict):
#     def lookup_key(data, value):
#         keys = []
#         for key in data:
#             if data[key] == value:
#                 keys.append(key)
#         return keys
            


##############################
# from collections import UserString


# class TruncatedString(UserString):
#     MAX_LEN = 2

#     def truncate(self):
#         self.data = self.data[:self.MAX_LEN]


# ts = TruncatedString('abcdefghjklmnop')
# ts.truncate()
# print(ts)  # abcdefg



#######################################################
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass


# class Cat(Animal):
#     def say(self):
#         return "Meow"


# class Dog(Animal):
#     def say(self):
#         return "Woof"


# class CatDog(Cat, Dog):
#     def __init__(self, nickname, weight):
#         super().__init__(nickname, weight)
    
#     def info(self):
#         return f"{self.nickname}-{self.weight}"

# class DogCat(Dog, Cat):
#     def __init__(self, nickname, weight):
#         super().__init__(nickname, weight)
    
#     def info(self):
#         return f"{self.nickname}-{self.weight}"
    
    
# cat = CatDog("Nick", 6)
# dog = DogCat("Simon", 10)
# print(cat.say())
# print(dog.info())





##########################################
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Owner:
#     def __init__(self, name, age, address): #name, вік — age та адреса — address
#         self.name = name
#         self.age = age
#         self.address = address
        
        

#     def info(self) -> str:
#         dict_info = {}
#         dict_info["name"] = self.name
#         dict_info["age"] = self.age
#         dict_info["address"] = self.address
#         return str(dict_info)
            

# class Dog(Animal):
#     def __init__(self, nickname, weight, breed, owner):
#         self.breed = breed
#         self.owner = owner
#         super().__init__(nickname, weight)

#     def say(self):
#         return "Woof"

#     def who_is_owner(self):
#         return str(Owner.info(owner))


# owner = Owner("Sherlock", 24, "London, 221B Baker Street")
# dog = Dog("Simon", 10, "british", owner)

# print(dog.who_is_owner())






###########################################
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Dog(Animal):
#     def __init__(self, nickname, weight, breed):
#         super().__init__(nickname, weight)
#         self.breed = breed
        
#     def say(self):
#         return str("Woof")
    
# dog = Dog("Barbos", 23, "labrador")
# print(dog.say())
    
        
    


#######################################
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight
    


# class Cat(Animal):
#     def __init__(self, nickname, weight):
#         super().__init__(nickname, weight)
        
#     def say(self):
#         return f"Meow"
    
#     # def __str__(self):
#     #     return str(self.nickname), str(self.weight)

# cat = Cat("Simon", 10)
# print(cat.say())



############################################
# from collections import UserDict


# class Field:#Батьківський клас
#     def __init__(self, value):
#         self.nicname = value
#         self.value = value
    
#     def __str__(self):
#         return str(self.value)
    
# class Name(Field):
#     pass

# class Phone(Field):
#     pass

# class Record:
#     def __str__(self):
#         return f"'name': ''"
    
# val = Field("fe.er \nqw")
 
# print(val.value)