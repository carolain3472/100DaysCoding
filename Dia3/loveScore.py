#You are going to write a program that tests the compatibility between two people.

#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 

#Then combine these numbers to make a 2 digit number.

#For Love Scores less than 10 or greater than 90, the message should be:

#"Your score is **x**, you go together like coke and mentos."
#For Love Scores between 40 and 50, the message should be:

#"Your score is **y**, you are alright together."
#Otherwise, the message will just be their score. e.g.:

#"Your score is **z**."

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

nombre1= name1.lower()
nombre2= name2.lower()

combinarNombres= nombre1+nombre2

t=combinarNombres.count("t")
r=combinarNombres.count("r")
u=combinarNombres.count("u")
e=combinarNombres.count("e")

totalTrue= str(t+r+u+e)

l=combinarNombres.count("l")
o=combinarNombres.count("o")
v=combinarNombres.count("v")
e=combinarNombres.count("e")

totalLove= str(l+o+v+e)
loveScore= int(totalTrue+totalLove)


if loveScore<10 or loveScore>90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore>=40 and loveScore<=50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")
