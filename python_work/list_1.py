magicians = ['alian','david','carolian']
for magician in magicians:
    print(magician)

#4-1

pizzas = ['seafood_pizza','cheese_pizza','beef_pizza']
for pizza in pizzas:
    print(pizza)
    print('I like ' + pizza+'\n')

print('I really love pizza!')

animals = ['cat','dog','rabbit']
for animal in animals:
    print(animal)
    print('A ' + animal + ' would make a great pet\n')
print('Any of these animals would make a great pet!')

for i in range(1,21):
    print(i,end='')

#4-4
num = []
num_list = [i for i in range(1,1000001)]


print(min(num_list))
print(max(num_list))
print(sum(num_list))

#4-6
num_1 = [i for i in range(1,21,2)]
print(num_1)
for x in num_1:
    print(x)

#4-7
num_2 = [i for i in range(0,31,3)]
print(num_2)

#4-8
num_3 = [i**3 for i in range(1,11)]
print(num_3)

print("The first three items in the list are:"+ str(num_3[:3]))
print("The last three items in the list are:"+ str(num_3[-3:]))
print("Three items from the middle of the list are:")

#4-11
friend_pizza = pizzas[:]
pizzas.append('choose_pizza')
friend_pizza.append('reef_pizza')
print('My favorite pizzas are:')
for i in pizzas:
    print(i)

print('my friend\'s favorite pizzas are:')
for x in friend_pizza:
    print(x)

#4-12

###拷贝副本得用切片方式 不能直接相等 friend_pizza = pizzas[:]
###浅拷贝和深拷贝