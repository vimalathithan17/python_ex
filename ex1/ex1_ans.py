#1
'''
Given the amount in rupees , convert it into ruble 
1 rupee = 1.11 ruble
'''
"""
amount=int(input("enter the amount in rupees:"))
print("the ammount in ruble :",amount*1.11)
"""
#2
'''
Normalize the input data ( an integer x) using z-score normalization whose equation is provided below
z =( x-mean)/ std 
Accept mean and standard deviation(std) from the user and compute the normalized value
'''
"""
x=int(input("enter x:"))
mean=int(input("enter mean:"))
std=int(input("enter standard deviation:"))
print("z-normaliztion of x is:",(x-mean)/std)
"""
#3
'''
Compute BMI(Body Mass Index) of a person 
Accept mass in kg  and height in meters 
BMI = (mass) / (height*height)
'''
"""
mass=eval(input("enter mass in kg:"))
height=eval(input("enter height in meters:"))
print("BMI:",mass/(height**2))
"""
#4
'''
Accept preferred name for mail account  from the user and create a mail id by appending the
domain information
Consider domain as @google.com
Ex: if user name is 'all' , mail id is all@google.com 
'''
"""
domain="@google.com"
user_name=input("enter your name:")
print("your e-mail id is:",user_name+domain)
"""
#5
'''
Consider the following books are bought by the user through Amazon web portal.
The rate and quantity of the items are provided below. 
The user is also entitled for a discount of 15% for the purchase.
Find the total cost of purchase in rupees.
Item	              Quantity	Cost
The Alchemist	        2	$50
Rich dad and poor dad	3	$67
Harry Potter	        1	$100

'''
"""
cost=(2*50)+(3*67)+(1*100)
print("the total cost is $",cost-(cost*0.15))
"""
