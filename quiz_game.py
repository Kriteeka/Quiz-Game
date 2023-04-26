print("Welcome to the Quiz Game")
playing = input("Do you wanna play? ")

if playing.lower() != "yes":  #lower() -> it changes every letter to lower case
    quit()
else:
    print("Okayy Let's Play!")
    score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("That's the correct answer!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("That's the correct answer!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("That's the correct answer!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply":
    print("That's the correct answer!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%")


