#Creating A simple calculator
print("What do you like to calculate")
print(" 1. sumation")
print(" 2. Substarct")
print(" 3. Multiplication")
print(" 4. Division")
print(" 5. Exponential")
print(" 6.  Modulation")


print(" ENTER FIRST NUMBER")
a=int(input())

print(" ENTER SECOND NUMBER")
b=int(input())

print(" Choese Your Option")
x=int(input())
def sum():
    print(a+b)

def sub():
     print(a-b)

def mult():
     print(a*b)

def div():
     print(a/b)

def exp():
     print(a**b)

def mod():
     print(a%b)


if x==1:
    sum()
    

if x==2:
    sub()
    

if x==3:
    mult()
    

if x==4:    
    div()
    

if x==5:
    exp()
  
if x==6:
    mod()
    
if (1<x>6):
    print(" Wrong Option")
    






