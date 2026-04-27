age = 18


#if - else
if age >= 18:
    print("Adult")
else:
    print("Minor")


#if,elif,else
marks = 75

if marks >= 90:
    print("A Grade")
elif marks >= 70:
    print("B Grade")
elif marks >= 50:
    print("C Grade")
else:
    print("Fail")




# Nested - if - else
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
    else:
        print("ID Required")
else:
    print("Not Allowed")



# Ternary Operators
age = 18

result = "Adult" if age >= 18 else "Minor"
print(result)



#Example
marks = int(input("Enter your marks:"))

if marks >= 90:
    print("A")
elif marks >= 75: 
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

#Advanced
grade = (
    "A" if marks >= 90 else
    "B" if marks >= 75 else
    "C" if marks >= 50 else
    "Fail"
)
print(grade)



# Loops
# range(start, stop, range)
for i in range(3):
    print("Hello")


#types: for loop, while loop
for i in range(4):
    print(i)

for i in range(1,10,2):
    print("Numbers:",i)




#loop through list
fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    print(fruit)


#while loops
i = 1
while i <= 5:
    print(i)
    i+=1


#break
for i in range(20):
    if i == 5: 
        break
    # print(i)


#continue
for i in range(10):
    if i == 5:
        continue
    # print(i)


#pass
for i in range(5):
    if i == 2:
        pass
    print(i)




#else with loop (runs when loop finish)
for i in range(3):
    print(i)
else:
    print("Done")




#nested loops
for i in range(3):
    for j in range(3):
        print(i,j)


#Example1
total = 0
for i in range(1,6):
    total += i
print("sum:",total)


#Example2
for i in range(1,10):
    if i % 2 == 0:
        print(i) 


#Example3
secret = 5
while True:
    guess = int(input("Guess number: "))

    if guess == secret:
        print("Correct")
        break
    else:
        print("Try again")


