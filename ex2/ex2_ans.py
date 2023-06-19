#1
'''
To access CRED programs, one needs to have a credit score of 750 or more.
Given that the present credit score is X,
determine if one can access CRED programs or not.
If it is possible to access CRED programs, output YES, otherwise output NO.
'''
"""
credit_score=int(input("Enter your credit score:"))
if credit_score>=750:
    print("yes")
else:
    print("no")
"""
#2
'''
A study has shown that playing a musical instrument helps in increasing one's IQ by 7 points.
Chef knows he can't beat Einstein in physics, but he wants to try to beat him in an IQ competition.
Given that Einstein’s IQ is170, and Chef currently has an IQ of X.
Determine if, after learning to play a musical instrument,
Chef's IQ will become strictly greater than Einstein's.
Print "Yes" if it is possible for Chef to beat Einstein,
else print "No" (without quotes).
'''
"""
iq_einstein=170
iq_chef=int(input("enter chef's current iq:"))
if (iq_chef+7)>iq_einstein:
    print("yes")
else :
    print("no")
"""
#3
'''
Chef is currently working for a secret research group called NEXTGEN.
While the rest of the world is still in search of a way to utilize Helium-3 as a fuel,
NEXTGEN scientists have been able to achieve 2 major milestones
Finding a way to make a nuclear reactor that will be able to utilize Helium-3 as a fuel
Obtaining every bit of Helium-3 from the moon's surface
Moving forward, the project requires some government funding for completion,
which comes under one condition: to prove its worth, the project should power Chefland
by generating at least A units of power each year for the next B years.
Help Chef determine whether the group will get funded assuming that the moon has X grams of Helium-3
and 1 gram of Helium-3 can provide Y amount of power.
Given A, B, X and Y , determine whether the group will get funded.
'''
"""
min_power_per_year=int(input("Enter A:"))
number_of_years=int(input("Enter the number of years:"))
amt_of_h3=int(input("Enter amount of helium-3(in grams):"))
power_per_gram=int(input("Enter power per gram:"))
total_power=amt_of_h3*power_per_gram
min_total_power=min_power_per_year*number_of_years
if total_power>=min_total_power:
    print("yes")
else:
    print("no")
"""
#4
'''
Print the following pattern 
 1
 1 1
 1 2 1
 1 3 3 1
 1 4 6 4 1
 1 5 10 10 5 1
 1 6 15 20 15 6 1
 '''
