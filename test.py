"""def dec(fun):
    print("hlw")
    def inner():
        print("hi")
        fun()
    return inner
@dec
def hello():
    print("hoi")
@dec
def outer():
    print("in outer")
    def in1():
        print("in1")
    
print(dec)
print(hello)
print(outer)"""
'''class c:
    def dec(fun):
        print("hlw")
        def inner(s):
            print("hi")
            fun(s)
        return inner
    @dec
    def hey(s):
        print("ntg",s)
    def hey1(a):
        print("ntg 1",a)
    def hey2(b):
        print("ntg 2",b)
c1=c()
c1.hey()
c1.hey1()
c1.hey2()
'''
'''#try :
#    raise ValueError
#except ValueError:
#    print(ValueError)
class a:
    @staticmethod
    def hello():
        print("hello")
class b:
    @staticmethod
    def call_hello():
        Parent.hello()
b1=b()
b1.call_hello()
'''
"""
s="class was really _ today. We learned how to _ today in class. I can't wait for tomorrow's class!"
l=['calc','happy','badminton']
#j=0
#count=s.count("_")
for i in range(3):
    s=s.replace("_",l[i],1)
#for i in s:
#    if i=="_":
#        s=s.replace("_",l[j],1)
#        j+=1
print(s)
"""
'''
def isprime(num):
    check=0
    if num==2:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
                check=1
                return False
        if check==0:
            return True
n=20
l=[]
numbers=2
while len(l)!=20:
    result=isprime(numbers)
    if result:
        l.append(numbers)
    numbers+=1
print(l)
'''
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
            print("Prime number found")
        else:
            print("Prime number not found")
n=int(input("Enter a number"))
pr=SimpleTester()
pr.prime(n)


