def main():
    # planet = input("planet:")

    # # Separation
    # print("Hello", planet)

    # # Concatenation
    # print("Hello " + planet)

    # # Formatted Strings
    # print(f"Hello {planet}")

    # # Ending
    # print("Hello", end=" ")
    # print(planet)

    name = input("what is your name? ").strip().title()
    color =  input("tell me a color: ").strip().lower()
    adjective = input("tell me an adjective: ").strip().lower()
    goal = input("a goal you would like to achieve: ").strip().lower()

    print(f"hello, {name}!", end="\n\n")

    print("this is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.")
    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.".upper())
if __name__ == "__main__":
    main()

