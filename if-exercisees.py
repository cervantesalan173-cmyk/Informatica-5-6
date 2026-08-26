def main():
    integer = int(input("give me an integer number: "))
    if integer < 0:
        print(integer * -1)
    elif integer > 0:
        print(integer)


if __name__ == "__main__":
    main()
