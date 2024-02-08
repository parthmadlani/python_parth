#WAP to find the roots of quadratic equation ax2+bx+c using cmath library
import cmath
a = 1
b = 4
c = 2
dis = (b**2) - (4 * a*c)
ans1 = (-b-cmath.sqrt(dis))/(2 * a)
ans2 = (-b + cmath.sqrt(dis))/(2 * a)
print('The roots are')
print(ans1)
print(ans2)

