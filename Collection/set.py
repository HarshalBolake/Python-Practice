myset = {"apple","banana","cherry","cherry"}
print(myset)

anotherset ={0,1.2,3,False,"apple"}
print(anotherset)

#access item
for x in myset:
    print(x)

print("apple" in myset)

#adding item
myset.add("orange")
print(myset)

#update
mylist = ["red","green","yellow"]
myset.update(mylist)
print(myset)

#remove
myset.remove("red")
print(myset)

#discard
myset.discard("redd")
print(myset)

#pop
myset.pop()
print(myset)


#clear
myset.clear()
print(myset)

del myset
# print(myset)