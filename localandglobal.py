#WAF to demonstrate local and global variables 
a = 10 
fact = 1
for i in range(1, a+1):
	fact = fact * i
print("The factorial of number 10 is : ", end="")
print(fact)

a = int(input("Write first number: "))
y = int(input("Write secound number: "))

def add(a,y):
    print(a + y)
    print("I am done with :")
def sub(a,y):
    print(a - y)
    print("I am done with :")
def mul(a,y):
    print(a * y)
    print("I am done with :")
def div(a,y):
    print(a / y)
    print("I am done with :")

add (a,y)
sub (a,y)
mul(a,y)
div(a,y)

