thisdict = {
    "brand":"Ford",
    "name":"Mustang",
    "year":1964
    
}

print(thisdict["brand"])

print(len(thisdict))


#dict containing list
cars = {
    "brand":"Ford",
    "electric":False,
    "colors":["Red","white","Black"]
    }


#print key values
keys = cars.keys()
print(keys)
values = cars.values()
print(values)


#add item
cars["price"] = 200000
print(cars)

#update item
cars["price"] = 250000
cars.update({"country":"United States"})
print(cars)

#print every item in dict
print(cars.items())

#remove item
cars.pop("price")
print(cars)

#remove lat inserted
cars.popitem()
print(cars)


#delete value
del cars["brand"]
print(cars)

#clear whole dict
cars.clear()
print(cars)

#loop through dict
personal = {
    "name":"Harshal",
    "age":22,
    "course":"Software Engineering",
    "Passed":True
}

for x in personal:
    print(x)
    print(personal[x])

for x in personal.keys():
    print(x)

for x,y in personal.items():
    print(x,y)


#nested dictonaries
family = {
    "child1":{
        "name":"John",
        "age":18
    },
    "child2":{
        "name":"Tom",
        "age":20
    },
    "child3":{
        "name":"Jerry",
        "age":22
    }
}

print(family["child1"]["name"])

print("Hello")
for x, y in family.items():
    print(x)
    for i in y:
        print(i+":",y[i])