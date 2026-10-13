import random

def main():
     largest("hangman.txt")
def largest(file):
        with open(file) as number_file:
            content = number_file.read().splitlines()
            word1 = random.choice(content)
            print(word1)





if __name__ == "__main__":
    main()
