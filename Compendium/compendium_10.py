

from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass  # Ім'я не потребує додаткової логіки, тому використовуємо базовий клас Field

class Phone(Field):
    def __init__(self, value):
        super().__init__(self._validate_phone(value))

    def _validate_phone(self, phone):
        phone_str = str(phone)
        if len(phone_str) == 10 and phone_str.isdigit():
            return phone_str
        raise ValueError("Phone number must have exactly 10 digits.")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
    
    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            phone_obj.value = self._validate_phone(new_phone)
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def _validate_phone(self, phone):
        phone_str = str(phone)
        if len(phone_str) == 10 and phone_str.isdigit():
            return phone_str
        raise ValueError("Phone number must have exactly 10 digits.")

    def __str__(self):
        phones_str = "; ".join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

# Приклад використання
if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

'''
Опис реалізації:
Field: Базовий клас для полів, який зберігає значення і перетворює його в рядок через метод __str__.

Name: Наслідує Field і не потребує додаткової логіки.

Phone: Наслідує Field і додає валідацію номера телефону, який повинен мати рівно 10 цифр.

Record: Зберігає об'єкт Name і список об'єктів Phone. Реалізовані методи для додавання, видалення, редагування і пошуку телефонів у записі.

AddressBook: Наслідує UserDict і дозволяє додавати, знаходити та видаляти записи за ім'ям.

Приклад використання:
Створюється адресна книга, додаються записи для користувачів "John" і "Jane".
Можна додавати, редагувати та видаляти телефони для запису, а також видаляти самі записи з адресної книги.
Цей код відповідає усім вимогам, зазначеним у завданні. Якщо у вас будуть питання чи потрібна додаткова допомога, звертайтесь!
'''

################################################################################################
# from collections import UserDict

# class AddressBook(UserDict):  # Адресна книга
    
#     def add_record(self, record):  # Метод add_record, який додає запис до self.data.
#         self.data[record.nam.names] = record

#     def find(self, fid):  # Знаходить запис за ім'ям
#         return self.data.get(fid, None)
    
#     def delete(self, delt):  # Видаляє запис за ім'ям.
#         if delt in self.data:
#             del self.data[delt]
#             return f"Deleted: {delt}"
#         return f"Record {delt} not found"
    
#     def __str__(self):
#         records = "\n".join(str(record) for record in self.data.values())
#         return f"{records}"

# class Field:  # Базовий клас
#     pass

# class Name(Field):
#     def __init__(self, names):
#         self.names = names
        
#     def __str__(self):
#         return str(self.names)

# class Phone(Field):
#     def __init__(self, phone):
#         self.phone = self._validate_phone(phone)

#     def _validate_phone(self, phone):
#         phone_str = str(phone)
#         if len(phone_str) == 10 and phone_str.isdigit():
#             return phone_str
#         raise ValueError("Phone number must have exactly 10 digits.")

#     def __str__(self):
#         return self.phone

# class Record:
#     def __init__(self, nam):
#         self.nam = Name(nam)
#         self.phon_list = []

#     def add_phone(self, phon):  # Метод для додавання телефону
#         phone = Phone(phon)
#         self.phon_list.append(phone)

#     def __str__(self):
#         phones = ", ".join(str(phone) for phone in self.phon_list)
#         return f"{self.nam}: {phones}"

# # Приклад використання
# book = AddressBook()  # Створюю адресну книгу

# dima = Record("Dima")
# lisa = Record("Lisa")
# dima.add_phone(2334443221)
# dima.add_phone(1111111111)

# book.add_record(dima)
# book.add_record(lisa)

# print(f"AddressBook-> {book.data}\n")






###############################################################################################
# from collections import UserDict

# class AddressBook(UserDict):  # Адресна книга
    
#     def add_record(self, record):  # Метод add_record, який додає запис до self.data.
#         self.data[record.nam.names] = record

#     def find(self, fid):  # Знаходить запис за ім'ям
#         return self.data.get(fid, None)
    
#     def delete(self, delt):  # Видаляє запис за ім'ям.
#         if delt in self.data:
#             del self.data[delt]
#             return f"Deleted: {delt}"
#         return f"Record {delt} not found"

# class Field:  # Базовий клас
#     pass

# class Name(Field):
#     def __init__(self, names):
#         self.names = names
        
#     def __str__(self):
#         return str(self.names)

# class Phone(Field):
#     def __init__(self, phone):
#         self.phone = self._validate_phone(phone)

#     def _validate_phone(self, phone):
#         phone_str = str(phone)
#         if len(phone_str) == 10 and phone_str.isdigit():
#             return phone_str
#         raise ValueError("Phone number must have exactly 10 digits.")

#     def __str__(self):
#         return self.phone

# class Record:
#     def __init__(self, nam):
#         self.nam = Name(nam)
#         self.phon_list = []

#     def add_phone(self, phon):  # Метод для додавання телефону
#         phone = Phone(phon)
#         self.phon_list.append(phone)

#     def __str__(self):
#         phones = ", ".join(str(phone) for phone in self.phon_list)
#         return f"{self.nam}: {phones}"

# # Приклад використання
# book = AddressBook()  # Створюю адресну книгу

# dima = Record("Dima")
# lisa = Record("Lisa")
# dima.add_phone(2334443221)
# dima.add_phone(1111111111)

# book.add_record(dima)
# book.add_record(lisa)

# print(f"AddressBook-> {book}\n")

# # Знаходження запису
# print(f"Find Dima: {book.find('Dima')}")