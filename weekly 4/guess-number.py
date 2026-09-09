import random
def main():
    name = input("Hello! What is your name?")
    print(f"Well, {name},  I am thinking of a number between 1 and 100. Take a guess.")


    guess = 0 #initialize
    number = random.randint(1, 100)



    while guess != number:
        guess = int(input("Take a guess: "))
        if guess > number:
            print("Your guess is too high.")
        elif guess < number:
            print("Your guess is too low.")



    print(f"Good job, {name}! You guessed my number!")

    if guess == number:
        print("You win")


if __name__ == "__main__":
    main()





