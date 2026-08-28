def main():
    password = "alan1234"

    attempt = input("enter your password: ")
    if  attempt == password:
        print("Correct password. ")
    elif attempt != password:
        print("incorrect password. ")
    
        print("see you later. ")



if __name__ == "__main__":
    main()
