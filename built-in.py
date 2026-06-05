name = "Harshal"
print(len(name))

nums = [10,20,30,15,20]
print(sum(nums))
print(sum(nums,10))  #start value

print(max(nums))
print(min(nums))
print(sorted(nums))
print(sorted(nums, reverse= True))


#Enumerate
fruits = ["apple","banana","kiwi"]
for i in range(len(fruits)):
    print(i,fruits[i])


print("with enumerate()")
for i, fruits in enumerate(fruits,start=1):
    print(i, fruits)


names = ["Alex","John"]
ages = [20,22]
result = zip(names,ages)
print(list(result))

for name,age in zip(names,ages):
    print(name, age)


nums = [False, False, False]
print(any(nums))

print(all(nums))