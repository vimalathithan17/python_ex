#1
'''1. Write a program that asks the user to enter a string. The program should then print 
the following:
a. The total number of characters in the string
b. The string repeated 10 times
c. The first character of the string (remember that string indices start at 0)
d. The first three characters of the string
e. The last three characters of the string
f. The string backwards
g. The seventh character of the string if the string is long enough and a message 
otherwise
h. The string with its first and last characters removed
i. The string in all caps
j. The string with every a replaced with an e
k. The string with every letter replaced by a space'''

"""
string=input("enter a string:")
length=len(string)
print("length of the string is",length)
print(f"string repeated 1 times:{string*length}")
print(f"first character:{string[0]}")
print(f"first three characters:{string[:3]}")
print(f"last 3 characters:{string[length-3:length]}")
print(f"string backwards:{string[-1]}")
if length>=7:
    print(f"seventh character:{srting[6]}")
else:
    print("string has less than 7 characters")
print(f"sting with 1st and last characters removed:{string[1:length-1]}")
print(f"string in all caps:{string.upper()}")
print(f"strin eith every 'a' repalced with 'e':{string.replace('a','e')}")
string=""
string+=(" "*length)
print(f"string with every letter replaced by a space:{string}")
"""
#2
'''
 A simple way to estimate the number of words in a string is to count the number of 
spaces in the string. Write a program that asks the user for a string and returns an 
estimate of how many words are in the string
'''
"""
sentence=input("Enter a sentence:")
number_of_words=sentence.count(" ")+1
print("number of words in the given sentence is:",number_of_words)
"""
#3
'''
People often forget closing parentheses when entering formulas. Write a program that 
asks the user to enter a formula and prints out whether the formula has the same 
number of opening and closing parentheses.
'''
"""
formula=input("enter a formula:")
if(formula.count("(")==formula.count(")")):
    print("yes")
else:
    print("no")
"""
#4
'''
Write a program that asks the user to enter a word and prints out whether that word 
contains any vowels.
'''
"""
word=input("enter a word:")
word=word.lower()
count=0
for letter in word:
    if letter in "aeiou":
        print("the word contains vowels")
        count=1
        break
if count==0:
    print("the word dosen't contain any vowels")
"""
#5
'''
Write a program that asks the user to enter a string. The program should create a new 
string called new_string from the user's string such that the second character is 
changed to an asterisk and three exclamation points are attached to the end of the 
string. Finally, print new_string. Typical output is shown below:
'''
"""
input_string=input("enter a string:")
new_string=input_string.replace(input_string[1],'*')+"!!!"
print(new_string)
"""
#6
'''
Write a program that asks the user to enter a string s and then converts s to lowercase, 
removes all the periods and commas from s, and prints the resulting string.
'''
"""
s=input("enter a string:")
s=s.lower()
s=s.replace('.','')
s=s.replace(",","")
print(s)
"""
#15
'''
When I was a kid, we used to play this game called Mad Libs. The way it worked was 
a friend would ask me for some words and then insert those words into a story at 
specific places and read the story. The story would often turn out to be pretty funny 
with the words I had given since I had no idea what the story was about. The words 
were usually from a specific category, like a place, an animal, etc. For this problem 
you will write a Mad Libs program. First, you should make up a story and leave out 
some words of the story. Your program should ask the user to enter some words and 
tell them what types of words to enter. Then print the full story along with the inserted 
words. Here is a small example, but you should use your own (longer) example:
'''
"""
story='''_ class was really _ today. We learned how to
_ today in class. I can't wait for
tomorrow's class!'''
story_list=story.split()
first_=input('Enter a college class:')
second_=input('Enter an adjective:')
third_=input('Enter an activity:')
replace_list=[first_,second_,third_]
j=0
for i in range(len(story_list)):
    if story_list[i]=='_':
        story_list[i]=replace_list[j]
        j+=1
story=" ".join(story_list)
print(story)
"""
