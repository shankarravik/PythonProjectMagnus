# Polymorphism means Many Forms
# We can use the same class as inheritance to update the new class
# We can use polymorphism for Function / Method overriding

class Kia_Sorento_2022:
    def roof(self):
        print("Sun Roof")
    def wheels(self):
        print("Normal ALloy Wheels")
    def music(self):
        print('7" Music Touch Player')
    def braking (self):
        print('Automatic Emergency Braking')

class Kia_Sorento_2023(Kia_Sorento_2022):
    def roof(self):
        print("Panaromic Sun Roof")
        super().roof() # Super class will retain the same values form the inheritancing class
    def music(self):
        print('11" Music Touch Player')
    def mobileConnect(self):
        print("Kia UVO Connect")
    def braking(self):
        print("ADAS")
obj1 = Kia_Sorento_2023()
obj1.roof()
obj1.wheels()
obj1.music()
obj1.mobileConnect()
obj1.braking()
