x = "10"
y = int(x)
print(y + 10)

#Types of Type Casting 
#Implicit(Automatic)
x = 10
y = 2.5

Result = x + y
print(Result)

#Explicit(Manually)
#functions -> int(), float(), str(), list(), tuple(), set()

#int(),float(),str()
x = "100"
y = int(x)
print("Variable", y ,"is", type(y))

age = 20
print("Age:"+ str(age));



#list(), tuple(), set()
x = "hello"
y = list(x)
print(y);



#dict()
x = [("a",1), ("b",2), ("c",3)]
y = dict(x)
print(y)


#Bool casting
bool(0) #False
bool(1) #True
bool("") #False
bool("hello") #True
bool([]) #False
bool([1,2]) #True



#Error
# x = "10"
# y = int(x)
# print(x + y)




