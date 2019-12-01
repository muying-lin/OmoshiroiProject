#7-1
how = input('what are you need bus?')
print("Let me see if I can find you a " + how)

#7-2
how_people = int(input('how much people have lunch?'))

if how_people > 8:
    print(' It\'s not available for the moment.')
else :
    print('please')

#7-3
num = int(input('input a number:'))
if num % 10 == 0:
    print('the number is 10 的倍数')
else :
    print('cant')


#parrot.py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

#当条件多个的时候 （标志）设置一个变量active= True 进行判断 如果进行到不满足情况的条件就active = False

#7-4
prompt = "\nPlease tell me something, and I will add it"
prompt += "\nEnter 'quit' to end the program. "

food = True
while food:
    message = input(prompt)
    if message == 'quit':
        food = False
    else :
        print("We will add " + message)

#7-5
prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    elif int(message) < 3:
        print("free")
    elif 3 <= int(message) <= 12 :
        print("10 dollor")
    else :
        print("15 dollor")

#7-8
sandwich_oders = ['tunafish','meatball_sub','italian','reuben']
finished_sandwich =[]

for i in sandwich_oders:
    print('I made your '+ i +' sandwich.')
    finished_sandwich.append(i)
print(finished_sandwich)

#7-9

sandwich_oders = ['tunafish','meatball_sub','italian','reuben','pastrami','pastrami','pastrami']

print("We sell out of pastrami")
while 'pastrami' in sandwich_oders:
    sandwich_oders.remove('pastrami')

print(sandwich_oders)

#7-10
prompt = ("\nIf you could visit one place in the world, where would you go?")
prompt += "\nEnter 'quit' to end the program. "

best_city = []
active = True
while active:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I want to go to " + city +' most.')
        best_city.append(city)
print(best_city)

