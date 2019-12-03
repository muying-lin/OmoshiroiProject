from car import Car, ElectricCar

from collections import OrderedDict

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())




from random import randint

class Die():
    def __init__(self,sides,num):
        self.sides = sides
        self.num = num


    def roll_die(self):
        while self.num > 0:
            x = randint(1,self.sides)
            print(x)
            self.num -= 1

new_sides = Die(6,10)
new_sides.roll_die()

new_sides = Die(10,10)
new_sides.roll_die()

new_sides = Die(20,10)
new_sides.roll_die()


