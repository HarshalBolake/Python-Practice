numbers = [1,2,3,4]      #numbers list
names = ["Harshal","John","Tom","Jack"] #string list
mixed = [1,"hello", True]      #mixed list


print(numbers[2])
print(names[0])
print(mixed[2])


#Accesing data
names[2] = "Jerry"
print(names)

#slicing same as string slicing
print(names[::-1]) #Reverse


#creating new list from list
a = [1,2,3,4,5,6,7,8,9,0]
b = a[0:5]
print(b)


#Example1
marks = [85,90,78,92,88]
top_marks = marks[:3]
print("Top 3: ", top_marks)

#Example2
numbers = [10,11,12]
for num in numbers:
    print(num)


#Example3
list1 = [10,20,30,40,50]
print(list1[0])
print(list1[-1])
print(list1[1:-1])
print(list1[::-1])






