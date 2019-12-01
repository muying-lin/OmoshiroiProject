message = "hello wolrd"
print(message)
name = "muying"
print(name.lower())
print(name.upper())
famous_person = "Albert Einstein"
message = '“A person who never made a mistake never tried anything new.”'
print(famous_person + " once said, "+ message)
name = '\n   muying       \t'
print(name.lstrip())
print(name.rstrip())
print(name.strip())

print(11-3)
print(40/5)
print(5+3)
print(2*4)

name = ['xiaowan','xiaohong','xiaoming']
print(name)
print(name[1])
print(name[2])
print(name[0])
print(name[0] + message)
print(name[1] + message)
print(name[2] + message)

#插入值有insert，append
#变量名.insert(索引值，值) append加到末尾
name.pop(0)
#pop不能指定列表值删除，remove可以，del +变量名+索引 永久删除的
name.remove('xiaohong')
print(name)


#3-4
invite_name = ['biwen','zhiyan','weipo','waigong']
message = 'Can you have lunch with me ?'
print(invite_name[0] +','+ message)
print(invite_name[1] +','+ message)
print(invite_name[2] +','+ message)
print(invite_name[3] +','+ message)



#3-5
print(invite_name[3] + 'cant have lunch with me.')
invite_name.remove('biwen')
invite_name.insert(3,'yeye')
print(invite_name)
print(invite_name[3] +','+ message)

#3-6
print('I found a big desk.')
invite_name.insert(0,'nainai')
invite_name.insert(3,'tailaolao')
invite_name.append('tailaoye')
print(invite_name)
print(invite_name[0] + message)
print(invite_name[1] + message)
print(invite_name[2] + message)
print(invite_name[3] + message)
print(invite_name[4] + message)
print(invite_name[5] + message)
print(invite_name[6] + message)

#3-7
invite_name.pop()
invite_name.pop()
invite_name.pop()
invite_name.pop()
invite_name.pop()
print("I'm so sorry,because my desk cant at time at here.")
print("so" + invite_name[0] +' ' + invite_name[1] + ' have lunch wite you')

del invite_name[0]
del invite_name[0]
print(invite_name)

#3-8
want_place = ['chongqing','sichuang','shanghai','shenzhen','guangzhou']

print(sorted(want_place))
print(want_place)
print(sorted(want_place,reverse=True))
print(want_place)

want_place.reverse()
print(want_place)
want_place.reverse()
print(want_place)

#3-9
invite_name = ['biwen','zhiyan','weipo','waigong']
print('I ask '+ str(len(invite_name)) + ' for lunch')

