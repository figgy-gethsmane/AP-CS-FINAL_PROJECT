# AP-CS-FINAL_PROJECT
## Rover Repair Garage overview:
This technical doc will go over the 4 main segments of code that make the land rover repair log function.

- [Main menu](#main-menu-explained:)
- [Logging repairs](#logging-repairs-explained:)
- Viewing repairs
- Showing all different parts


## Main menu explained:
This code segment consists of only print statements that show the user options they can choose. This is all put into a procedure that will be used in the last segment. There is also another print statement that shows the title of the rover repair log, that automatically goes down a line eachtime the procedure is called.

`print("\n------Rover Repair log------")`
`print("1. Log a repair")`


## Logging repairs explained:
This procedure calls for 3 user inputs, rover id, the issue with the rover, and how it was fixed. Then the procedure creates a text file, opening it asd the variable "fi" with the write mode using the "W" variable. Then the code will write in the text file the rover id, the problem with the rover, and the fix for it using the user inputs from before. 

 `with open("Repairs.txt", "a") as fi:
        fi.write(f"Rover ID: {rov_id} | Issue: {iss} | Fix: {fix} \n")`
  
Once the with statement ends, the code will print that the repair is logged.
