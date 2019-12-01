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
