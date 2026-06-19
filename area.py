'''

a = float(input('enter side 1 = '))
b = float(input('enter side 2 = '))
c = float(input('enter side 3 = '))

#semi perimeter of triangle
s = ( a + b+ c)/2

#area of triangle
A = (s*(s-a)*(s-b)*(s-c))**0.5

print("the area of triangle is %0.3f" , A ) 

import random
print(random.randint (0,1000))

from pint import UnitRegistry

# Initialize the unit registry
ureg = UnitRegistry()

# Define the initial measurement
distance_km = 20 * ureg.kilometer

# Convert it to miles
distance_miles = distance_km.to(ureg.mile)

print(distance_miles) 
# Output: 6.21371192237334 mile


# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
celsius = 37.5

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

a = float(input('enter a nummber : '))
if a>=0:
   print("number is positive")
elif a==0:
   print("zero")
else :
   print("number is negative")
   
num = int(input(" enter a number: "))
if num % 2 == 0:
   print("{0} is even".format(num))
else:
   print("{0} is odd".format(num))
   
a = int(input("enter a year : "))
if (a % 400 ==0 ) and (a % 100 == 0 ):
    print("{0} is a leap year". format(a))
elif ( a % 4 ==0 ) and (a % 100 != 0 ):
    print("{0} is a leap year".format(a))
else :
    print("{0} is not a leap year".format(a))
    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1>=num2) and (num1>=num3):
    largest = num1
elif (num2>=num1) and (num2>=num3):
    largest = num2
else:
    largest = num3
print("the largest number is " ,largest)    
   
num = int(input("enter a number : "))
flag = False

if num==0 or num==1:
   print(num , "num is not a prime number")
elif num>1:
    for f in range(2 , num):
        if (num % f ) == 0:
            flag = True
            break #break of loop

if flag :
   print(num , "is not a prime number")
else :
     print(num , "is a prime number") 

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
   
num = int(input("enter a number : "))
factorial = 1

if num<0:
    print("foctorial does not exist for negative numbers")
elif num==0:
    print("factorial of 0 is 1")
else :
    for i in range (1,num + 1):
        factorial = factorial*i
    print("The factorial of" , num , "is" , factorial )
    
num = int(input("enter a number : "))
#Iterate 15 times from i=1 to 15
for i in range(0,16):
    print(num , "x" , i , "=" , num*i)

nterms = int(input("how many terms?"))
n1 , n2 = 0 , 1
count = 0

if nterms<=0:
    print("please enter a positive number")
elif nterms==1:
    print("fibonacci sequence upto" , nterms , ":")
    print(n1)
else :
    print("fibonacci sequence")
    while count<nterms:
        print(n1)
        nth = n1 + n2
        
        n1 = n2
        n2 = nth
        count+=1
        
num = int(input("enter a number = "))
sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
    
if num==sum:
    print(num , "is an armstrong number")
else :
    print(num , "is not an armstrong number")

lower = 100
upper = 2000

for num in range ( lower , upper + 1 ):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digits = temp % 10
        sum+= digits ** order
        temp //= 10
        
        if num == sum:
            print (num)

num = int(input("enter a number : "))

if num < 0:
    print("enter a postive number")
else :
    sum = 0
    while (num > 0):
        sum += num
        num -= 1
    print("The sum is" , sum )

terms = 11

result = list(map(lambda x : 2**x , range(terms)))

print("The total terms are" , terms )
for i in range(terms):
    print("2 raised to power" , i , "is" , result[i])
# Take a list of numbers
my = [ 13 , 26 , 543 , 863 ]

result = list(filter(lambda x : (x%13==0) , my ))

print("the numbers divisible by 13 are " , result )

   
dec = 180

print("the value of decimal" , dec , "is :")
print(bin(dec) , "in binary")
print(oct(dec) , "in octal")
print(hex(dec) , "in hex")

y = 'z'

print("The ASCII code for'" + y + "'is" , ord(y))

#hcf

def compute_hcf(x,y):

#smaller number choose karna hai 
    if x>y:
        smaller = y
    else :
        smaller = x 
    for i in range( 1 , smaller + 1 ):
        if ((x%i == 0 ) and ( y%i==0)):
            hcf = i
    return hcf
        
num1 = 54
num2 = 24   
print("The HCF is" , compute_hcf(num1 , num2))
 
#lcm    

def compute_lcm(x,y):

    if x>y:
       greater=x
    else:
       greater = y        

    while(True):
        if(( greater%x == 0) and (greater%y == 0 )):
            lcm = greater
            break
        greater += 1
        
    return lcm
num1 = 54
num2 = 24
print("The LCM is" , compute_lcm(num1 , num2 ))

#factors of a number 

def factors(x):
    
    print("The factors of" , x , "are:")
    for i in range(1 , x + 1 ):
        if x%i == 0:
            print( i )
num = 512
factors(num)

# simple calculator 
def add(x,y):
    return x + y
 
def subtract ( x , y ):
    return x - y
    
def multiply ( x , y ):
    return x*y
    
def divide ( x , y ):
    return x/y

print("select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice (1,2,3,4):")
    
    if choice in ('1','2','3','4',):
        try :
            num1 = float(input("enter a number: "))
            num2 = float(input("enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
            
        if choice == '1':
            print(num1 , "+" , num2 , "=" , add(num1 , num2 ))
            
        elif choice =='2':
            print(num1 , "-" , num2 , "=" , subtract(num1 , num2))
            
        elif choice == '3':
            print(num1 , "*", num2 , "=" , multiply(num1 , num2))
            
        elif choice == '4':
            print(num1 , "/" , num2 , "=" , divide(num1 , num2))
            
        next_calculation = input("Next calculation? : (yes/no)")
        if next_calculation == "no" :
            break
    else :
        print("Invalid input")

import itertools , random

deck = list(itertools.product(range(1,14), [ 'Spade' , 'Club' , 'Diamond' , 'Hearts']))
random.shuffle(deck)

print("You got : ")
for i in range (5):
    print(deck[i][0] , "of" , deck[i][1] )

# display calendar of the given month and year

import calendar


yy = int(input("Enter year: "))
mm= int(input("Enter month: "))

print(calendar.month(yy, mm))


def fibo(n):
    if n<=1:
        return n
    else:
        return( fibo(n-1) + fibo(n-2))
        
nterms = 10
if nterms<=0:
    print("Please enter a positive number")
else:
    print("Fibonacci sequence: ")
    for i in range(nterms):
        print(fibo(i))



def recur_sum(n):
    if n<=1:
        return n
    else:
        return n + recur_sum(n-1)
        
num = int(input("Enter a number:"))
if num<0:
    print("Please enter a positive number")
else:
    print("The sum is" , recur_sum(num))



def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = int(input("enter a number: "))

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))


# Function to print binary number using recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = 4

convertToBinary(dec)
print()



X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

for row in X:
    print(X)

 
# Program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(X)):
  
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for sin result:
    print(s)


# transpose of matrix

X = [[ 12 , 5],
    [ 6 , 4 ],
    [ 81,9]]
    
    
result = [[ 0,0,0],
         [ 0,0,0]]
  
for i in range(len(X)):
    for j in range(len(X[0])):
        result[j][i] = X[i][j]
for y in result:
    print(y)

import numpy as np

my = np.array([12 ,48 , 7 ])

result = my + 2
print(result)



# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)

# palindrome

my_str ="fhcGIDKYSFhdhs"

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("the string is palindrome")
else:
    print("the string is not palindrome")


# define punctuation
punctuations = !()-[]{};:'"\,<>./?@#$%^&*_~

my_str = "Hello!!!, he said ---and went where @%^&&H$^&E wanted to."

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

print(no_punct)


# Program to sort alphabetically the words form a string provided by the user

my_str = "Hello this Is an Example With cased letters"

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)


# Program to perform different set operations like in mathematics

E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};

# set union
print("Union of E and N is",E | N)

# set intersection
print("Intersection of E and N is",E & N)

# set difference
print("Difference of E and N is",E - N)

# set symmetric difference
print("Symmetric difference of E and N is",E ^ N)


# Program to count the number of each vowels

# string of vowels
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)


rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()
    


my_list = [ 1 , 2, 3, 4, 5, 7]

print(my_list[0:5])



my_list = [ 1 , 2, 3, 4, 5, 7]

print(my_list[:])


my_list = [ 1 , 2, 3, 4, 5, 7]

print(my_list[:3])


# Creating a dictionary of a smartphone
phone = {
    "brand": "Apple",
    "model": "iPhone 15",
    "year": 2023,
    "colors": ["Black", "Blue", "Silver"]
}


print(phone["year"])


# merging dictionaries

dict_a = { 'a':1 , 'b':5 }
dict_b = { 'p':1 , 'c':9 }

print({**dict_a , **dict_b})


# print index of list with its's elements

my = [ 8 , 24 , 17 ,99,18 ]

for index , value in enumerate(my):
    print( index , value )
 

# start the index with non_zero

my = [ 8 , 24 , 17 ,99,18 ]

for index , value in enumerate(my, start=5):
    print(index , value )


my_list = [21, 44, 35, 11]

for index in range(len(my_list)):
    value = my_list[index]
    print(index, value)

my_list = [ [1] , [2,4,6,8] , [ 3,5,7,9]]

flatten_list = [ n for sublist in my_list for n in sublist ]
print(flatten_list)

my_list = [ [1] , [2,4,6,8] , [ 3,5,7,9]]

flatten_list = []

for sublist in my_list:
    for n in sublist:
        flatten_list.append(n)
print(flatten_list)

        
# slicing lists 

my_list = [ 2,4,6,8,10,12,14,16,18,20 ]

print( my_list[2:7])


my_list = [ 2,4,6,8,10,12,14,16,18,20 ]

print( my_list[::3])


my_list = [ 2,4,6,8,10,12,14,16,18,20 ]
print( my_list[2:7:3])


my_dict = {'y':'coffee' , 'a':'burger' , 's': 'pizza' , 'h':'coke'}

for keys , values in my_dict.items():
    print(keys , values )
 

my_dict = {'y':'coffee' , 'a':'burger' , 's': 'pizza' , 'h':'coke'}

for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)


my_list = ["yash","kumawat"]

if not my_list :
    print("The list is empty")
else:
    print("the list is not empty")


my_list = []

if not my_list :
    print("The list is empty")
else:
    print("the list is not empty")


my_list = []

if not my_list :
    print("The list is empty")


my_list = [ "yash"]
if not len(my_list):
    print("the list is empty")
else:
    print("the list is not empty" , my_list)


my_list = []

if my_list == []:
    print("the list is empty")
else:
    print("the list is not empty" , my_list)


# concatenate two lists 

yash = [ "main" ]
ash = [ "hoon" ]

final_list = yash + ash
print(final_list)


a_list = [ 4 , 'a' , "I am" , 42 ]
b_list = range(46,57)

final_list = [ *a_list , *b_list]
print(final_list)



customers = [ 1,2,3,4,5]
prices = [ 81 , 24 , 60 , 230 , 95 ]

prices.extend(customers)
print(prices)


# to check if a key is in the dictionary or not
yash = { 'gill':46 , 'kohli':89 , 'rohit':89 }

if "rohit" in yash:
    print("present")
else:
    print("not in the dictionary")
    


def split( list_a , chunk_size ):

    for i in range(0, len(list_a) , chunk_size ):
        yield list_a[i : i+chunk_size]
    
chunk_size = 2
my_list = [ 1,2,3,4,5,6,7,8,9]
print(list(split(my_list , chunk_size)))

    
import numpy as np

my_list = [ 1,2,3,4,5,6,7,8,9]

final_list =  np.array_split(my_list , 5)
print(final_list)



# conversion of one datatype into another , only if it's valid

a = "32"
t= int(a)
print( a , type(t))


yash = "78.45678"
yash_int = int(float(yash))
print( yash_int , type(yash_int ))


import colorama
colorama.init()

print('\x1b[38;2;5;86;243m' + 'Yash' + '\x1b[0m')

# Define styling configurations
GREEN_TEXT = "\x1b[32m"
YELLOW_BG = "\x1b[43m"
BOLD = "\x1b[4m"
RESET = "\x1b[0m"

# Combine styles fluidly inside a standard f-string
print(f"{BOLD}{GREEN_TEXT}Success!{RESET} Operation completed.")





BOLD = "\x1b[1m"
MY_BLUE = "\x1b[38;2;5;86;243m"
RESET = "\x1b[0m"

# Execute your styled string combination
print(f"{BOLD}{MY_BLUE}Successfully rendering Bold and Truecolor Blue on Win64 CMD!{RESET}")


from datetime import datetime

today = datetime.now()
print("time- " , today)


from datetime import date 

timestamp = date.fromtimestamp(14182940)
print(timestamp)                            # command terminal negative number pe error bataega 

 


from datetime import datetime 

my_date_string = "Jul 17 2005 06:30PM"
datetime_object = datetime.strptime(my_date_string , '%b %d %Y %I:%M%p')

print(type(datetime_object))
print(datetime_object)


my_list = [ 1 , 2 , 'a' , 'b' ,'m' ]

print(my_list[-1])


my_str = "Maybe i love myself"

print(my_str[6:20])
print(my_str[17])
print(my_str[2:19:3])


print("What are you doing?")
print()
print("who are")
print("you")
print()
print("am I", end = " " )
print("myself??")



import random

my_list = [1, 'a', 32, 'c', 'd', 31]
print(random.choice(my_list))


import secrets

my_list = [ '1', 't', 'f', '6' ]

print(secrets.choice(my_list))


# if a string is a number(float)

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False 
        
print(isfloat('1f23'))
print(isfloat('48.2'))
print(isfloat('17')) 
       


my_list = ['a', 1, 'a', 4, 3, 2, 'a']
freq = my_list.count('a')
print(freq)


marks = { 'Chemistry' : 84 , 'Physics' : 89 , 'Math' : 97 }

element = marks.pop('Chemistry')
print(marks)


my_dict = { 'Ashish': 32 , 'Bhuvan': 34 , 'Carry': 45}

del my_dict['Bhuvan']
popped = my_dict.pop('Carry')
print(popped)
print(my_dict)



my_str = """The itsy bitsy spider climbed up the waterspout.
Down came the rain and washed the spider out.
Out came the sun and dried up all the rain,
And the itsy bitsy spider climbed up the spout again!"""

print(my_str)



import time

start = time.time()

print(24*54*85*72*91*2*5*7)

end = time.time()

print(end - start )



import time

# Save timestamp
start = time.time()

print(23*2.3)

# Save timestamp
end = time.time()

print(end - start)



from timeit import default_timer as timer

start = timer()

print(24*48.2*2.6*28.495678*2.3*8.7*16.6*29.85*46.863)

end = timer()

print(end - start)


string = input("enter a string: ")

try:
    num = int(input("enter a number: "))
    print(string + num )
    
except (TypeError, ValueError) as e:
    print(e)



# sort a dictionary by value

my_dict = { 5:4 , 8:7 , 10:9 , 3:1 , 6:2 }

sorted_dict = { key: value for key,value in sorted(my_dict.items() , key = lambda item : item[1] )}

print(sorted_dict)



my_dict = { 5:4 , 8:7 , 10:9 , 3:1 , 6:2 }

sorted_values = sorted(my_dict.values())
print(sorted_values)



my_dict = { 5:4 , 8:7 , 10:9 , 3:1 , 6:2 }
sorted_keys = sorted(my_dict.keys())
print(sorted_keys)



from datetime import datetime

abhi_ka_time = datetime.now().time()
print(abhi_ka_time)


from datetime import datetime

my_date = "Jul 17 2005 18:30PM"

new_style = datetime.strptime( my_date , '%b %d %Y %H:%M%p')

print(new_style)


# converting multiple lists into dictionary

hobbies = [ 'cricket' , 'acting' , 'direction' , 'writing' , 'photography' , 'videography' ]
classes = [ 4 , 7 , 9 , 11 , 10 , 12 , 19 , 25 , 86 , 19 ]

my_dict = dict(zip(hobbies , classes ))
print(my_dict)



hobbies = [ 'cricket' , 'acting' , 'direction' , 'writing' , 'photography' , 'videography' ]
classes = [ 4 , 7 , 9 , 11 , 10 , 12 , 19 , 25 , 86 , 19 ]

my_dict = { k:v for k ,v in zip(hobbies , classes)}
print(my_dict)


def names():
    return "Yash" , "Manas" , "Jatin"
    
print(names()) 


def names():
    return "Salil" , "Bhuvan" , "Ashish"
    
print(names())

name_1 , name_2 , name_3 = names()
print(name_1 , name_2 , name_3)  

# to return multiple values from a function using dictionary

def name():
    n1 = "Ashish"
    n2 = "Bhuvan"
    n3 = "Salil"
    n4 = "Yash"
    
    return{1:n1 , 2:n2 , 3:n3 , 4:n4 }
    
names = name()
print(names) 


my_list = [ 1,2,3,4,5,6,7,2,4,3,5 ]

update_list = list(set(my_list))
print(update_list)



list_1 = [ 1,3,5,7,9,17,18,45,10 ]
list_2 = [ 1,3,5,7]

final_list = list(set(list_1) ^ set(list_2))
print(final_list)



list_1 = [1,2,3,4,5,6,7,8,9,10,17,18,45,99,100]
list_2 = [ 6 , 12 ]
list_3 = [ 3 , 5 , 9 , 8 , 4,2]

final_list = list(set(list_1) ^ set(list_2) ^ set(list_3))
print(final_list)


class Vehicle:
    def name( self , name ):
        return name
        
v = Vehicle()
print(v.__class__.__name__)  
      
'''






