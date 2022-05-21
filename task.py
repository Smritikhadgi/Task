#1. Write a python program to reverse a given list using while loop.
# a=[1,2,3,4]
a=[1,2,3,4]
output=[ ]
i=len(a)-1
while i>=0:
    output=a.reverse()
    i=i-1
print(a)



#2.Write a python program to reverse a string using while loop.
# a="python"

a="python"
output=" "
i=len(a)-1
while i>=0:
    output=output+a[i]
    i=i-1
print(output)
# 3.Write a python program to print a multiplication table of any number using while loop.

n=int(input("Enter a number for multiplication:"))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i=i+1

# 5.Write a program to print the following using while loop
# a. first 10 even numbers
# b.first 10 odd numbers
# c.first 10 natural numbers

i=0
while i<=8:
    i=i+2
    print(i)
i=1
while i<=20:
    i=i+2
    print(i)
i=0
while i<=9:
    i=i+1
    print(i)
# 6.Write for loop statement to print the following series:
# 10 20 30 --------300
a=10
while a<300:

    a=a+10
    print(a,end=" ")

# 7. Write a while loop statement to print the following series:
# 105 98 -------7
a=112
while a>=7:
    a=a-7
    print(a,end=" ")

# 8. Write a program to print the factorial of a number accepted from user.

n=int(input("Enter a number to calculate factorial:"))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print(fact)

# 1.  Write a Python function to multiply all the numbers in a list.
# Sample list = [8,2,3,-1,7]

def mul():
    a=[8,2,3,-1,7]
    b=1
    for i in range(0,5):
        b=a[i]*b
    print(b)
mul()

# 2.  Write a Python function to sum all the numbers in a list.
# Sample list : [8, 2, 3, 0, 7]

def add():
    a=[8,2,3,0,7]
    b=0
    for i in range(0,5):
        b=a[i]+b
    print(b)
add()

# 3.  Write a python function to find min of three numbers.(no parameter and no return type)

def min(x,y,z):
    if x<y and x<z:
        print(x, 'is the smallest minimal integer.')
    elif y<x and y<z:
        print(y,'is the smallest minimal integer.')
    else:
        print(z,'is the smalles minimal integer')
min(-2,3,1)
    
##################incase not with parameters#############################

def min():
    x=float(input('enter a number; '))
    y=float(input('enter next number; '))
    z=float(input('enter third number; '))
    if x<y and x<z:
            print(x, 'is the smallest minimal integer.')
    elif y<x and y<z:
        print(y,'is the smallest minimal integer.')
    else:
        print(z,'is the smalles minimal integer')
min()

# 4. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input
print(fizz_buzz(33))
print(fizz_buzz(5))

# 5. Create a function that can accept two arguments name and age and print its value.

def na(name,age):
    print(f"your name is {name}, and you are existing from {age} years in time.")
na("kevin","27")

# 6. Write a program function to find max of three numbers.(no parameter and no return type)

def gtx(x,y,z):
    if x>y and x>z:
        print(x,"is the greatest")
    elif y>x and y>z:
            print(y,"is the greatest")
    else:
        print(z,"is the greatest")
gtx(3,0,1)

# 7. Write a Python function to print the even numbers from a given list. 
# sample: [1,2,3,4,5,6]

def evn():
    a=[1,2,3,4,5,6]
    for b in a:
        if b%2==0:
            print(b,end=",")
evn()   

# 8. Write a Python function to print the odd numbers from a given list. 
# sample: [1,2,3,4,5,6]

def odd():
    a=[1,2,3,4,5,6]
    for b in a:
        if b%2!=0:
            print(b,end=",")
odd()

# 9. Write a Python function that takes a number as a parameter and check the number is prime or not

