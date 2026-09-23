def main():
    while True:
        number = int(input("select a number from 1-10: "))
        if number <= 10:
            if number > 0:
                    for i in range(10):
                       tatortot = i * number
                       print(f"{i} times {number} is {tatortot}")

if __name__ =="__main__":
    main()
