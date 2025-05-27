def the_menu():
    print("\n------Rover Repair log------")
    print("1. Log a repair")
    print("2. View repair log")
    print("3. Exit program")

def log_repair():
    print("\n----Log a repair----")
    rov_id = input("Enter rover ID: ")
    iss = input("Issue with rover: ")
    fix = input("Fix for issue: ")
    with open("Repairs.txt", "a") as fi:
        fi.write(f"Rover ID: {rov_id} | Issue: {iss} | Fix: {fix} \n")
    print("Repair logged.")

def repair_viewer():
    try:
        with open("Repairs.txt", "r") as fi:
            log = fi.readlines()
            if log:
                print("\n----Repair Logs----")
                for entry in log:
                    print(entry.strip())
            else:
                 print("No repairs logged.")
    except FileNotFoundError:
        print("No repairs logged")

def main_thing():
    while True:
        the_menu()
        big_choice = input("Select an option (1-3): ")
        if big_choice == "1": 
             log_repair()
        elif big_choice == "2":
             repair_viewer()
        elif big_choice == "3":
            print("Exiting program.")
            break

print(main_thing())