#----------------------file handling---------------------
'''
import os, glob, time, datetime, pathlib

myfile = r"D:\Guddu\area.py"
print(os.path.splitext(myfile)[0])
print(os.path.splitext(myfile)[1])
num_of_lines = sum(1 for l in open(myfile))
print(num_of_lines)

os.chdir("D:\Guddu")
for file in glob.glob("*.py"):
    print(file)

print("Last modification time: %s" % time.ctime(os.path.getmtime(myfile)))
print("Last metadata change time or path creation time: %s" % time.ctime(os.path.getctime(myfile)))
a = pathlib.Path("area.py")
print("Last modification time: %s" % datetime.datetime.fromtimestamp(a.stat().st_mtime))
print("Last metadata change time or path creation time: %s" % datetime.datetime.fromtimestamp(a.stat().st_ctime))
print( pathlib.Path("area.py").parent.absolute())      
print(pathlib.Path().absolute())

print("This file's filesize is : ", os.stat(myfile).st_size)
'''

# ---------------------------------



'''
class Polygon:
    def sides_no(self):
        pass
    
    
class Triangle(Polygon):
    def area(self):
        pass
        
obj_polygon = Polygon()
obj_triangle = Triangle()

print(type(obj_triangle) == Triangle)        
print(type(obj_triangle) == Polygon)

print()

print(isinstance(obj_triangle , Triangle))
print(isinstance(obj_triangle , Polygon ))    
   


import itertools

list_1 = [ 1,2,3,4]
list_2 = [ 'Ashish' , 'Bhuvan' , 'Harsh' , 'Salil' , 'Carry' ]

for i,j in zip(list_1 , list_2):
    print(i,j)

print()

for i,j in itertools.zip_longest(list_1 , list_2):
    print(i,j)


num = 1234567
rev_num = 0

while num != 0:
    digit = num % 10 
    rev_num = rev_num * 10 + digit
    num = num//10
    
print("Reversed number : " +str(rev_num))   
''' 


