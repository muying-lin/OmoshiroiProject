class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + self.cuisine_type)

    def open_restaurant(self):
        print('The reataurant is open')

my_new_restaurant = Restaurant('xilaideng','chinese food')
print(my_new_restaurant.describe_restaurant())

class User():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def describe_user(self):
        print(self.first_name + self.last_name)
        print(self.age)
    def greet_user(self):
        print("Hello " + self.first_name.title() + self.last_name.title())

new_user = User('mu','ying','22')
print(new_user.describe_user())
print(new_user.greet_user())

#9-4
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + self.cuisine_type)

    def open_restaurant(self):
        print('The reataurant is open')

    def read_number(self):
        print('there are ' + str(self.number_served) + ' have lunch.')

    def set_number_served(self,change):
        self.number_served = change


    def increment_number_served(self,people):
        self.number_served += people

my_old_restaurant = Restaurant('kfc',' chinese food')
print(my_old_restaurant.describe_restaurant())

my_old_restaurant.increment_number_served(20)
my_old_restaurant.read_number()

my_old_restaurant.increment_number_served(30)
my_old_restaurant.read_number()

my_old_restaurant.set_number_served(20)
my_old_restaurant.read_number()

#9-5

class User():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name + self.last_name)
        print(self.age)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def read_login_attempts(self):
        print(self.login_attempts)

    def greet_user(self):
        print("Hello " + self.first_name.title() + self.last_name.title())

    def reset_login_attempts(self):
        self.login_attempts = 0

new_user = User('mu','ying','22')
print(new_user.describe_user())
print(new_user.greet_user())

new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.read_login_attempts()

new_user.reset_login_attempts()
new_user.read_login_attempts()

#将实例用作属性
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size ==70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85



class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()




#9-6
class Flavors():
    def __init__(self,flavors):
        self.flavors = flavors

    def add_flavors(self):
        pass


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,*flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def add_flavors(self):
        flavor = []
        flavor.append(self.flavors)
        print(flavor)

my_old_restaurant = IceCreamStand('kfc',' chinese food','starberry icecream','origin icecream')
my_old_restaurant.add_flavors()



#9-7
class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = ["can add post","can delete post","can ban user"]

    def show_privileges(self,):
        for i in self.privileges:
            print("You " + i)


new_user = Admin('mu', 'ying', '22')
new_user.greet_user()
new_user.show_privileges()


#9-8
class Privileges():
    def __init__(self):
        self.privileges = ["can add post","can delete post","can ban user"]

    def show_privileges(self):
        for i in self.privileges:
            print("You " + i)

class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = Privileges()

new_user = Admin('mu', 'ying', '22')
new_user.greet_user()
new_user.privileges.show_privileges()

#9-9




