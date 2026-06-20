'''
area of triangle

a = int((input("Enter length of side a:")))
b = int((input("Enter length of side b:")))
c = int((input("Enter length of side c:")))

# semi-perimeter of triangle = s
s =( a + b + c) / 2

area = int(((s*(s-a)*(s-b)*(s-c))**0.5))
print("The area of the triangle is :" , area )




area of circle 
r = int(input("Enter the radius of the circle: "))
pi = 3.14

A = pi*(r)**2
print("The area of the circle is: " , A)




#area of square
# s = int(input("Enter the length of the side of the square: "))

# A = s**2
# print("The area of the square is : " , A )




# Write a Python program to check whether a given string is a number or not using Lambda.

st = lambda x : True if type(x) == str else False

print(st('Hello'))
print(st('ash123'))
print(st('123'))
print(st(234))





# Write a Python program to find the intersection of two given arrays using Lambda

arr_1 = [1, 2, 3, 5, 7, 8, 9, 10]
arr_2 = [1, 2, 4, 8, 9]

ints = list(filter(lambda x: x in arr_1 , arr_2))
print(ints)





#Write a Python program to count the even and odd numbers in a given array of integers using Lambda.

arr1 = [1, 2, 3, 5, 7, 8, 9, 10]

even_num = len(list(filter(lambda x : x%2 == 0 , arr1)))
odd_num = len(list(filter(lambda x :  x%22 != 0 , arr1)))

print("Even numbers in arr1 are :" , even_num)
print("Odd numbers in arr1 are :" , odd_num)
'''




#Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

days = list(filter(lambda x : len(x) == 6 , week))

print("Days with length of 6 are :" , days)

