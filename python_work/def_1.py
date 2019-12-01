def greet_user():
    print("hello")

def display_message():
    print("I study 定义函数，向函数传递信息，实参和形参")



def favorite_book(title):
    print("One of my favorite books is " +title.title()  + " in Wonderland" )

favorite_book('alien')

#8-3
def make_shirt(size,char):
    print("the shirt size is " + size)
    print("the shirt char is " + char)

make_shirt('L','fuck')
make_shirt(char='will good',size='M')

#8-4
def make_shirt(size,char='I love Python'):
    print("the shirt size is " + size)
    print("the shirt char is " + char)
make_shirt('M')
make_shirt('L')
#8-5
def describe_city(name,city='china'):
    print(name.title() + " is in " + city.title() + ".")

describe_city('chanle')
describe_city('daban','japan')
describe_city('fuzhou')

#让实参变成可选的
def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = first_name +' '+ middle_name +' '+ last_name
        print(full_name.title())
    else:
        full_name = first_name + ' ' + last_name
        print(full_name.title())

get_formatted_name('mu','ying')
get_formatted_name('lin','mu','ying')


#函数和while循环
def get_formatted_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print('\nEnter \'q\' at any time to quit. ')
    f_name = input("First name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break

    name1 = get_formatted_name(f_name,l_name)
    print("\nHello, " + name1 + '!\n')

#8-6
def city_country(city,country):
    full_1 = city + ',' + country
    return full_1.title()

name1 = city_country('changle','china')
name2 = city_country('daban','japan')
name3 = city_country('xiusidun','Asia')
print(name1)
print(name2)
print(name3)

#8-7
def make_album(singer,special_edition,num=''):
    if num:
        dict_1 = {'singer':singer,'special_edition':special_edition,'num':num}
    else:
        dict_1 = {'singer':singer,'special_edition':special_edition}
    return dict_1

num1 = make_album('cenninger','live','5')
num2 = make_album('Edson','suiyue')
print(num1)
print(num2)

#8-8
def make_album(singer,special_edition,num=''):
    dict_2 = {'singer': singer, 'special_edition': special_edition}
    return dict_2
while True:
    print('input your like:')
    print('Enter \'q\' at any time')

    s = input('singer name:')
    if s == 'q':
        break

    s_edition = input('special_edition name:')
    if s_edition == 'q':
        break

    num3 = make_album(s,s_edition)
    print(num3)

#8-9
magicians = ['yuqian','liuqian','yuhua']
def show_magicians(names):
    for i in names:
        print(i)

name = show_magicians(magicians)

#8-10

magicians = ['yuqian','liuqian','yuhua']
new_magicians = []
def show_magicians(names):
    for i in names:
        i ='the Great ' + i
        new_magicians.append(i)

name = show_magicians(magicians)
print(new_magicians)

#8-11

def make_pizza(*toppings):
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping)

make_pizza('pepperoni')
make_pizza('mush','green peppers','extra cheese')


#8-12
#三明治：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个 函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点 的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。
def material(*datas):
    print('you need food: ')
    for i in datas:
        print(' - ' + i)

material('beef','meal')

#8-13

def build_profile(first, last, **user_info):

    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('mu','ying',location='fujian',field='math')
print(user_profile)

#8-14
def make_car(mfrs,type,**user_info):
    info = {}
    info['mfrs'] = mfrs
    info['type'] = type
    for keys,values in user_info.items():
        info[keys] = values
    return info

car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)

#8-15

