#simple decorators
def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner

@changecase
def myfunction(nam):
    return "Hello " + nam

# print(myfunction("harshal"))



#decorator with argument
def changecase(n):
    def changecase(func):
        def myinner(x):
            if n == 1:
                a = func(x).lower()
            else:
                a = func(x).upper()
            return a
        return myinner
    return changecase

@changecase(0)
def myfunction(name):
    return "Hello "+ name

# print(myfunction("harshal"))


#multiple decorators
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addGreet(func):
    def myinner():
        return "Hello "+ func()+ " Have a good day!"
    return myinner

@changecase
@addGreet
def myfunction():
    return "Harshal"

print(myfunction())

