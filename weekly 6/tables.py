def main():
    valid_nums = []
    for i in range(1,11):
        valid_nums.append(str(i))

    while True:
        number = input("select a number from 1-10 or exit: ").lower().strip()

        if number == "exit":
             break

        elif number in valid_nums:
            max_value = int(input("Enter maximum value for the times table: "))


            print(f"Here is the {number} times table")


            for i in range(1, max_value + 1):
                       tatortot = i * int(number)
                       print(f"{i} times {number} is {tatortot}")

            else:
                 print("Invalid command.")



if __name__ =="__main__":
    main()
