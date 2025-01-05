

file_link = "123/folder_test/txt_test.txt"

file = open(file=file_link, mode="r+", encoding="utf-8")

# print(file.read())

file.close()

#######################################
# class Contacts:
#     current_id = 1
   
  
#     def __init__(self):
#         self.contacts = []
        
#     def list_contacts(self):
#         # print(self.contacts)
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

# # user2 = Contacts()   
# # user2.add_contacts("Wylie Pope", "3333333", "Wylie_Pope@gmail.com", True)

# users = Contacts.list_contacts
# # users.list_contacts

# # print(Contacts.list_contacts)

# # Contacts.list_contacts()
# # print(f"List_conact-> {Contacts().list_contacts()}")
# print(f"User: {users}")