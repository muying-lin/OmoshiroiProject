car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
#5-3
alien_color = 'green'
if alien_color =='green':
    print('Player win 5 point')

#5-4
if alien_color =='green':
    print('Player win 5 point')
else:
    print('Player win 10 point')
#5-5


#5-6
age = 5
if age < 2:
    print('baby')
elif 2<=age<4:
    print('study wolk')
elif 4<=age<13:
    print('children')
elif 13<=age<20:
    print('teenage')
elif 20<=age<65:
    print('adult')
else:
    print('old man')

#5-7
favorite_fruits = ['apple','straberry','orange']
if 'apple' in favorite_fruits:
    print('You really like apple')
if 'straberry' in favorite_fruits:
    print('You really like straberry')
if 'orange' in favorite_fruits:
    print('You really like orange')
else:
    print('nothing you like')

#5-8
list_1 = ['admin','muying','luozheng','bailin','zhiping']
for i in list_1:
    if list_1 :
        if i == 'admin':
            print('“Hello admin, would you like to see a status report?”。')
        else:
            print('Hello ' + i + 'thank you for logging in again')
    else:
        print('We need to find some users!')


current_users = ['admin','muying','luozheng','bailin','zhiping']
new_users = ['admin','muying','guanbing','zhixuan','zhiping']

for i in new_users:
    if i.lower() in current_users:
        print(i + 'your name used')
    else:
        print(i + 'you can use name')

#5-11
list_2 = [x for x in range(1,10)]
for num in list_2:
    if num == 1:
        print(str(num)+'st')
    elif num == 2:
        print(str(num)+'nd')
    elif num == 3:
        print(str(num)+'rd')
    else:
        print(str(num) + 'th')

