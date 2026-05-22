mytuple = ("apple","banana","cherry")

mytupleduplicatevalues = ("apple","banana","cherry","cherry")

print(mytuple)
print(mytupleduplicatevalues)

#finding length
print(len(mytuple))

mytuplewithonevalue = ("apple",)
print(type(mytuplewithonevalue))

mytupledatatype = ("apple",3,2.4)
print(mytupledatatype)

#accesing tuple items
print(mytuple[1])
print(mytuple[:2])
print(mytuple[-1:])

#update tuple
mytupleupdated = list(mytuple)
mytupleupdated[1] = "orange"
mytuple = tuple(mytupleupdated)
print(mytuple)
print(type(mytuple))


#add items
mytupleadditem = list(mytuple)
mytupleadditem.append("kiwi") 
mytuple = tuple(mytupleadditem)
print(mytuple)
print(type(mytuple))


#adding two tuples
firsttuple = ("Apple","Orange")
secondtuple = ("Banana","Kiwi")
firsttuple += secondtuple
print(firsttuple)


#remove item
removeditemtuple = list(mytuple)
removeditemtuple.remove("apple")
mytuple = tuple(removeditemtuple)
print(mytuple)


#delete tuple
del removeditemtuple
# print(removeditemtuple) #deleted

#unpacking tuple
packtuple = ("red","green","yellow","orange","purple") #packing
(apple,*banana,kiwi) = packtuple

print(apple)
print(banana)
print(kiwi)

#loop tuple
for i in mytuple:
    print(i)


#multiply tuple
multiplytuple = mytuple * 2
print(multiplytuple)


#count()
print(mytuple.count("apple"))
print(packtuple.index("purple"))