import csv

userData =     {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
userData2 =     {
    "name": "Chaim Lewis",
    "email": "null.co.uk",
    "phone": "(992) 97777",
    "favorite": False,
}


def write_contacts_to_file(filename, contacts):
    with open(filename, "w") as f:
        # res = {}.update(contacts)
        Dwriter = csv.DictWriter(f, contacts, delimiter=',')
        Dwriter.writeheader()
        # for d in contacts:
        print(contacts)
        Dwriter.writerows(contacts)

write_contacts_to_file("data.scv", userData)
write_contacts_to_file("data.scv", userData2)
        
        
        
            


def read_contacts_from_file(filename):
    with open(filename, 'r') as f:
        res = []
        reader = csv.DictReader(f)
        for rd in reader:
            res.append(rd)
            
        return res
    
print(read_contacts_from_file("data.scv"))



# # ######################################################
# import json

# userData =     {
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# }

# userData2 =     {
#     "name": "Raymond",
#     "email": "ul.co.uk",
#     "phone": "(992) 914",
#     "favorite": False,
# }

# def write_contacts_to_file(filename, contacts):
#     with open(filename, 'w') as file:
#         json.dump({"contacts": contacts}, file, indent=4)
        

# # write_contacts_to_file("data.json", userData)
# # write_contacts_to_file("data.json", userData2)



# def read_contacts_from_file(filename):
#     with open(filename, 'r') as file:
#         red = json.load(file)
#         return red['contacts']



        
# print(read_contacts_from_file('data.json'))


######################################################
# import pickle

# userData =     {
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# }


# def write_contacts_to_file(filename, contacts):
#     with open(filename, 'wb') as file:
#         pickle.dump(contacts, file)
#     # return rr

# # write_contacts_to_file('data.pkl', userData)


# def read_contacts_from_file(filename):
#     with open(filename, 'rb') as file:
#         red = pickle.load(file)
#         return red
        
# print(read_contacts_from_file('data.pkl'))

#################################################################
# from random import randrange

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, vector):
#         return (
#                 self.coordinates.x * vector.coordinates.x
#                 + self.coordinates.y * vector.coordinates.y
#         )

#     def len(self):
#         return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5
        

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"
    
    
#     def __eq__(self, vector):
#         return self.len() == vector.len()

#     def __ne__(self, vector):
#         return self.len() != vector.len()

#     def __lt__(self, vector):
#         return self.len() < vector.len()

#     def __gt__(self, vector):
#         return self.len() > vector.len()

#     def __le__(self, vector):
#         return self.len() <= vector.len()

#     def __ge__(self, vector):
#         return self.len() >= vector.len()


# class Iterable:
#     def __init__(self, max_vectors, max_points):
#         self.max_vectors = max_vectors
#         self.max_points = Vector(Point(0, max_points))
#         self.current_index = 0
#         self.vectors = []
        
            

#     def __next__(self):
#         if self.max_vectors > self.current_index:
#             self.max_vectors -= 1
#             self.vectors.append(self.max_points)
#             return self.max_points
#         raise StopIteration


# class RandomVectors:
#     def __init__(self, max_vectors=10, max_points=50): 
#         self.max_vectors = max_vectors
#         self.max_points = max_points
        
        

#     def __iter__(self):
#         return Iterable(self.max_vectors, self.max_points)


# vectors = RandomVectors(5, 10)
# for vector in vectors:
#     print(vector)


# # vector1 = Vector(Point(1, 10))
# # vector2 = Vector(Point(3, 10))
# # print(vector1 == vector2)  # False
# # print(vector1 != vector2)  # True
# # print(vector1 > vector2)  # False
# # print(vector1 < vector2)  # True
# # print(vector1 >= vector2)  # False
# # print(vector1 <= vector2)  # True



# # vector1 = Vector(Point(1, 10))
# # vector2 = Vector(Point(10, 10))
# # print(vector1.len())  # 10.04987562112089
# # print(vector2.len())  # 14.142135623730951


# # vector1 = Vector(Point(1, 10))
# # vector2 = Vector(Point(10, 10))
# # scalar = vector2 * vector1
# # print(scalar)  # 110


# # vector1 = Vector(Point(1, 10))
# # vector2 = Vector(Point(10, 10))
# # vector3 = vector2 + vector1
# # vector4 = vector2 - vector1
# # print(vector3)  # Vector(11,20)
# # print(vector4)  # Vector(9,0)


# # vector = Vector(Point(1, 10))
# # print(vector())  # (1, 10)
# # vector = Vector(Point(1, 10))
# # print(vector(5))  # (5, 50)


# # point = Point(1, 10)
# # vector = Vector(point)
# # print(point)  # Point(1,10)
# # print(vector)  # Vector(1,10)
        

        


###################################################
# class ListedValuesDict:
#     def __init__(self):
#         self.data = {}

#     def __setitem__(self, key, value):
#         if key in self.data:
#             self.data[key].append(value)
#         else:
#             self.data[key] = [value]

#     def __getitem__(self, key):
#         result = str(self.data[key][0])
#         for value in self.data[key][1:]:
#             result += ", " + str(value)
#         return result


# l_dict = ListedValuesDict()
# l_dict[1] = 'a'
# l_dict[0] = 'b'
# print(l_dict[1])  # a, b
# print(l_dict[0])