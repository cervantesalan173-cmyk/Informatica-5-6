import random

def main():
    start_game("hangman.txt")
def start_game(file):
        attempts = 10
        with open(file) as f:
            word_bank = f.read().splitlines()

        word = random.choice(word_bank)
        hint = len(word)
        content = ["_"] * len(word)
        incorrect_letters = []
        while attempts > 0:
             print("current word:", " ".join(hint))



        while True:
            guess = input("Take a guess: ").lower
            print(len(guess))
            if len(guess) == 1:
                break
            else:
                print("Invalid guess, try again.")

            if guess in word and guess not in hint:
                for i in range(len(word)):
                    if word[i] == guess:
                        hint[i] = guess
                print("Great guess!")
            elif guess in hint:
                attempts -= 1
                print("Your already guessed that letter! Attempts left:", str(attempts))
            else:
                attempts -= 1
                print("Wrong guess! Attempts left:", str(attempts))
                if guess not in incorrect_letters:
                    incorrect_letters.append(guess)
                    print(f"incorrects letters: {" ".join(incorrect_letters)}")

            if "_" not in hint:
                print("Congratulations! you guessed the word:", word)
                break

            if attempts == 0 and "_" in hint:
                print("No attempts left the word was:", word)






if __name__ == "__main__":
    main()
