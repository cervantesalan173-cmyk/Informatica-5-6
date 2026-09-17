def main():

    tasks = []

    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)
        command = input("What do you want to do? (add, complete, exit): ")
        if command == "add":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
        elif command == "complete":
            new_task = input("What task shall we destroy?: ")
            tasks.remove(new_task)
        elif command == "exit":
            break

if __name__ == "__main__":
    main()