"""
print("PASCAL'S TRIAGLE")
def fact(n):
    if n==0 or n==1:
        return 1
    result=1
    for i in range(2,n+1):
        result*=i
    return result
for i in range(0,7):
    for j in range(0,i+1):
        print(int(fact(i)/(fact(i-j)*fact(j))),end=" ")
    print("")
"""
#5
'''
An integer is called squarefree if it is not divisible by any perfect squares other than 1.
For instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42,
and none of those numbers (except 1) is a perfect square.
On the other hand, 45 is not squarefree because it is divisible by 9, which is a perfect square.
Write a program that asks the user for an integer and tells them if it is squarefree or not.
'''
"""
number=int(input("Enter a number:"))
check=0
for i in range(2,number+1):
    if number%i==0:
        sqrt=i**(1/2)
        if (int(sqrt)-sqrt)==0:
            check=1
            print(number,"is not a squarefree number")
            break
if check==0:
    print(number,"is a squarefree number")
"""
#6
'''
Write a program to play the following simple game.
The player starts with $100. On each turn a coin is flipped and the player has to guess heads or tails.
The player wins $9 for each correct guess and loses $10 for each incorrect guess.
The game ends either when the player runs out of money or gets to $200.
'''
"""
from random import choice
cash=100
choices=["heads","tails"]
while cash>0 or cash<200:
    user_choice=input("enter our choice(heads/tails):")
    if choice(choices)==user_choice:
        cash+=9
        print("you guessed it!")
    else:
        cash-=10
        print("oops! guess it right next time")
    print(cash)
print("cash:$",cash)
print("END")
"""
#7
'''
The GCD (greatest common divisor) of two numbers is the largest number that both are divisible by.
For instance, gcd(18,42) is 6 because the largest number that both 18 and 42 are divisible by is 6.
Write a program that asks the user for two numbers and computes their gcd.
Shown below is a way to compute the GCD, called Euclid's Algorithm.
First compute the remainder of dividing the larger number by the smaller number
Next, replace the larger number with the smaller number and the smaller number with the remainder.
Repeat this process until the smaller number is 0. The GCD is the last value of the larger number.
'''
"""
number_1=int(input("Enter a number:"))
number_2=int(input("Enter a number:"))
if number_1>number_2:
    largest=number_1
    smallest=number_2
else:
    largest=number_2
    smallest=number_1
remainder=0
while smallest!=0:
    remainder=largest%smallest
    largest=smallest
    smallest=remainder
print(f"the GCD of {number_1} and {number_2} is {largest}")
"""
#8
'''
Write a program that draws “modular rectangles” like the ones below.
The user specifies the width and height of the rectangle,
and the entries start at 0 and increase typewriter fashion from left to right and top to bottom,
but are all done mod 10. Below are examples of a 3 × 5 rectangle and a 4 × 8.
'''
"""
rows=int(input("enter the number of rows:"))
columns=int(input("ente the number of columns:"))
i=0
for j in range(rows):
    for k in range(columns):
        print(i%10,end=" ")
        i+=1
    print("")
"""
#9
'''
Write a program that prints out the sine and cosine of the angles ranging from 0 to 345°
in 15° increments. Each result should be rounded to 4 decimal places. Sample output is shown below:
'''
"""
from math import sin,cos,pi
TO_RADIAN=pi/180
angle=0
print("angle sin cos")
while angle<=345:
    print("{:.4f} {:.4f} {:.4f}".format(angle,sin(angle*TO_RADIAN),cos(angle*TO_RADIAN)))
    angle+=15
"""
#10
'''
Write a Python program that will: 
Ask the user for seven numbers
Print the total sum of the numbers
Print the count of the positive entries, the number entries equal to zero,
and the number of negative entries. Use an if, elif, else chain, not just three if statements.
'''
"""
numbers=list(map(int,input("Enter 7 numbers seperated by comma:").split(",")))
print("sum of 7 numbers:",sum(numbers))
possitive=0
negative=0
zero=0
for i in numbers:
    if i>0:
        possitive+=1
    elif i<0:
        negative+=1
    elif i==0:
        zero+=1
print("count of possitive numbers:",possitive)
print("count of negative numbers:",negative)
print("count of zero:",zero)
"""
#11
'''
random guesser
Allow the user to guess for a number.
If the user finds the number within max number of tries, he wins the game.
After each try, the system can provide hint to aid the user in the next guess.
It can print either lower (or) higher depending on the whether the guess was lower than the number (or) higher than the number.
Refine the code so that number of hints are increased to 4 namely ‘higher’,
‘much higher’, ‘lower’, ‘much lower’.
If the absolute difference between the guess and the number is greater than 10 
'''
"""
from random import randint
number=randint(1,100)
tries=5
while tries>0:
    guess=int(input("Enter your guess:"))
    if guess==number:
        print("you guessed it!")
        tries=-1
        break
    elif guess-number< -300:
        print("guess much higher")
    elif guess-number<0:
        print("guess higher")
    elif guess-number>0:
        print("guess lower")
    elif guess-number>30:
        print("guess much lower")
    tries-=1
if tries==0:
    print("you ran out of tries")
"""
#12
'''
Write a program that plays rock, paper, scissors: 
Create a program that randomly prints 0, 1, or 2.
Expand the program so it randomly prints rock, paper, or scissors using if statements.
Don't select from a list, as shown in the chapter.
Add to the program so it first asks the user their choice.
(It will be easier if you have them enter 1, 2, or 3.)
Add conditional statement to figure out who wins.
'''
"""
from random import choice
choices=["rock","paper","scissors"]
print("enter 0 for rock \n1 for paper \n2 for scissors")
computer=choice([0,1,2])
user=int(input("enter the number corresponding to your choice:"))
print("computer:{}\nyou:{}".format(choices[computer],choices[user]))
if computer==user:
    print("draw")
elif choices[computer]=="rock" and choices[user]=="paper":
    print("you win!")
elif choices[computer]=="paper" and choices[user]=="scissors":
    print("you win!")
elif choices[computer]=="scissors" and choices[user]=="rock":
    print("you win!")
elif choices[user]=="rock" and choices[computer]=="paper":
    print("you loose!")
elif choices[user]=="paper" and choices[computer]=="scissors":
    print("you loose!")
elif choices[user]=="scissors" and choices[computer]=="rock":
    print("you loose!")
"""
