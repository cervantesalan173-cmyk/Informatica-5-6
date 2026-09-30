def main():
    not_validated = True # Initialization

    while not_validated: #condition
        try:
            number = int(input("Enter a number between 1 nd 10: "))
            if number >= 1 and number <= 10:
                print("Succesful !")
                not_validated = False
        except ValueError:
            print("You must enter a number between 1 and 10.")

        name = input("Enter name: ")

        while name  == " ":
            name = input("Enter a name: ")
        print()


if __name__ =="__main__":
    main()