def p(input):
    if input>1:
        for i in range(2,input):
                if input%i==0:
                    print(input,'is not a prime number.')
                    print(i,'times', input//i,'is', input)
                break
    else:
        print(input,'is a prime number')
    
print(p(13))

# 10. Write a function to reverse a string.

def rev():
    x="multiverse"
    for j in range(9,-1,-1):
        print(x[j],end="")
# rev()

# 12. Write a program to create function func1()
#  to accept a variable length of arguments and print their value.

def func1(*args):
    print(*args)
    
func1('hello', 'hi', 23, '2383')

# 13  Write a program to create function calculation() such that it can accept 
# two variables and calculate addition and subtraction.Also, it must return 
# both addition and subtraction in a single return call

def calculation(c,d):
    print(c+d)
    print(c-d)
    return c,d
calculation(6,3)

# 14. Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

def func(employee, salary=9000):
    print('employee: ', employee )
    print('Salary: ', salary)

func('stevenGrant', 30000)
func('Marc')

# 15. Find the largest item from a given list. 
# sample: [4, 6, 8, 24, 12, 2]

sample=[4,6,8,24,12,2]
print(max(sample))

# 16. Find the smalles item from a given list. 
# sample: [4, 6, 8, 24, 12, 2]

smpl=[4,6,8,24,12,2]
print(min(smpl))

# 17. Define a function that accepts roll number and returns
#  whether the student is present or absent.

def rollno(rno):
    x=[23,43,22,56]
    if rno in x:
        print(f'roll number {rno}, is present.')
    else:
        print(f'roll number {rno}, is absent')
rno=int(input('enter a roll number'))
rollno(rno)

# 18. Define a function that accepts a number and returns whether the number is even or odd.

def func(x):
    if x%2==0:
        print(f"{x}, is even")
    else:
        print(f"{x}, is odd")
x=int(input('enter your number: '))
func(x)

# 19. Define a function which counts vowels and consonant in a word.

def count(val):
    vov=0
    cons=0
    for i in range(len(val)):
        if val[i] in ["a",'e','i','o','u']:
            vov=vov+1
        else:
            cons=cons+1
    print("count of vowels is", vov)
    print("count of consonant is", cons)
x=input("enter sth; ")
count(x)

# 20. Define a function that returns Factorial of a number.

def factorial(num):
    fact=1
    while(num!=0):
        fact*=num
        num=num-1
    print("Factorial is", fact)
num=int(input('enter a number'))
factorial(num)

# 21. Define a function that accepts lowercase words
#  and returns uppercase words.

def respone(text):
    z=text.upper()
    print(z)
text=input('Enter a string.')
response(text)

# 22. Define a function that accepts radius and returns the area of a circle.

def area(radius):
    area=3.14*radius**2
    return area
radius=int(input('enter radii; '))
print(area(radius))

# 1 .. Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".

a=int(input("Enter your desired number: "))
b=int(input("Enter your other number: "))
if a==b:
    print("1")
elif a>b:
    print("2")
else:
    print("3")

________________________________________________________________________________

# 2. Print "Hello" if a is equal to b, and c is equal to d.  
a=int(input("Enter number A: "))
b=int(input("Enter number B: "))
c=int(input("Enter number C: "))
d=int(input("Enter number D: "))
if a==b and c==d:
    print("HELLO")
else:
    print("Nice to meet you! ")

_______________________________________________________________
 
# 3. Print "Hello" if a is equal to b, or if c is equal to d.

a=int(input("Enter number A: "))
b=int(input("Enter number B: "))
c=int(input("Enter number C: "))
d=int(input("Enter number D: "))
if a==b or c==d:
    print("HELLO")
else:
    print("Nice to meet you! ")
_______________________________________________________________---

# 4. For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.

x=int(input("Enter an integer: "))
if x>0:
    print("True")
elif x<0:
    print("False")
else:
    print("Zero")

_____________________________________________

# 5. Check whether the user input number is even or odd and display it to user.
c=int(input("ENTER A NUMBER: "))
if (c%2==0):
    print("Even")
else:
    print("Odd")

________________________________

# 6.  WAP which accepts marks of four subjects and display total marks, percentage and grade.
g=int(input("Enter maths mark; "))
h=int(input("Enter your programming mark;"))
i=int(input("Enter your software design mark; "))
j=int(input("Enter your algo marks; "))
x=g+h+i+j
print(x)
y=x/400*100
print(y)
if y>70:
    print("Distinction")
elif y>60:
    print("First Division")
elif y>40:
    print("Pass")
else:
    print("Fail")
#_________________________________________________

# 7. What is the output of ‘APPLE’ > ‘apple’?
#  false

# 8. Write a Python program to display your details like name, age, address in three different lines.
def personal_details():
    name, age = "Pramesh", 20
    address = "167 K.U.K.L-Jay Ganesh Galli-16,Parijat sadak,44600-Kathmandu"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
 
personal_details()

_______________________________________________________

# 9. Write a python program which accepts the radius of circle from user and compute the area.

r=float(input("ENTER THE RADIUS OF THE CIRCLE FOR FINDING OUT ITS AREA; "))
pi=22/7
a=pi*r**2
print(a)
__________________________________________________________________


# 10. A school decided to replace the desks in three classrooms. Each desk sits two students. 
# Given the number of students in each class, print the smallest possible number of desks 
# that can be purchased.

# The program should read three integers: the number of students in each of the three 
# classes, a, b and c respectively.
# Hint. In the first test there are three groups. The first group has 20 students and thus needs 10 
# desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 
# 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total. 

a=int(input("Enter the number of students in first class; "))
b=int(input("Enter the number of students in second class; "))
c=int(input("Enter the number of students in second class;"))
d=(a+b+c)/2
print(d,"are the required number of total desks.")

______________________________________________________________________-

# 11. Given three integers, print the smallest one. (Three integers should be user input)

a = int(input("Enter first number  : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number  : "))
smallest = 0
if a < b and a < c :
    smallest = a
if b < a and b < c :
    smallest = b
if c < a and c < b :
    smallest = c

print(smallest, "is the smallest of three numbers.")

_________________________________________________________________________________-

# 12. Write a program that takes three numbers and prints their sum. Every number is given on 
# a separate line.

a=int(input("Enter 1st number; "))
b=int(input("Enter 2nd number; "))
c=int(input("Enter 3rd number; "))
d=(a+b+c)
print(a)
print(b)
print(c)
print(d,"is the sum of three numbers")

___________________________________________________

# 13. Write a program that reads the length of the base and the height of a right-angled triangle 
# and prints the area. Every number is given on a separate line.

b=float(input("Enter the length of the base of a right angled triangle; "))
h=float(input("Enter the length of the height of a right angled triangle; "))
A=(b*h)/2
print(b)
print(h)
print(A,"is the area of the given RA triangle")

_____________________________________________________________________________

# 14. N students take K apples and distribute them among each other evenly. The remaining 
# (the undivisible) part remains in the basket. How many apples will each single student 
# get? How many apples will remain in the basket? The program reads the numbers N and 
# K. It should print the two answers for the questions above.


n=int(input("Enter number of student; "))
k=int(input("Enter number of apples; "))
v=n//k
h=n%k
print(v,";is the number of apples shared each")
print(h,";is the number of apple left over")

# 1. What is the output of ‘banana’ > ‘BANANA’?
a="banana"
print(a)
print(a.upper())

# 2. Check whether 5 is in list of first 5 natural numbers or not. Hint: List => [1,2,3,4,5]

a=int(input("Enter a number to check weather the number is natural or not:"))
if a>=0:
    print("The given number is natural.")
else:
    print("The given number is not natural number.")

# 3. Given three integers, print the smallest one. (Three integers should be user input)

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number: "))

if a<b and a<c:
    print("The smallest number is a which is",a)
elif b<a and b<c:
    print("The smallest number is b which is",b)
else:
    print("The smallest number is c which is",c)

4. Given a three-digit number. Find the sum of its digits

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number: "))
sum=a+b+c
print("The sum of number is:",sum)

# 5. Write a program that asks the user for a number in the range of 1 to 12. The program should display the corresponding month, where
# 1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 8=august,9=september,10=october,11=november,12=december. The program should display an error message if the user enters a number
# that is outside the range of 1 to 12.

month=int(input("Enter a number to know month:"))
if month==1:
    print("January")
elif month==2:
    print("February")
elif month==3:
    print("March")
elif month==4:
    print("April")
elif month==5:
    print("May")
elif month==6:
    print("June")
elif month==7:
    print("July")
elif month==8:
    print("August")
elif month==9:
    print("September")
elif month==10:
    print("October")
elif month==11:
    print("November")
elif month==12:
    print("December")


# 6. Given x = 5, what will be the value of x after we run x+=3?

x=5
x+=3
print(x)

# 7. Write a Python Program to Check Prime Number.
a=int(input("Enter a number to check weather the given number is prime or not:"))
b=3
if a%b==0:
    print("prime number")
else:
    print("composite numbers")

# # 8. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

math=int(input("Enter your marks in math:"))
programming=int(input("Enter your marks in programming:"))
science=int(input("Enter your marks in science:"))
english=int(input("Enter your marks in english:"))
totalmarks=400
obtainedmarks=math+programming+science+english
percentage=obtainedmarks/totalmarks*100
print("Your percentage is:",percentage)
if percentage>80:
    print("you got A")
elif percetage>60:
    print("you got B")
elif percentage>50:
    print("you got C")
elif percentage>45:
    print("you got D")
elif percentage>25:
    print("you got E")
else:
    print("you got F")

# 9. Take input of age of 3 people by user and determine oldest and youngest among them
a=int(input("Enter your age:"))
b=int(input("Enter your age:"))
c=int(input("Enter your age:"))
if a>b and a>c:
    print("A is oldest")
elif b>c and b>a:
    print("B is oldest")
elif c>a and c>b:
    print("C is oldest")
if a<b and a<c:
    print("A is youngest")
elif b<a and b<c:
    print("B is youngest")
else:
    print("C is youngest")

# 10.  Write a program to check whether a person is eligible for voting or not. (accept age from user)

age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible for voting.")
else:
    print("sorry you are not eligible for voting.")

# 11.  Write a program to check whether a number entered by user is even or odd.

a=int(input("Enter a number to check the number is even or odd:"))
if a%2==0:
    print("Even number.")
else:
    print("Odd number.")

# 12. Write a program to check whether a number is divisible by 7 or not.

a=int(input("Enter a number to check weather it is divisible by 7 or not:"))
if a%7==0:
    print("The number you entered is divisible by 7")
else:
    print("Sorry!!")


# 13. Write a program to display "Hello" if a number entered by user is a multiple of five ,
# otherwise print "Bye".

n=int(input("Enter a number:"))
if n%5==0:
    print("Hello")
else:
    print("Bye")

# 14. Write a program to accept percentage from the user and display the grade according to the following criteria:

#          Marks                                    Grade
#          > 90                                         A
#          > 80 and <= 90                    B
#          >= 60 and <= 80                  C
#          below 60                                 D

totalmarks=400
english=int(input("Enter your marks in english:"))
math=int(input("Enter your marks in math:"))
computer=int(input("Enter your marks in computer:"))
account=int(input("Enter your marks in account:"))
obtainedmarks=english+math+computer+account
print("Your obtained marks is:",obtainedmarks)


percentage=obtainedmarks/totalmarks*100
print("Your percentage is:",percentage)

if percentage>90:
    print(" A")
elif percentage>80:
    print(" B")
elif percentage>=60:
    print(" C")
else:
    print(" D")

# 15. Accept any city from the user and display monument of that city.
#                   City                                 Monument
#                   Delhi                               Red Fort
#                   Agra                                Taj Mahal
#                   Jaipur                              Jal Mahal

city=input("Enter the name of the city:")
if city=="Delhi":
    print("Red Fort")
elif city=="Agra":
    print("Taj Mahal")
elif city=="Jaipur":
    print("Jal Mahal")

# 16. Write the output of the following if

a = 9

if (a>5  and a<=10):
    print("Hello")
else:
    print("Bye")

# 17. Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

num = int(input("enter number:"))
if num%2 == 0:
   if num%3 == 0:
      print ("Divisible by 3 and 2")
   else:
      print ("divisible by 2 not divisible by 3")
else:
   if num%3 == 0:
      print ("divisible by 3 not divisible by 2")
   else:
      print  ("not Divisible by 2 not divisible by 3")

# 18. Write a program to check a character is vowel or not.

n=input("Enter one letter:")
if n=="a":
    print("vowel")
elif n=="e":
    print("vowel")
elif n=="i":
    print("vowel")
elif n=="0":
    print("vowel")
elif n=="u":
    print("vowel")
else:
    print("Consonant")

# 19. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
# Like:
# Enter First Number: 7
# Enter Second Number : 9
# Enter operator : +
# Your Answer is : 16

l=int(input("Enter a number:"))
m=int(input("Enter another number"))
n=input("Enter operator:")
if n=="+":
    print(l+m)
elif n=="-":
    print(l-m)
elif n=="*":
    print(l*m)
elif n=="/":
    print(l/m)
elif n=="%":
    print(l%m)
elif n=="//":
    print(l//m)
else:
    print("wrong input or operator!!")


for i in range(1,7):
    print("python")
print("learning python")
b="multiverse"
for i in b:
    print(i)

#1. Write a python program to reverse a given list using while loop.
# a=[1,2,3,4]
a=[1,2,3,4]
output=[ ]
i=len(a)-1
while i>=0:
    output=a.reverse()
    i=i-1
print(a)



# 2.Write a python program to reverse a string using while loop.
# a="python"

a="python"
output=" "
i=len(a)-1
while i>=0:
    output=output+a[i]
    i=i-1
print(output)
# 3.Write a python program to print a multiplication table of any number using while loop.

n=int(input("Enter a number for multiplication:"))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i=i+1

# 5.Write a program to print the following using while loop
# a. first 10 even numbers
# b.first 10 odd numbers
# c.first 10 natural numbers

i=0
while i<=8:
    i=i+2
    print(i)
i=1
while i<=20:
    i=i+2
    print(i)
i=0
while i<=9:
    i=i+1
    print(i)
# 6.Write for loop statement to print the following series:
# 10 20 30 --------300
a=10
while a<300:

    a=a+10
    print(a,end=" ")

# 7. Write a while loop statement to print the following series:
# 105 98 -------7
a=112
while a>=7:
    a=a-7
    print(a,end=" ")

# 8. Write a program to print the factorial of a number accepted from user.

n=int(input("Enter a number to calculate factorial:"))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print(fact)

# 1.  Write a Python function to multiply all the numbers in a list.
# Sample list = [8,2,3,-1,7]

def mul():
    a=[8,2,3,-1,7]
    b=1
    for i in range(0,5):
        b=a[i]*b
    print(b)
mul()

# 2.  Write a Python function to sum all the numbers in a list.
# Sample list : [8, 2, 3, 0, 7]

def add():
    a=[8,2,3,0,7]
    b=0
    for i in range(0,5):
        b=a[i]+b
    print(b)
add()

# 3.  Write a python function to find min of three numbers.(no parameter and no return type)

def min(x,y,z):
    if x<y and x<z:
        print(x, 'is the smallest minimal integer.')
    elif y<x and y<z:
        print(y,'is the smallest minimal integer.')
    else:
        print(z,'is the smalles minimal integer')
min(-2,3,1)
    
##################incase not with parameters#############################

def min():
    x=float(input('enter a number; '))
    y=float(input('enter next number; '))
    z=float(input('enter third number; '))
    if x<y and x<z:
            print(x, 'is the smallest minimal integer.')
    elif y<x and y<z:
        print(y,'is the smallest minimal integer.')
    else:
        print(z,'is the smalles minimal integer')
min()

# 4. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input
print(fizz_buzz(33))
print(fizz_buzz(5))

# 5. Create a function that can accept two arguments name and age and print its value.

def na(name,age):
    print(f"your name is {name}, and you are existing from {age} years in time.")
na("kevin","27")

# 6. Write a program function to find max of three numbers.(no parameter and no return type)

def gtx(x,y,z):
    if x>y and x>z:
        print(x,"is the greatest")
    elif y>x and y>z:
            print(y,"is the greatest")
    else:
        print(z,"is the greatest")
gtx(3,0,1)

# 7. Write a Python function to print the even numbers from a given list. 
# sample: [1,2,3,4,5,6]

def evn():
    a=[1,2,3,4,5,6]
    for b in a:
        if b%2==0:
            print(b,end=",")
evn()   

# 8. Write a Python function to print the odd numbers from a given list. 
# sample: [1,2,3,4,5,6]

def odd():
    a=[1,2,3,4,5,6]
    for b in a:
        if b%2!=0:
            print(b,end=",")
odd()

# 9. Write a Python function that takes a number as a parameter and check the number is prime or not

def p(input):
    if input>1:
        for i in range(2,input):
                if input%i==0:
                    print(input,'is not a prime number.')
                    print(i,'times', input//i,'is', input)
                break
    else:
        print(input,'is a prime number')
    
print(p(13))

# 10. Write a function to reverse a string.

def rev():
    x="multiverse"
    for j in range(9,-1,-1):
        print(x[j],end="")
# rev()

# 12. Write a program to create function func1()
#  to accept a variable length of arguments and print their value.

def func1(*args):
    print(*args)
    
func1('hello', 'hi', 23, '2383')

# 13  Write a program to create function calculation() such that it can accept 
# two variables and calculate addition and subtraction.Also, it must return 
# both addition and subtraction in a single return call

def calculation(c,d):
    print(c+d)
    print(c-d)
    return c,d
calculation(6,3)

# 14. Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

def func(employee, salary=9000):
    print('employee: ', employee )
    print('Salary: ', salary)

func('stevenGrant', 30000)
func('Marc')

# 15. Find the largest item from a given list. 
# sample: [4, 6, 8, 24, 12, 2]

sample=[4,6,8,24,12,2]
print(max(sample))

# 16. Find the smalles item from a given list. 
# sample: [4, 6, 8, 24, 12, 2]

smpl=[4,6,8,24,12,2]
print(min(smpl))

# 17. Define a function that accepts roll number and returns
#  whether the student is present or absent.

def rollno(rno):
    x=[23,43,22,56]
    if rno in x:
        print(f'roll number {rno}, is present.')
    else:
        print(f'roll number {rno}, is absent')
rno=int(input('enter a roll number'))
rollno(rno)

# 18. Define a function that accepts a number and returns whether the number is even or odd.

def func(x):
    if x%2==0:
        print(f"{x}, is even")
    else:
        print(f"{x}, is odd")
x=int(input('enter your number: '))
func(x)

# 19. Define a function which counts vowels and consonant in a word.

def count(val):
    vov=0
    cons=0
    for i in range(len(val)):
        if val[i] in ["a",'e','i','o','u']:
            vov=vov+1
        else:
            cons=cons+1
    print("count of vowels is", vov)
    print("count of consonant is", cons)
x=input("enter sth; ")
count(x)

# 20. Define a function that returns Factorial of a number.

def factorial(num):
    fact=1
    while(num!=0):
        fact*=num
        num=num-1
    print("Factorial is", fact)
num=int(input('enter a number'))
factorial(num)

# 21. Define a function that accepts lowercase words
#  and returns uppercase words.

def respone(text):
    z=text.upper()
    print(z)
text=input('Enter a string.')
response(text)

# 22. Define a function that accepts radius and returns the area of a circle.

def area(radius):
    area=3.14*radius**2
    return area
radius=int(input('enter radii; '))
print(area(radius))