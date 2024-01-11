#Convert the 0 into a number so we can add scores
score = 0
score = int(score)
print(""" welcome to Quiz night! 
You will be presented with 5 questions.
Enter the appropriate number to answer the question
Good luck!""")

#Question1
print("what is a baby kangaroo called? \n 1.calf \n 2. puppy \n 3.joey \n 4.kitten \n")

answer1 = "3"
response1 = input("Your answer is:")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
    print("the correct answer is joey")
else:
    print("Well done! " + response1 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question2
print("how many players are in a soccer team? \n 1.eleven \n 2.fifteen \n 3.twenty two \n 4.nine \n")

answer2 = "1"
response2 = input("Your answer is:")

if (response2 != answer2):
    print("Sorry, that is incorrect!")
    print("the correct answer is eleven")
else:
    print("Well done! " + response2 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question3
print("What is the name of a shape with 5 sides?\n 1.circle \n 2.triangle \n 3.square \n 4.pentagon \n")

answer3 = "4"
response3 = input("Your answer is:")

if (response3 != answer3):
    print("Sorry, that is incorrect!")
    print("the correct answer is pentagon")
else:
    print("Well done! " + response3 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question4
print("the language spoken by the pepole by pakistan is?\n 1.hindi \n 2.palauan \n 3.sindhi \n 4.nauruan \n")

answer4 = "3"
response4 = input("Your answer is:")

if (response4 != answer4):
    print("Sorry, that is incorrect!")
    print("the correct answer is sindhi")
else:
    print("Well done! " + response4 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question5
print("which planet is known as the Red planet?\n 1.venus \n 2.mars \n 3.saturn \n 4. jupiter \n")

answer5 = "2"
response5 = input("Your answer is:")

if (response5 != answer5):
    print("Sorry, that is incorrect!")
    print("the correct answer is mars")
else:
    print("Well done! " + response5 + " is correct!")
    score = score + 1

print("Your total score is " + str(score) + " out of 5")
print("Thank you for playing,goodbye!")
