import random
def main():
    print("Welcome to my learning app")
    print("I will now give you some problems for you to solve")


    #print(f"what is {num1} + {num2}?")
    streak = 0
    while streak < 3:

        input(f"what is {num1} + {num2}?")

        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)



        if ans != num1+ num2:
            print("INCORRECT")

        elif ans == num1 + num2:
            print("CORRECT")

            streak += 1




if __name__ == "__main__":
    main()
