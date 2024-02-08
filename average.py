#Write a function to determine an average of given numbers in arguments
def avgfun(*n):
	sums = 0
	for t in n:
		sums = sums + t
	avg = sums / len(n)
	return avg
result1 = avgfun(1, 2, 3)
result2 = avgfun(2, 6, 4, 8)
print(round(result1, 2))
print(round(result2, 2))

 
 


