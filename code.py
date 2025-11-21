medicines = []
def add_medicine():
    name = input("Enter medicine name: ")
    dosage = input("Enter dosage (e.g., 1 tablet): ")
    time = input("Enter time to take (e.g., 9 AM): ")
    med = {
        "name": name,
        "dosage": dosage,
        "time": time
    }
    medicines.append(med)
    print("Medicine added.\n")
def show_medicines():
    if not medicines:
        print("No medicines added yet.\n")
        return
    print("\nYour Medicine Schedule:")
    for m in medicines:
        print("Name:", m["name"])
        print("Dosage:", m["dosage"])
        print("Time:", m["time"])
        print("----------------------")
    print()
while True:
    print("1. Add Medicine")
    print("2. Show All Medicines")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_medicine()
    elif choice == "2":
        show_medicines()
    elif choice == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid option.\n")
