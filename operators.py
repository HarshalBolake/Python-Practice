#Operators
#Arithmetic Operators (+ Addition, - subtraction, * multiplication, / division, // floor division, % modulus, ** power)

a, b = 11,2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

if a % 2 == 0:
    print("Even")
else:
    print("Odd")




#Comparison Operator (== equal, != not equal, > grater, < less, >= grater equal, <= less equal)
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


if a >= 18:
    print("Eligible")
else:
    print("Not eligible")




#Logical Operators (and = both true , or = at least one true , not = reverse)
age = 20
has_id = True
if age >= 18 and has_id:
    print("Allowed")



#Assignment operators (+= , -= , *= , /=)  
x = 10
x *= 5
print(x)



#Membership Operators (in , not in)
name = "Harshal"
print("H" in name)
print("Q" in name)

fruits = ["apple", "banana"]
if "apple" in fruits:
    print("apple available")



#Identity Operators (is, is not)
a = [1, 2]
b = a
c = [2, 3]
print(a is b)
print(b is c)



