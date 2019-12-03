
#相对路径
with open('../pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#绝对路径
file_object_1 = '/Users/muying/PycharmProjects/OmoshiroiProject/pi_digits.txt'
with open(file_object_1) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#逐行读取
filename = '../pi_digits.txt'
with open(filename) as file_object:
    for i in file_object:
        print(i.rstrip())

#创建一个包含文件各行内容的列表
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#使用文件的内容
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))


pi_string_1 = ''
for line in lines:
    pi_string_1 += line.strip()

print(pi_string_1)
print(len(pi_string_1))

#10-1
filename = '../learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

with open(filename) as file_object:
    for i in file_object:
        print(i.rstrip())

with open(filename) as file_object:
    contents = file_object.readlines()

pi_string_2 = ''
for x in contents:
    pi_string_2 += x

print(pi_string_2)
#10-2
pi_string_3 = "In Python you can study English"
pi_string_3.replace('Python','C')
print(pi_string_3)

#10.2.1写入空文件
filename = '../programing.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programing!\n")
    file_object.write("I love creating new games.\n")

#10.2.2写入多行


#10.2.3附加到文件
filename = '../programing.txt'

with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

#10-3
name = '../guest.txt'

with open(name,'w') as file_object:
    write = input("input your name")
    if write != '':
        file_object.write(write+'\n')

#10-4
name = '../guest_book.txt'

with open(name,'w') as file_object:
    while True:
        wri = input("whats your name?")
        if wri == 'q':
            break
        print("Enter 'q' to end the program")
        print("Hello " + wri)
        file_object.write(wri+'\n')


#10-5

name = '../reason.txt'

with open(name,'a') as file_object:
    while True:
        reason = input("why are you like programming?")
        if reason == 'q':
            break
        file_object.write(reason+'\n')


#10.3异常
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

try:
    first_num = input("input your num:")
    last_num = input("input your second num:")
    print(first_num +' / ' + last_num + ' = '  + int(first_num)/int(last_num))
except ZeroDivisionError:
    print("You cant divide by zero")

#10.3.4 else代码块 try-except-else
