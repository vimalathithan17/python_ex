#1
'''
Create a class, "PrimeTester", that defines one method "Boolean isPrime(int n)".
When this function is called the implementing class should determine if the given "n" is prime or not.
Create a class "SimpleTester" that inherits "PrimeTester" and uses a naive method
to determine if a given number is a prime or not.
'''
"""
class PrimeTester:
    def isPrime(self,n):
        if n==2:
            return 0
        else:
            c=0
            for i in range(2,n):
                if(n%i==0):
                    c=1
                    return 1
            if c==0:
                return 0
                
class SimpleTester(PrimeTester):
    def prime(self,n):
        b=self.isPrime(n)
        if(b==0):
            print(f"{n} is a prime number")
        else:
            print(f"{n} is not a prime number")
n=int(input("Enter a number:"))
obj=SimpleTester()
obj.prime(n)
"""

#2
'''
Create a class called Fruit with a method Boolean hasAPeel().
Write another class Vegetable with the method Boolean isARoot().
Create a class called Checking which consists of the following methods: 
String doesThisHaveAPeel(Fruit f)
and String  doesThisHaveARoot(Vegetable v).
The doesThisHaveAPeel() should in turn check hasAPeel().
If true display “This has a peel”. Else display “This doesn’t have a peel”.
Similarly the doesThisHaveARoot() should check the isARoot().
If yes, display a message “This sis a root” else display “This is not a root”. 
Create a class called Tomato which implements the above classes
and provides proper implementation for the above methods.
'''
"""
class Fruit:
    def __init__(self,peel):
        self.peel=peel
    def has_a_peel(self):
        return self.peel
class Vegetable:
    def __init__(self,root):
        self.root=root
    def is_a_root(self):
        return self.root
class Checking:
    def does_this_have_a_peel(self):
        result=self.has_a_peel()
        if result:
            print("this has peel")
        else:
            print("this is doesn't have a peel")
    def does_this_have_a_root(self,):
        result=self.is_a_root()
        if result:
            print("this is a root")
        else:
            print("this is not a root")
class Tomato(Checking,Fruit,Vegetable):
    def __init__(self):
        Fruit.__init__(self,True)
        Vegetable.__init__(self,False)
t=Tomato()
print("Tomato")
t.does_this_have_a_peel()
t.does_this_have_a_root()
"""
#3
'''
Create a class called ITEMS which should have all the item names with its code.
Create another class called DETAILS which contains the methods getPrice(int code) and getName(int code) to return the price and name of a particular item code.
Create a class SHOP that inherits the classes ITEMS and DETAILS.
Define the main method that should ask the user to enter the item code and display the product name
and price based on the item code.
'''
"""
class Items:
    def __init__(self):
        self.item_data={1110:{"name":"football","price":499},1120:{"name":"t-shirt","price":599},11300:{"name":"shoe","price":799},1140:{"name":"trousers","price":449}}
class Details:
    def get_price(self,code):
        price=self.item_data[code]["price"]
        print("price:Rs",price)
    def get_name(self,code):
        name=self.item_data[code]["name"]
        print("item-name:",name)
class Shop(Items,Details):
    def __init__(self):
        Items.__init__(self)
obj=Shop()
item_code=int(input("Enter item code:"))
obj.get_name(item_code)
obj.get_price(item_code)
"""
#4
'''
Create a class “Message” consisting of a private string data member “information”.
Write set and get functions for assigning and returning value of the attribute “information”.
Define a class called “Crypto” consisting of a member functions  “Vignere_cipher”
to generate the cipher text. The vignere_cipher technique uses multiple character keys .
Each of the keys encrypts one single character.Each character is replaced by a number (A=0, B=1, …Z=25).
After all keys are used, they are recycled.
For encryption, Formula used : E=(M+K)mod 26 
Plaintext:  ATTACKATDAWN
Key:        LEMONLEMONLE
Ciphertext: LXFOPVEFRNHR 
Define class “Display” to print the cipher text and the plain text (original information). 
'''
"""
class Message:
    def __init__(self):
        self.__information=None
    def set(self):
        info=input("Enter the information:").lower()
        self.__information=info
    def get(self):
        return self.__information
class Crypto:
    def vignere_cipher(self):
        keyword=input("Enter the keyword:").lower()
        info=self.get()
        key=""
        for i in range(len(info)):
            key+=keyword[(i%len(keyword))]
        encrypt="abcdefghijklmnopqrstuvwxyz"
        cipher_text=''
        for i in range(len(info)):
            cipher_text+=encrypt[(encrypt.index(info[i])+encrypt.index(key[i]))%26]
        return cipher_text.upper()
class Display(Message,Crypto):
    def __init__(self):
        Message.__init__(self)
        self.set()
        print("cipher text:",self.vignere_cipher())
        print("plain text:",self.get().upper())
obj=Display()
"""
#5
'''
Define a class “Book” to store the details author, book name, price, status, rack number and edition.
Create display book function to display the details of the book and
an update function to update the details of book.
Create a class called “Librarian” having members name and password.
Define a function search book, return book and issue book.
'''
"""
class Book:
    total_books=0
    books={}
    def __init__(self,author,book_name,price,status,rack_no,edition):
        self.book_name=book_name
        self.author=author
        self.price=price
        self.status=status
        self.rack_no=rack_no
        self.edition=edition
    def display(self):
        print("\nBook name:",self.book_name)
        print("Author:",self.author)
        print("Price:Rs",self.price)
        print("Status:",self.status)
        print("Rack number:",self.rack_no)
        print("Edition:",self.edition)
    def update(self,**data):
        for key,value in data.items():
            self.key=value
    @classmethod
    def add_books(cls,book_obj):
        cls.total_books+=1
        exec(f'cls.books["book"+str(cls.total_books)]=book_obj')
    @classmethod
    def get_books(cls):
        return list(zip(cls.books.keys(),cls.books.values()))
class Librarian:
    def authorize(func):
        def inner(self,*args):
            if self.no_of_calls==0:
                name=input("enter librarian name:")
                password=input("enter your password:")
                if name==self.name and password==self.password:
                    if len(args)==1:
                        func(self,args[0])
                    else:
                        func(self,args[0],args[1],args[2],args[3],args[4],args[5])
            else:
                if len(args)==1:
                        func(self,args[0])
                else:
                        func(self,args[0],args[1],args[2],args[3],args[4],args[5])
        return inner
    def __init__(self,name,password):
        self.no_of_calls=0
        self.name=name
        self.password=password
    @authorize
    def create_book(self,author,book_name,price,status,rack_no,edition):
        self.no_of_calls+=1
        Book.add_books(Book(author,book_name,price,status,rack_no,edition))
    @authorize
    def search_book(self,book_name):
        self.no_of_calls+=1
        all_books=dict(Book.get_books())
        for book_no,book in all_books.items():
            if book.book_name==book_name:
                book.display()
    @authorize
    def return_book(self,book_name):
        self.no_of_calls+=1
        all_books=dict(Book.get_books())
        for book_no,book in all_books.items():
            if book.book_name==book_name:
                book.update(status="availabe")
                print("book returned")
    @authorize
    def issue_book(self,book_name):
        self.no_of_calls+=1
        all_books=dict(Book.get_books())
        for book_no,book in all_books.items():
            if book.book_name==book_name:
                book.update(status="unavilable")
                print("book issued")
librarian_1=Librarian("vimal","vimal@17")
librarian_1.create_book("jk.Rowling","Harry potter",500,"available",44,2)
librarian_1.create_book("George Orwel","1984",400,"available",43,5)
librarian_1.create_book("Kurt Vonnegt","slaughterhouse",600,"available",40,1)
print("\nBooks present:")
book_list=dict(Book.get_books())
for book_no,book in book_list.items():
    print(book.book_name)
print("\nCOMMANDS")
print("1.search book")
print("2.issue book")
print("3.return book")
print("4.stop process")
choice=int(input("enter the number of your choice:"))
print("\n")
while choice!=4:
    book_name=input("enter the name of the book:")
    if(choice==1):
        librarian_1.search_book(book_name)
        print("\n")
    elif(choice==2):
        librarian_1.issue_book(book_name)
    elif(choice==3):
        librarian_1.return_book(book_name)
    choice=int(input("enter the number of your choice:"))
"""
#6
'''
Create a class “Tree” consisting of member functions to create and display a binary search tree.
Write a class “Difference” containing a function absolute
to find the minimum absolute difference between the given two binary search trees.
Define a class “Weight” which assign a weight to each node in the BST.
Write a function exclusive_or to find the node whose node value xor with weight gives the minimum value.
'''
#7
'''
Consider a superclass PurchaseItem which models customer’s purchases. This class has: 
- two variables name (String) and unitPrice (double). 
- One constructor to initialize the instance variables. 
- A default constructor to initialize name to “no item”, and unitPrice to 0 
- A method getPrice that returns the unitPrice. 
Consider two subclasses WeighedItem and CountedItem.
WeighedItem has an additional instance variable weight (double) in Kg
while CountedItem has an additional variable quantity (int). 
- Write an appropriate constructor for each of the classes
making use of the constructor of the superclass to initialize its members. 
- getPrice method that returns the price of the purchasedItem based on its unit price and
weight (WeighedItem), or quantity (CountedItem). Make use of getPrice of the superclass. 
Write an application class where you construct objects from the two subclasses
and print them on the screen. 
'''
"""
class PurchaseItem:
    def __init__(self,name="no item",unit_price=0):
        self.name=name
        self.unit_price=unit_price
    def get_price(self,property_):
        return property_*self.unit_price
class WeightedItem(PurchaseItem):
    def __init__(self,name,unit_price,weight):
        PurchaseItem.__init__(self,name,unit_price)
        self.weight=weight
class CountedItem(PurchaseItem):
    def __init__(self,name,unit_price,quantity):
        PurchaseItem.__init__(self,name,unit_price)
        self.quantity=quantity
tomato=WeightedItem("Tomato",45,1.75)
print("cost of {}kg tomato is Rs {}".format(tomato.weight,tomato.get_price(tomato.weight)))
basket_ball=CountedItem("Basket-ball",399,5)
print("cost of {} basket balls is Rs {}".format(basket_ball.quantity,basket_ball.get_price(basket_ball.quantity)))
"""
#8
'''
Consider a class “Dictionary” to represent a dictionary of words defined as a private data member
and a class “Longest_String” which has a string data member.
Write appropriate functions to receive the input string
and a function “Largest_word” to find the largest word in the dictionary
by deleting some characters of the given string.
Input : dict = {"ale", "apple", "monkey", "plea"}   
        str = "abpcplea"  
Output : apple 
Input  : dict = {"pintu", "geeksfor", "geeksgeeks", "forgeek"} 
         str = "geeksforgeeks"
Output : geeksgeeks
'''
"""
class Dictionary:
    def __init__(self,dict_):
        self.__dict=dict_
    def get_dict(self):
        return list(self.__dict)
class LongestString(Dictionary):
    def __init__(self,string,dict_):
        self.string=string
        Dictionary.__init__(self,dict_)
    def largest_word(self):
        words=self.get_dict()
        matches=0
        result=None
        for i in words:
            current_match=0
            word=list(i)
            string_=list(self.string)
            j=0
            while(j<len(string_)):
                k=0
                while k<len(word):
                    if string_[j]==word[k]:
                        current_match+=1
                        del string_[j]
                        del word[k]
                        j-=1
                        break
                    k+=1
                j+=1
            if matches<current_match:
                matches=current_match
                result=i
        return result
dict_=eval(input("Enter a dictionary:"))
string=input("Enter a string:")
obj_1=LongestString(string,dict_)
print("the largest word:",obj_1.largest_word())
"""
#9
'''
Define a class “Input” containing a set member function to receive input of a integer array.
Write a class “sub-array” consisting of Maximum_subarray function.
This function given an array arr[] of N integers and an integer K
it finds the maximum sub-array sum by flipping signs of at most K array elements.
Input: arr[] = {-6, 2, -1, -1000, 2}, k = 2
Output: 1009
We can flip the signs of -6 and -1000, to get maximum subarray sum as 1009 
Input: arr[] = {-1, -2, -100, -10}, k = 1
Output: 100
We can only flip the sign of -100 to get 100 
Input: {1, 2, 100, 10}, k = 1
Output: 113
We do not need to flip any elements
'''
from itertools import combinations

class Input:
    def __init__(self):
        self.arr=[]
    def set(self,arr):
        self.arr=arr
class SubArray(Input):
    def __init__(self,arr,k):
        Input.__init__(self)
        self.set(arr)
        self.k=k
    def maximum_sub_array(self,arr,k):
        arr=tuple(arr)
        max_sum=0
        for length in range(1,len(arr)+1):
            for sub_arr in combinations(arr,length):
                sum_=sum(sub_arr)
                if max_sum<sum_:
                    max_sum=sum_
        for i in combinations(arr,k):
           modified=list(arr)
           for j in i:
               modified[modified.index(j)]=-modified[modified.index(j)]
           for length in range(1,len(modified)+1):
               for sub_arr in combinations(modified,length):
                   sum_=sum(sub_arr)
                   if max_sum<sum_:
                       max_sum=sum_
        return max_sum
arr=eval(input("Enter a array of integers:"))
k=int(input("Enter the value of k:"))
obj=SubArray(arr,k)
print("maximum sum:",obj.maximum_sub_array(obj.arr,obj.k))
