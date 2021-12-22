import random

def guess(x):
    random_number = random.randint(1, x)

    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number b/w 1 and {x} \n"))
        if (guess == random_number):
            print(f"Yay, congrats. You have guessed the number {random_number} correctly!!")
            break
        elif (guess > random_number):
            print("Sorry, guess again. Too high.")
        else:
            print("Sorry, guess again. Too low.")


if __name__=="__main__":
    guess(15)
