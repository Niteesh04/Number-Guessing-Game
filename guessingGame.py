import random
print("Number Guessing Game")
number=random.randint(1,9)
chances=0
print("Guess A Number Between 1 & 9")
while chances < 5:
    guess=int(input("Enter Your Guess"))
    if guess == number:
        print("Congratulations You Won")
    elif guess < number:
        print("Your Guess Was Too Low, Guess A Higher Number")
    else:
         print("Your Guess Was Too High, Guess A Lower Number")
    chances += 1
if not chances < 5:
    print("You Lose, The Number Is",number)