def main():
    print("Los pollos hermanos family!")

    rating = float(input("rate our service from 0 to 5!: "))

    if rating >= 4.5:
        print("Perfetcion!")
    elif rating > 4:
        print("Excellent!")
    elif rating > 3:
        print("Good")
    elif rating > 2:
        print("Fair")
    else:
        print("poor")



if __name__ == "__main__":
    main()
