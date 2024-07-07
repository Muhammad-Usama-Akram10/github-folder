# TASK 1 Print Your Name with your Father name and Date of birth using suitable escape sequence charactor
name="m usama "
father_name="m akram"
dob="june 3,2000"

print("my name is",name,"\n","my father name is",father_name,"\n","dob is",dob,"\n")

# TASK 2 Write your small bio using variables and print it using print function
name1="m usama1 "
father_name1="m akram1"
age=24
dob1="june 3.1,2000"
occupation="Student Studying in bahria university"
print("my name is",name1,"\n","my father name is",father_name1,"\n","dob is",dob1,"\n","my age is",age,"\n","occupation is",occupation,"\n")

# TASK 3 Write a program in which use all the operators we can use in Python
# OPERATOR
print (2-2)
print (99+10,12+2,60/6,6*6)
print (55+6)
#power
print(2**4)
print(3**4)
print(3**3)
# "%" is modulus operator & it return remainder 
w= 9%4 
print(w)
# floor --> round-off at lower point
i= 5//2
print(i)
v=9//5
print(v) 

###TASK 4 Completes the following steps of small task:
#Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
#Mention Variable of Total Marks and assign 300 to it
#Calculate Percentage
english=88
islamait=91
math=55
total_marks=300
total_marks_obtained=english+ islamait+ math
percentage= total_marks_obtained/total_marks*100
print("total marks obtained is ",total_marks_obtained)
print("percentage is",percentage)

#task 5 Part -2 Python Basics (Conditional Statements)
# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#  Ask user for their salary and year of service and print the net bonus amount.
salary=int(input('what,s your salary: '))
years_of_service=int(input('year of service: '))

if years_of_service > 5 :
    bonus = salary*0.05 
else:
    bonus = 0

print('Net bonus amount is : ' , salary*0.05)

# Write a program to check whether a person is eligible for voting or not. 
# (accept age from user) if age is greater than 17 eligible otherwise not eligible
age=(int(input("your age is ")))  
if age>=18 :
    print("you are eligible")
else:
    print("you are not eligible")

# Write a program to check whether a number entered by user is even or odd.
#Type your code here
number = int(input('enter your number: '))
if number % 6 == 0 :
    print(f'entered {number} is even')
else:
    print(f'entered {number} is odd')

# Write a program to check whether a number is divisible by 7 or not. Show Answer
#Type your code here
number = int(input('enter you want to write a number'))
if number % 7 == 0 :
    print(f'{number} is divisible by 7')
else:
    print(f'{number} is not divisible by 7')

# Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".
#Type your code here
number = int(input('enter your number'))
if number % 5 == 0:
    print('hello')
else:
    print('bye')

# Write a program to display the last digit of a number.
#Type your code here
number = int(input('enter your number'))
last_digit = number % 10
print('last digit of number is : ' , last_digit)

#Take values of length and breadth of a rectangle from user and print if it is square or rectangle.
#Type your code here 
Length = int(input('value of length is : '))
Breadth = int(input('value of breadth is : '))
if Length == Breadth:
    print('This is Square')
else:
    print('This is Rectangle')

# Take two int values from user and print greatest among them.
# Type your code here
value_1 = int(input('enter your value'))
value_2 = int(input('enter your value'))
if value_1 > value_2 :
    print(f'the gratest value is value 1 {value_1}')
else:
    print(f'the gratest value is value 2 {value_2}')

# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
#Type your code here
quantity = int(input('Enter the quantity of items: '))
total_cost = quantity * 100
if total_cost >= 1000:
    discount = total_cost * 0.1
    total_cost -= discount
    print('total cost of user is: ' , {total_cost} )
else:
    print('No discount for user')

# A school has following rules for grading system:
#a. Below 25 - F
#b. 25 to 45 - E
#c. 45 to 50 - D
#d. 50 to 60 - C
#e. 60 to 80 - B
#f. Above 80 - A
#Ask user to enter marks and print the corresponding grade.
marks = int(input('Enter your marks: '))

if marks < 25:
    print('your grade is F')
elif 25 <= marks <= 45:
    print('your grade is E')
elif 45 < marks <= 50:
    print('your grade is D')
elif 50 < marks <= 60:
    print('your grade is C')
elif 60 < marks <= 80:
    print('your grade is B')
else:
    print('your grade is A')

# )A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.
#Type your code here
number_of_classes = int(input('Enter number of classes held : '))
number_of_classes_attended = int(input('Enter number of classes attended : '))
attendence = number_of_classes_attended / number_of_classes * 100
if attendence >= 75:
    print(F'student is allowed to sit in exam and his percentage of class attended is : {attendence}%' )
else:
    print(F'student is not allowed to sit in exam and his percentage of class attended is : {attendence}%' )

# Modify the above question to allow student to sit if he/she has medical cause.
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
#Type your code here
medical_cause = input('Do you have medical cause : ')
if medical_cause == 'NO':
    print('student is allowed to sit in exam')
else:
    print('student is not allowed to sit in exam')

# Write a program to check if a year is leap year or not.
#If a year is divisible by 4 then it is leap year but if the year is century year
# like 2000, 1900, 2100 then it must be divisible by 400.
#Type your code here
def  is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#And any other input of age should print "ERROR"
employee_gender = input('enter employee gender : ')
employee_age = int(input('enter employee age : '))
employee_martial_status = input('enter employee martial status : ')
if employee_gender == 'F':
    print('employee will work only in urban areas')
elif(employee_gender == 'M') and (25<= employee_age <=40):
    print('employee is male and will work any where')
elif (employee_gender == 'M') and (40<= employee_age <=60):
    print('employee is male and will work in urban areas only')
else:
    print('ERROR')

# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : Unit Price
#uptp 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per unit 
#(For example if input unit is 350 than total bill amount is Rs.3500 
 #(For example if input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750
units = int(input("Enter the number of units: "))
total_bill = 0
if units <= 100:
    total_bill = 0
elif units <= 300:
    total_bill = (units - 100) * 5
elif units > 300:
    total_bill = 200 * 5 + (units - 300) * 10
print(f"The total bill amount is Rs. {total_bill}")

# Take input of age of 3 people by user and determine oldest and youngest among them.
#Type your code here
ali_age = int(input('enter usman age :'))
atif_age = int(input('enter ashiq age :'))
amin_age = int(input('enter russel age :'))
oldest = max(ali_age, atif_age, amin_age)
youngest = min(ali_age, atif_age, amin_age)
print(f"The youngest person is {youngest} years old.")
print(f"The oldest person is {oldest} years old.")