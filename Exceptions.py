# Error - Unexpected Evennt that stops the normal flow is called error

# Compile error is also called as Rule error

def m1():
    print("Welcome")

# Unexpected error also called as Run time error
# try to Handle the issue instead of solving the issue, during run time errors

class Sample:
    def m2(self):
        a = 10
        b = 10
        print(a/b)
obj1 = Sample()
obj1.m2()

# Exception will handle the error
class Sample:
    def m2(self):
        a = 10
        b = 0
        try:
            print(a/b)
        except Exception as e:
            print(e)
obj1 = Sample()
obj1.m2()

class Sample:
    def m2(self):
        a = 10
        b = 0
        try:
            print(c)
            print(a/b)
        except Exception as e:
            print(e)
obj1 = Sample()
obj1.m2()

# One try block will only handle one error
class Sample:
    def m2(self):
        a = 10
        b = 0
        try:
            print(c)
            print(a/b)
        except Exception as e:
            print(e)
obj1 = Sample()
obj1.m2()
