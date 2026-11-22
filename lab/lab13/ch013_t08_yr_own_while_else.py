from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
secret = randint(1, 10)

guesses_left = 3

while guesses_left > 0:
    guess = int(input("Your guess: "))
    
    if guess == secret:
        print("You win!")
        break
    
    guesses_left -= 1
else:
    # This block only runs if the while loop finished normally
    # (i.e. we never hit `break`)
    print("You lose.")