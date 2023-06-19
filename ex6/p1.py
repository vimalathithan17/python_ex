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
"""
class Wordplay:
    @staticmethod
    def removes(result,string):
        if None in result:
            result=list(set(result))
            result.remove(None)
            if len(result)==0:
                return "there are no words "+string
            else:
                return result
        elif len(result)==0:
            return "there are no words "+string
        else:
            return result
    def __init__(self,words):
        self.word_list=[]+words
    def words_with_length(self,length):
        result = list(map(lambda x:x if len(x)==length else None,self.word_list))
        result=Wordplay.removes(result,f"that has length {length}")
        return result
    def starts_with(self,s):
        result=list(map(lambda x:x if x[0]==s else None,self.word_list))
        result=Wordplay.removes(result,f"that starts with '{s}'")
        return result
    def ends_with(self,s):
        result=list(map(lambda x:x if x[-1]==s else None,self.word_list))
        result=Wordplay.removes(result,f"that ends with '{s}'")
        return result
    def palindromes(self):
        result=list(map(lambda x:x if x==x[::-1] else None,self.word_list))
        result=Wordplay.removes(result,"that are palindrome")
        return result
    def only(self,l):
        l_="".join(list(l))
        l="".join(sorted(list(set(l))))
        result=[]
        for word in self.word_list:
            word_="".join(sorted(list(set(word))))
            if l==word_:
                result.append(word)
        result=Wordplay.removes(result,f"that only contain the letters in '{l_}'")
        return result
    def avoids(self,l):
        l_="".join(list(l))
        l="".join(sorted(list(set(l))))
        result=[]
        for word in self.word_list:
            word_="".join(sorted(list(set(word))))
            if l not in word_:
                result.append(word)
        result=Wordplay.removes(result,f"that dosent contain any of the letters in '{l_}'")
        return result
words=eval(input("Enter a list of word:"))
c=Wordplay(words)
length=int(input("Enter a length:"))
print(f"the words with length {length} are ",c.words_with_length(length))
starting_letter=input("Enter the a character:")
print(f"the words which start with letter {starting_letter} are:",c.starts_with(starting_letter))
ending_letter=input("Enter the a character:")
print(f"the words which ends with letter {ending_letter} are:",c.ends_with(ending_letter))
print("the palindromes are:",c.palindromes())
a_word=input("Enter a Word:")
print(f"the words that only cointain the letters in '{a_word}' are:",c.only(a_word))
print(f"the words that does not cointain any of the letters in '{a_word}' are:",c.avoids(a_word))
"""
#6
'''
Write a class called Converter. The user will pass a length and a unit when declaring 
an object from the class—for example, c = Converter(9, 'inches'). The possible 
units are inches, feet, yards, miles, kilometers, meters, centimeters, and millimeters. 
For each of these units there should be a method that returns the length converted 
into those units. For example, using the Converter object created above, the user 
could call c.feet() and should get 0.75 as the result
'''
"""
class Converter:
    def __init__(self,value,unit):
        self.value=value
        self.unit=unit
    def inches(self):
        value_in_meters=self.meters(intermediate=True)
        return 'the equivalent of {} {} is {} inches'.format(self.value,self.unit,value_in_meters*39.37)
    def feet(self):
        value_in_meters=self.meters(intermediate=True)
        return 'the equivalent of {} {} is {} feet'.format(self.value,self.unit,value_in_meters*3.2808)
    def yards(self):
        value_in_meters=self.meters(intermediate=True)
        return 'the equivalent of {} {} is {} yards'.format(self.value,self.unit,value_in_meters*1.0936)
    def miles(self): 
        value_in_meters=self.meters(intermediate=True)
        return 'the equivalent of {} {} is {} miles'.format(self.value,self.unit,value_in_meters*0.000621)
    def kilometers(self):
        value_in_meters=self.meters(intermediate=True)
        return 'the equivalent of {} {} is {} kilometers'.format(self.value,self.unit,value_in_meters*0.001)
    def meters(self,intermediate=False):
        conversion_factor={"inches":0.0254,"feet":0.3048,"yards":0.9144,"miles":1609.344,"kilometers":1000,"metres":1,"centimeters":0.01,"millimeters":0.001}
        if intermediate:
            return self.value*conversion_factor[self.unit]
        else:
            return 'the equivalent of {} {} is {} meters'.format(self.value,self.unit,self.value*conversion_factor[self.unit])
    def centimeters(self):
        value_in_meters=self.meters(intermediate=True)
        return 'the equivalent of {} {} is {} centimeters'.format(self.value,self.unit,value_in_meters*100)
    def millimeters(self):
        value_in_meters=self.meters(intermediate=True)
        return 'the equivalent of {} {} is {} millimeters'.format(self.value,self.unit,value_in_meters*1000)
print("Converter")
print("the available units are:")
print("1.inches")
print("2.feet")
print("3.yards")
print("4.miles")
print("5.kilometers")
print("6.meters")
print("7.centimeters")
print("8.millimeters")
value,unit=input("enter the value and unit seperated by a space:").split()
convert_to=input("wnter the unit to which you want to convert the above value to:")
c=Converter(float(value),unit)
print(getattr(c,convert_to)())
"""
#7
'''
Use the Standard_deck class of this section to create a simplified version of the 
game War. In this game, there are two players. Each starts with half of a deck. The 
players each deal the top card from their decks and whoever has the higher card wins 
the other player's cards and adds them to the bottom of his deck. If there is a tie, the 
two cards are eliminated from play (this differs from the actual game, but is simpler 
to program). The game ends when one player runs out of cards.
'''
"""
class Card:
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
    def __str__(self):
        names=["Jack","Queen","King","Ace"]
        if self.value <= 10:
            return '{} of {} '.format(self.value,self.suit)
        else:
            return '{} of {} '.format(names[self.value-11],self.suit)
import random
class CardGroup:
    def __init__(self,cards=[]):
        self.cards=cards
    def next_card(self):
        return self.cards.pop(0)
    def has_card(self):
        return len(self.cards)>0
    def size(self):
        return len(self.cards)
    def shuffle(self):
        random.shuffle(self.cards)
class StandardDeck(CardGroup):
    def __init__(self):
        self.cards=[]
        for s in ["Hearts","Diamonds","Clubs","Spades"]:
            for v in range(2,15):
                self.cards.append(Card(v,s))
class War(StandardDeck):
    def __init__(self):
        StandardDeck.__init__(self)
        class Players(CardGroup):
            def __init__(p_self):
                p_self.mycards=[]
            def create_group(p_self):
                CardGroup.__init__(p_self,p_self.mycards)
                
        self.player=Players()
        self.computer=Players()
        CardGroup.__init__(self,self.cards)
        self.shuffle()
        for i in range(len(self.cards)):
            if i%2==0:
                self.player.mycards.append(self.cards[i])
                
            else:
                self.computer.mycards.append(self.cards[i])
        self.player.create_group()
        self.computer.create_group()
    def start(self):
        while len(self.player.mycards)!=0 and len(self.computer.mycards):
            input("Hit enter to know your card")
            player_card=self.player.next_card()
            computer_card=self.computer.next_card()
            print("you:",player_card)
            print("computer's card:",computer_card)
            if player_card.value == computer_card.value:
                print("draw")
            elif player_card.value > computer_card.value:
                print("you win this round!")
                self.player.mycards.append(player_card)
                self.player.mycards.append(computer_card)
            elif player_card.value < computer_card.value:
                print("you loose this round")
                self.computer.mycards.append(computer_card)
                self.computer.mycards.append(player_card)
        if len(self.player.mycards)==0 and len(self.computer.mycards)==0:
            print("war draw")
        elif len(self.player.mycards)>0:
            print("you win the war!!!")
        elif len(self.player.mycards)==0:
            print("you loose the war!!!")
war1=War()
war1.start()
"""
#8
'''
Write a class that inherits from the Card_group class of this chapter. The class should 
represent a deck of cards that contains only hearts and spaces, with only the cards 2 
through 10 in each suit. Add a method to the class called next2 that returns the top 
two cards from the deck.
'''
"""
class Card:
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
    def __str__(self):
        names=["Jack","Queen","King","Ace"]
        if self.value <= 10:
            return '{} of {} '.format(self.value,self.suit)
        else:
            return '{} of {} '.format(names[self.value-11],self.suit)
import random
class CardGroup:
    def __init__(self,cards=[]):
        self.cards=cards
    def next_card(self):
        return self.cards.pop(0)
    def has_card(self):
        return len(self.cards)>0
    def size(self):
        return len(self.cards)
    def shuffle(self):
        random.shuffle(self.cards)
class Deck(CardGroup):
    def __init__(self):
        suits=["Hearts","Spades"]
        CardGroup.__init__(self)
        for suit in suits:
            for number in range(2,11):
                self.cards.append(Card(number,suit))
        self.shuffle()
    def next2(self):
        return [self.cards[0],self.cards[1]]
new_deck=Deck()
card_1,card_2=new_deck.next2()
print("the top 2 cards in the deck are:")
print(card_1,card_2,sep=",")
"""
#9
'''
Write a class called Rock_paper_scissors that implements the logic of the game 
Rock-paper-scissors. For this game the user plays against the computer for a certain 
number of rounds. Your class should have fields for the how many rounds there will 
be, the current round number, and the number of wins each player has. There should 
be methods for getting the computer's choice, finding the winner of a round, and 
checking to see if someone has one the (entire) game. You may want more methods.
'''
"""
from random import choice
class RockPaperScissors:
    choices=["rock","paper","scissors"]
    def __init__(self,rounds):
        self.rounds=rounds
        self.current_round=0
        self.player_wins=0
        self.computer_wins=0
    @staticmethod
    def get_computer_choice():
        return choice([0,1,2])
    def find_round_winner(self):
        self.current_round+=1
        print("round {} of {}".format(self.current_round,self.rounds))
        computer=RockPaperScissors.get_computer_choice()
        player=int(input("enter the number corresponding to your choice:"))
        print("computer:{}\nyou:{}".format(RockPaperScissors.choices[computer],RockPaperScissors.choices[player]))
        if computer==player:
            return "draw"
        elif RockPaperScissors.choices[computer]=="rock" and RockPaperScissors.choices[player]=="paper":
            self.player_wins+=1
            return "you win the round!"
        elif RockPaperScissors.choices[computer]=="paper" and RockPaperScissors.choices[player]=="scissors":
            self.player_wins+=1
            return "you win the round!"
        elif RockPaperScissors.choices[computer]=="scissors" and RockPaperScissors.choices[player]=="rock":
            self.player_wins+=1
            return "you win the round!"
        elif RockPaperScissors.choices[player]=="rock" and RockPaperScissors.choices[computer]=="paper":
            self.computer_wins+=1
            return "you loose the round!"
        elif RockPaperScissors.choices[player]=="paper" and RockPaperScissors.choices[computer]=="scissors":
            self.computer_wins+=1
            return "you loose the round!"
        elif RockPaperScissors.choices[player]=="scissors" and RockPaperScissors.choices[computer]=="rock":
            self.computer_wins+=1
            return "you loose the round!"
    def winner(self):
        if self.player_wins==self.computer_wins:
            return "game draw"
        elif self.player_wins>self.computer_wins:
            return "you win the game!!!"
        elif self.player_wins<self.computer_wins:
            return "computer wins the game!!"
rounds=int(input("enter the total number of rounds:"))
game=RockPaperScissors(rounds)
print("\nenter:\n0 for rock \n1 for paper \n2 for scissors\n")
while game.current_round<game.rounds:
    print(game.find_round_winner())
print(game.winner())
"""
#10
'''
a. Write a class called Connect4 that implements the logic of a Connect4 game. 
Use the Tic_tac_toe class from this chapter as a starting point.
b. Use the Connect4 class to create a simple text-based version of the game.
'''
"""
class tic_tac_toe:
    def __init__(self):
        self.b=[[0,0,0],[0,0,0],[0,0,0]]
        self.player=1
    def get_open_spots(self):
        return [[r,c] for r in range(3) for c in range(3) if self.b[r][c]==0]
    def is_valid_move(self,r,c):
        if 0<=r<=2 and 0<=c<=2 and self.b[r][c]==0:
            return True
        return False
    def make_moves(self,r,c):
        if self.is_valid_move(r,c):
            self.b[r][c]=self.player
            self.player=(self.player+2)%2+1
    def check_for_winner(self):
        for c in range(3):
            if self.b[0][c]==self.b[1][c]==self.b[2][c]!=0:
                return self.b[0][c]
        for r in range(3):
            if self.b[r][0]==self.b[r][1]==self.b[r][2]!=0:
                return self.b[r][0]
        if self.b[0][0]==self.b[1][1]==self.b[2][2]!=0:
                return self.b[0][0]
        if self.b[2][0]==self.b[1][1]==self.b[0][2]!=0:
                return self.b[2][0]
        if self.get_open_spots()==[]:
                return 0
        return -1
def print_board():
    chars=['-','x','o']
    for r in range(3):
        for c in range(3):
            print(chars[game.b[r][c]],end=" ")
        print("")
game=tic_tac_toe()
while game.check_for_winner()==-1:
    print_board()
    r,c=eval(input('enter spot,player '+str(game.player)+": "))
    game.make_moves(r,c)
print_board()
x=game.check_for_winner()
if x==0:
    print("It's a draw")
else:
    print(f"player {x} wins")
"""
