import random

def main():
     largest("hangman.txt")
def largest(file):
        with open(file) as number_file:
            content = number_file.read().splitlines()

        word1 = random.choice(content)
        count = len(word1)
        content = ["_"] * count
        print(" ".join(count))


        while True:
            guess = input("Take a guess: ")
            print(len(guess))
            if len(guess) == 1:
                break
            else:
                print("Invalid guess, try again.")

        for





if __name__ == "__main__":
    main()
