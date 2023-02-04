print('''
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
''')
print("      Welcome to the Love Calculator ! \n")

name1 = input("What is your name : ")
name2 = input("What is their name : ")

combined_name = name1+name2
lower_case = combined_name.lower()
t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
true = t+r+u+e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
love = l+o+v+e

love_score = int(str(true) + str(love))
if love_score < 10 or love_score > 90:
    print(
        f"Your love score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
