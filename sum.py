'''
Date: 6/16/16
Programmer: Josué Mora
Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.
Problem from: https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
'''

#get numbers from list
l = [1,2,3]
n = len(l)
a = 0

# print sum using a for loop
def sum_for_loop():
	x = 0
	for item in l:
	   x += item
	return x

# print sum using a while loop
def sum_while():
	x = 0
	s = 0
	while n > 0:
	   s += l[x]
	   x += 1
	   n -= 1
	return s

# print sum using recursion
def sum_recursive(numbers,size):
   if size == 0:
     return 0
   else:
     return numbers[size-1] + sum_recursive(numbers,size-1)

# total = sum4loop()   
# total = sumwhile()
n = len(l)
total = sum_recursive(l,n) 

print total

# Program prints sum of integers in a list in 3 different methods. First method uses a for loop,
# second uses a while loop and the last one uses a recursive method

