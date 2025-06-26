# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# my_car = Car("Toyota", "Corolla")
# print(f"My car is a {my_car.brand} {my_car.model}.")

# class car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# mycar = car ("suzuki", "zx500")      
# print(f"nfiuefu {mycar.brand} {mycar.model}")


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Alice", 25)
# p2 = Person("Alice", 25)

# print(f"{p1.name}")

# if p1.name == p2.name and p1.age == p2.age:
#     print("Both persons are the same.")
# else:
#     print("They are different persons.")

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()