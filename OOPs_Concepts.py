# Object Oriented Program
# 1 Class
# 2 Object
# 3 Inheritance
# 4 Polymorphism
# 5 Abstraction

# Class - is blueprint or model or design of an application
# Properties of class are Variables and Functions
# Class should be represented with first letter capital (ex: Name)

class Sample:
    a = 10
    b = 20

    def m1(self):
        print("M1 Function")

# class will not be stored in memory until we assign

obj1 = Sample() # Creating an object for class
print(obj1.a)
obj1.m1()
print(type(obj1))

