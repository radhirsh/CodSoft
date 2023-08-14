chores = []
filename = "chores.txt"

try:
    with open(filename, "r") as file:
        chores = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    pass

while True:
    print("Welcome to Taskiee!")
    print("Choose an action:")
    print("1. View Chores")
    print("2. Add Chore")
    print("3. Mark Chore as done")
    print("4. Delete Chore")
    print("5. Save and exit")

    option = input("Select an option (1-5): ")

    if option == '1':
        if not chores:
            print("No chores in the list.")
        else:
            print("Chores:")
            for index, chore in enumerate(chores, start=1):
                print(f"{index}. {chore}")
    elif option == '2':
        chore = input("Enter the chore: ")
        chores.append(chore)
        print("Chore added:", chore)
    elif option == '3':
        index = int(input("Enter the index.No of the chore to mark as done: "))
        if 1 <= index <= len(chores):
            chores[index - 1] += " (Done)"
            print("Chore marked as done.")
        else:
            print("Invalid index.")
    elif option == '4':
        index = int(input("Enter the index.No of the chore to delete: "))
        if 1 <= index <= len(chores):
            deleted_chore = chores.pop(index - 1)
            print("Chore deleted:", deleted_chore)
        else:
            print("Invalid index.")
    elif option == '5':
        with open(filename, "w") as file:
            for chore in chores:
                file.write(chore + "\n")
        print("Chores saved. Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option in between 1-5.")
