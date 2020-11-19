import random


questions = [
    "I trust my intuition.\n(a) yes\n(b) no",
    "Before taking any risk, I make sure to have a Plan B ready.\n(a) Yes \n(b) No\n",
    "I have always been able to anticipate when something bad was going to happen.\n(a) Yes\n(b) No\n",
    "I adapt quickly to new surroundings. \n(a) yes\n(b) no",
    "I assess pros and cons before acting. \n(a) yes\n(b) no",
    "I trust my intuition?\n(a) yes\n(b) no",
    "I am good at thinking on my feet.\n(a) yes\n(b) no",
    "It doesn't take me long to orient myself in a new city. \n(a) yes\n(b) no",
    "I trust my intuition?\n(a) yes\n(b) no",
]
count = 0

response1 = input(questions[0]).lower()
if response1 == 'a' or response1 =='A':
    print("Next Question")
    count+=1
else:
    print("Next Question")

response2 = input(questions[1]).lower()
if response2 == 'a' or response2 =='A':
    print("Next Question")
    count+=1
else:
    print("Next Question")

response3 = input(questions[2]).lower()
if response3 == 'a' or response3 =='A':
    print("Next Question")
    count+=1
else:
    print("Next Question")

response4 = input(questions[3]).lower()
if response4 == 'a' or response4 =='A':
    print("Next Question")
    count+=1
else:
    print("Next Question")

response5 = input(questions[4]).lower()
if response5 == 'a' or response5 =='A':
    print("Next Question")
    count+=1
else:
    print("Next Question")

response6 = input(questions[5]).lower()
if response6 == 'a' or response6 =='A':
    print("Next Question")
    count+=1
else:
    print("Next Question")

response7 = input(questions[6]).lower()
if response7 == 'a' or response7 =='A':
    print("Next Question")
    count+=1
else:
    print("Next Question")

response8 = input(questions[7]).lower()
if response8 == 'a' or response8 =='A':
    print("Next Question")
    count+=1
else:
    print("Next Question")

response9 = input(questions[8]).lower()
if response9 == 'a' or response9 =='A':
    print("Next Question")
    count+=1
else:
    print("Next Question")


   
grade = count/9
grade_percent = "{:.0%}".format(grade)

print(f"You are {grade_percent} street smart")


