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


#special methods
A = {1,2,3,4,5}
B = {4,5,6,7,8}

#intersection
print(A.intersection(B))

#difference
print(A.difference(B))

#union
print(A.union(B))

#ymmetric difference
print(A.symmetric_difference(B))



# del myset
# print(myset)


#loop through set
thisset = {"Ford","Hyundai","Farrari","BMW"}
for x in thisset:
    if(x is "Ford"):
        print("Ford Mustang")