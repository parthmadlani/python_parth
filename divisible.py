#WAP to check wheather given number is divisible by 3 or 5 and 3 and 5
num = int(input("Enter a number: ")) 
if (num % 3 == 0) & (num % 5 == 0):
    print("%d is divisible by both 3 and 5" % num) 
elif (num % 3 == 0): 
    print("%d is divisible by 3" % num)  
elif (num % 5 == 0):  
    print("%d is divisible by 5" % num)   
else:  
    print("%d is not divisible by 3 or 5" % num)