'''
num = 1234567

print(str(num)[::-1])
print(int(str(num)[::-1]))
'''



# -------------

'''
with open("first.py" , "a" ) as y:
    y.write("nayi baat")



with open("First.py" , "r" ) as p:
    content_list = p.readlines()
    
print(content_list)

content_list = [ x.strip() for x in content_list]
print(content_list)    



with open("First.py" ) as f:
    content_list = [ line for line in f]
    
print(content_list)

with open("First.py" ) as f:
    content_list = [ line.rstrip() for line in f]
print(content_list)
'''    
    
'''   
from shutil import copyfiles

copyfile("/Guddu/First.py" , "/Guddu/2nd.py")
 

from pathlib import Path
Path("/Guddu/dirA/dirB").mkdir(parents=True , exist_ok= True)


import hashlib 

def hash_file(flepath):
    
    h = hashlib.sha1()
    
    with open(filepath , rb) as file:
        
        chunk = 0
        while chunk !=b'':
            chunk= file.read(1024)
            h.update(chunk)
            
    return h.hexdigest()
message = hash_file("track1.mp3")
print(message)    


           
           

with open("names.txt" , 'r' , encoding = 'utf-8') as name_file:
    
    with open("body.txt" , 'r' , encoding = 'utf-8') as body_file:
        
        body = body_file.read()
        
        for names in name_file:
            mail = "Hello" + name.strip() + "\n" + body
            
            with open(name.strip()+ ".txt" , 'w' , encoding = 'utf-8') as mail_file:
                mail_file.write(mail)





models = [
    {'brand': 'Nokia', 'model': 216, 'color': 'Black'},
    {'brand': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'brand': 'Samsung', 'model': 7, 'color': 'Blue'}
]

sorted_models = sorted(models , key=lambda x: x['color'])
print(sorted_models)




check = lambda x : x.startswith('P')
print(check('Python'))
print(check('Ashish'))
print(check('Print'))
print(check('ap'))
'''


























