import random
print("NUMBER GUESSING GAME")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 to 9")
while chances<5:
    firstString = int(input("ENter your guess: "))
    if (firstString == number):
        print("Congratulations! You guessed correctly!")
        break    
    
    elif(firstString < number):
        print("Your guess was too low! Guess a number higher than", firstString)
    
    else:
        print("Your guess was too high! Guess a number lower than", firstString)
    
    chances = chances + 1
if (chanceCount > 5):
    print("Sorry! You lose! The number is", number)
