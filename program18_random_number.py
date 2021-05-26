import random

guessNumber = int(input("Enter your guess between 1 to 5 : "))
randomNumber = random.randint(1, 5)
#randomNumber = random.random() * 5 + 1

if guessNumber == randomNumber:
    print("You have won")
else:
    print("You have lost")
    print("Random number was:", randomNumber)
