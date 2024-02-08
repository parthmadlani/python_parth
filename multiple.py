#WAP to read two numbers. then find out whether the first number is a multiple of secound number
def multiple(): 
    x=int(input("Enter First Number: ")) 
    y=int(input("Enter Second Number: "))  
    if (x % y==0):  
        print ("%d is Multiple of %d" %(x,y));  
    else:    
        print ("%d is Not Multiple of %d" %(x,y)); 
multiple();