def main():
    not_validated = True # Initialization

    while not_validated: #condition
        try:
            number = int(input("Enter a number between 1 nd 10: "))
            if number >= 1 and number <= 10:
                print("Succesful !")
                not_validated = False #-->
        except ValueError:
            print("You must enter a number between 1 and 10.")

                                                #name = input("Enter name: ")
                                                 #print(name[0])

    while True:
        try:                                                 #while name  == " ":
            name = input("Enter a name: ")
            f_letter = name[0]
            print("Name stored successfully.")
            break
        except IndexError:
            print("You MUST enter your name.")


if __name__ =="__main__":
    main()

