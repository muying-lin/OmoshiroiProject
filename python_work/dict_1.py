alien_0 = {'color':'green','point':'5'}

print(alien_0['color'])
print(alien_0['point'])

info = {'first_name':'lin','last_name':'ziwei','age':23,'city':'fujian'}

name = {'admin':1,'muying':2,'luozheng':3,'bailin':4,'zhiping':5}
for keys,values in name.items():
    print(keys,values)

sea = {'nile':'egypt','':'','':''}
for keys,values in sea.items():
    print('The ' + keys.title() + ' runs through ' + values.title())

for i in sea.keys():
    print(i)
for x in sea.values():
    print(x)


#pizza.py
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
print("You odered a " + pizza['crust'] + "-crust pizza with the following toppings" )
for topping in pizza['toppings']:
    print("\t" + topping)


#字典嵌套列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name,languages in favorite_languages.items():
    print(name + 'favorite language is :')
    for language in languages:
        print(language)

#
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    }
}



#6-6

#6-7

info_1 = {'first_name':'lin','last_name':'ziwei','age':22,'city':'fujian'}
info_2 = {'first_name':'peng','last_name':'guangbing','age':25,'city':'fujian'}
info_3 = {'first_name':'wang','last_name':'zhiping','age':23,'city':'fujian'}
people = [info_1,info_2,info_3]
for i in people :
    print(i)
#6-8
nina = {'type':'cat','master':'muying'}
weiduo = {'type':'dog','master':'zhiyan'}

pets = [nina,weiduo]
for i in pets:
    print(i)

#6-9
favorite_places = {
    'muying':['fuzhou','shanghai','shenzhen'],
    'zhiyan':['dailin','changle','fuzhou'],
    'biwen':['chanle','xiusidun','riben'],
}

for name,values in favorite_places.items():
    print(name + ' favorite places:')
    for value in values:
        print(value)

#6-10
name = {'admin':[1,4,5,7,11],'muying':[2,3,5,9,12],'luozheng':[3,6,15,20],'bailin':[4,5,9],'zhiping':[1,5]}
for name,nums in name.items():
    print(name + '\'s like num is ' )
    for num in nums:
        print(num)

#6-11
cities = {
    'changle':
    {
        'country':'china',
        'population':'500w',
        'fact':'toudu',
    },
    'fuzhou':
    {
        'country':'china',
        'population':'1000w',
        'fact':'yiming',
    }
}
for keys,values in cities.items():
    print(keys + 'infomation: ')
    for i,x in values.items():
        print('the ' + i + ' is ' + x)
