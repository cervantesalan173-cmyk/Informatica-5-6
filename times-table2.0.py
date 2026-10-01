def main():
    valid_nums = []
    for i in range(1,11):
        valid_nums.append(str(i))
    ala = True
    while ala:
        try:
            number = int(input("select a number you would like to be tested on: "))
            ala = False
        except ValueError:
             print("Invalid")



    alan = True
    while alan:
        try:
            max_value = int(input("Enter maximum value for the times table: "))
            alan = False
        except ValueError:



            print(f"Here is the {number} times table")


    for i in range(1, max_value + 1):
                tatortot = i * int(number)
                ans = int(input(f"{i} times {number} is... "))
                if ans == tatortot:
                     print("Correct")
                elif ans != tatortot:
                     print("Incorrect")



if __name__ =="__main__":
    main()
