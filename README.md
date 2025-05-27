# AP-CS-FINAL_PROJECT
## Rover Repair Garage overview:
This technical doc will go over the 4 main segments of code that make the land rover repair log function.

- [Main menu](#main-menu-explained)
- [Logging repairs](#logging-repairs-explained)
- [Viewing repairs](#viewing-repairs-explained)
- [Showing all different parts](#showing-all-different-parts-explained)


## Main menu explained:
This code segment consists of only print statements that show the user options they can choose. This is all put into a procedure that will be used in the last segment. There is also another print statement that shows the title of the rover repair log, that automatically goes down a line eachtime the procedure is called.

```
print("\n------Rover Repair log------")
print("1. Log a repair")
```


## Logging repairs explained:
This procedure calls for 3 user inputs, rover id, the issue with the rover, and how it was fixed. Then the procedure creates a text file, opening it asd the variable "fi" with the write mode using the "W" variable. Then the code will write in the text file the rover id, the problem with the rover, and the fix for it using the user inputs from before. 

```
 with open("Repairs.txt", "a") as fi:
        fi.write(f"Rover ID: {rov_id} | Issue: {iss} | Fix: {fix} \n")
```
  
Once the with statement ends, the code will print that the repair is logged.


## Viewing repairs explained:
This procedure calls to open the "Repairs.txt" file created from the logging repairs procedure in the read mode ("r") as "fi" again. The varaible log is created to store the strings created from the `.readlines` method. `.readlines` reads any text from the text file and then converts them into strings.

```
with open("Repairs.txt", "r") as fi:
            log = fi.readlines()
```

Then within an if statement, asking if strings were created from text within the file, it will print the title of the section "Repair logs" and then asks within a for statement that for each string created by `.readlines()` will be cleaned by the `.strip()` function, removing any spaces, tabs, or newline functions like `\n` which was in the write statement from the previous procedure. 

```
def repair_viewer():
    try:
        with open("Repairs.txt", "r") as fi:
            log = fi.readlines()
```

This procedure is within a try-except statement incase there is not a repairs text file created by the previous procedure, telling the user that there is no repairs logged if there is a FileNotFoundError.

```
if log:
        print("\n----Repair Logs----")
        for entry in log:
                    print(entry.strip())
            else:
                 print("No repairs logged.")
    except FileNotFoundError:
        print("No repairs logged")
```


## Showing all different parts explained:
This procedure is essentially the glue that pieces each other procedure together and lets them work together. In a while loop, asking while the procedure is being called is true, it will show the main menu procedure and aska user to input a number 1-3 for each option you can do. Using an if statement it asks if the user input variable `big_choice` is equal to 1 and if it is, it will display the `log_repair()` procedure. 
```
def main_thing():
    while True:
        the_menu()
        big_choice = input("Select an option (1-3): ")
        if big_choice == "1": 
             log_repair()
```

Using an elif statement it asks if the user input variable `big_choice` is equal to 2 and if it is, it will display the `repair_viewer` procedure. 
Using another elif statement it asks if the user input variable `big_choice` is equal to 3 and if it is, it will print that the user is exiting the program and then the code will stop using the `break` function
