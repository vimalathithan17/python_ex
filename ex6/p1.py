#1
'''
Write a class called Investment with fields called principal and interest. The 
constructor should set the values of those fields. There should be a method 
called value_after that returns the value of the investment after n years. The formula 
for this is p(1+i)^n
, where p is the principal, and i is the interest rate. It should also use 
the special method __str__ so that printing the object will result in something like 
below:
Principal - $1000.00, Interest rate - 5.12%
'''
'''class Investment:
    def __init__(self,principle,interest):
        self.principle=principle
        self.interest=interest
    def value_after(self,n):
        return f"value of investment after {n} years is ${self.principle*((1+self.interest)**n)}"
    def __str__(self):
        return f"Principal- ${self.principle} , Interest rate -{self.interest}%"
investment1=Investment(eval(input("enter the principal:")),eval(input("enter the intrest:")))
print(investment1.value_after(int(input("enter the number of years:"))))
print(investment1)'''

#2
'''Write a class called Product. The class should have fields called name, amount, 
and price, holding the product's name, the number of items of that product in stock, 
and the regular price of the product. There should be a method get_price that 
receives the number of items to be bought and returns a the cost of buying that many 
items, where the regular price is charged for orders of less than 10 items, a 10% 
discount is applied for orders of between 10 and 99 items, and a 20% discount is 
applied for orders of 100 or more items. There should also be a method 
called make_purchase that receives the number of items to be bought and 
decreases amount by that much.
'''
'''
class Product:
    def __init__(self,name,amount,price):
        self.name=name
        self.amount=amount
        self.price=price
    def get_price(self,n_items):
        regular_cost=n_items*self.price
        if n_items<10:
            return regular_cost
        elif n_items in range(10,100):
            return regular_cost*0.9
        else:
            return regular_cost*0.8
    def dec_make_purchase(func):
        def inner(self,n_items):
            if self.amount<n_items:
                print(f"can't make purchase(available stock is not suuficient to meet the order),quantity of stock available is {self.amount}")
                return False
            else :
                func(self,n_items)
                return True
        return inner
    @dec_make_purchase
    def make_purchase(self,n_items):
        self.amount-=n_items
product1=Product("tub",40,45.0)
n_items=int(input("enter the number of items to be putchased:"))
can_purchase=product1.make_purchase(n_items)
if(can_purchase):
   print(f"total cost:${product1.get_price(n_items)}")
'''
#3
'''
Write a class called Password_manager. The class should have a list 
called old_passwords that holds all of the user's past passwords. The last item of the 
list is the user's current password. There should be a method called get_password that 
returns the current password and a method called set_password that sets the user's 
password. The set_password method should only change the password if the 
attempted password is different from all the user's past passwords. Finally, create a 
method called is_correct that receives a string and returns a 
boolean True or False depending on whether the string is equal to the current 
password or not.

'''
'''
class PasswordManager:
    def __init__(self,prev_passwords,current_pass):
        self.old_passwords=[]+prev_passwords
        self.old_passwords.append(current_pass)
    def get_password(self):
        return self.old_passwords[-1]
    def set_password(self,new_pass):
        if new_pass not in self.old_passwords:
            self.old_passwords.append(new_pass)
        else :
            print("Enter a password that is not previously used")
    def is_correct(self,entered_pass):
        return self.old_passwords[-1]==entered_pass
old_pass=input("Enter your old passwords seperated by comma:").split(",")
current_pass=input("Enter your current passsword:")
person1_pm=PasswordManager(old_pass,current_pass)
print(person1_pm.get_password())
new_pass=input("Enter the new password to be set:")
person1_pm.set_password(new_pass)
entered_pass=input("Enter password:")
print(person1_pm.is_correct(entered_pass))
'''
#4
'''
Write a class called Time whose only field is a time in seconds. It should have a method 
called convert_to_minutes that returns a string of minutes and seconds formatted as 
in the following example: if seconds is 230, the method should return '5:50'. It should 
also have a method called convert_to_hours that returns a string of hours, minutes, 
and seconds formatted analogously to the previous method.

'''
"""class Time:
    def __init__(self,sec):
        self.sec=sec
    def convert_to_minutes(self):
        minutes=self.sec//60
        seconds=self.sec%60
        return "{}:{}".format(minutes,seconds)
    def convert_to_hours(self):
        hours=self.sec//3600
        minutes=(self.sec//60)%60
        seconds=self.sec%60
        return "{}:{}:{}".format(hours,minutes,seconds)
sec=int(input("Enter the number of seconds:"))
t=Time(sec)
print(t.convert_to_minutes())
print(t.convert_to_hours())
"""
#5
'''
Write a class called Wordplay. It should have a field that holds a list of words. The 
user of the class should pass the list of words they want to use to the class. There 
should be the following methods:
o words_with_length(length) — returns a list of all the words of length length
o starts_with(s) — returns a list of all the words that start with s
o ends_with(s) — returns a list of all the words that end with s
o palindromes() — returns a list of all the palindromes in the list
o only(L) — returns a list of the words that contain only those letters in L
o avoids(L) — returns a list of the words that contain none of the letters in L
'''
class Wordplay:
    def __init__(self,words):
        self.word_list=[]+words
    def words_with_length(self,length):
        result = list(map(lambda x:x if len(x)==length else None,self.word_list))
        result if None not in result else result.remove(None)
        return result
    def starts_with(self,s):
        result=list(map(lambda x:x if x[0]==s else None,self.word_list))
        result if None not in result else result.remove(None)
        return result
    def ends_with(self,s):
        result=list(map(lambda x:x if x[-1]==s else None,self.word_list))
        result if None not in result else result.remove(None)
        return result
    def palindromes(self):
        result=list(map(lambda x:x if x==x[::-1] else None,self.word_list))
        result if None not in result else result.remove(None)
        return result
    def only(self,l):
        l=list(set(l))
        count=dict()
        for i in self.word_list:
            count[i]=0
        keys=count.keys()
        for i in l:
            for key in keys:
                if i in key:
                    count[key]+=1
        result=[]
        for key in keys:
            if count[key]==len(l):
                result.append(key)
        return result
    def avoids(self,l):
        l=list(set(l))
        count=dict()
        for i in self.word_list:
            count[i]=0
        keys=count.keys()
        for i in l:
            for key in keys:
                if i in key:
                    count[key]+=1
        result=[]
        for key in keys:
            if count[key]==0:
                result.append(count[key])
        return result
    
c=Wordplay(["hell","dell"])
#print(c.words_with_length(4))
#print(c.starts_with('d'))
print(c.only('del'))
