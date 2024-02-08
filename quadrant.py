#WAP  to read an angle from user and then display its quadrant
def quad(degree):
    degree = int(input("Enter the number of degree: "))
    quad = int(input ("Enter the number of quadrant: "))
    if degree >= -45 and degree <= 45 :
        return "I"
    elif degree > 45 and degree <135 :
        return "II"
    elif degree >=135 and degree <= 180 :
        return "III"
    else :
        return "IV"
print(quad(90))