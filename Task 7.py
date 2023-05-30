#q1
print('q1')

name = ["Tarteel", "Asmaa", "Ahmed"]

name.insert(0, "Sabrin")
print(name)

name.pop()
print(name)

name.append("Hamda")
print(name)

del name[2]
print(name)

#q2
print('q2')
friends= ["Adel", "Ahmed"]
employees= ["Samah", "Amjad"]
school= ["Ali", "Basma"]
friends.extend(employees)
friends.extend(school)
print(friends)
#q3
print('q3')
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dict = {}
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

print(new_dict)
#q4
print('q4')
dict = {}
for i in range(1, 16):
    item = i ** 2

    dict[i] = item

print(dict)
#q5
print('q5')
d1={'a':100 , 'b':200 , 'c':300}
d2={'a':150 , 'b':200 , 'd':400}
new_dict = {}
for key in d1:
    if key in d2:
        new_dict[key] = d1[key] + d2[key]
    else:
        new_dict[key] = d1[key]

for key in d2:
    if key not in new_dict:
        new_dict[key] = d2[key]

print(new_dict)

#q6
print('q6')
keys=['ten' , 'twenty' , 'thirty']
values=[10,20,30]
my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print(my_dict)

#q7
print('q7')
sampelDict={
    "class":{
        "student":{
            'name': "maki",
            'marks':{
            "physics":70,
            "history":80
}

        }
    }
}

print(sampelDict['class']['student']['marks']['history'])
#q8
print('q8')
dic={1:"Alaa", 5:"Hadeel" , 7:"Hanin" , 13:"Malak"}
result = ""

for key in dic:
    if key < 10:
        result += dic[key] + "->"

result = result[:-2]

print(result)



