# Student Management System using Basic Python

students = []  # List to store student records

# Function to add a new student
def add_student():                                  # Function to add a new student
    name = input("Enter student name: ")            # Prompt user for student name
    roll_no = input("Enter roll number: ")          # Prompt user for roll number
    marks = input("Enter marks: ")                  # Prompt user for marks
      
    student = {                                     # Create a dictionary to store student details
        "name": name,                               # Store student name        
        "roll_no": roll_no,                # Store roll number
        "marks": marks                    # Store marks
    }
    
    students.append(student)                       # Add the student dictionary to the students list
    print("Student added successfully!\n")           # Confirmation message after adding student                  

# Function to display all students
def display_students():                            # Function to display all student records
    if not students:                             # Check if the students list is empty
        print("No student records found.\n")     # If empty, print message and return
        return                                   #  Return to exit the function
    
    print("\n--- Student Records ---")        # Print header for student records
    for student in students:                 # Loop through each student in the students list
        print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Marks: {student['marks']}")        # Print student details in a formatted string
    print()                            # Print a new line for better readability

# Function to search for a student by roll number
def search_student():                       # Function to search for a student by roll number
    roll_no = input("Enter roll number to search: ")   # Prompt user for roll number to search
    found = False                     # Flag to check if student is found
    for student in students:          # Loop through each student in the students list
        if student['roll_no'] == roll_no:                   # Check if the roll number matches       
            # If a match is found, print student details
            print(f"Student Found: Name: {student['name']}, Marks: {student['marks']}\n")      # Print student details if found
            found = True         # Set found flag to True
            break          # Break the loop as we found the student
    if not found:            # If no student is found, print message 
        print("Student not found.\n")      # Print message if student is not found       

# Function to update student details
def update_student():             # Function to update student details
    roll_no = input("Enter roll number of student to update: ")     #           Prompt user for roll number to update
    # Loop through each student to find the one with the given roll number  
    for student in students:                    # Loop through each student in the students list
        # Check if the roll number matches 
        if student['roll_no'] == roll_no:    # If a match is found
            # Prompt user for new details
            print("Student found. Enter new details.")          # Prompt user to enter new details
            # Update student details
            student['name'] = input("Enter new name: ")       # Prompt user for new name
            student['marks'] = input("Enter new marks: ")    # Prompt user for new marks
            print("Student details updated successfully!\n")  # Print confirmation message after updating details
            return                                            # Return to exit the function
    # If no student is found with the given roll number
    print("Student not found.\n")      # Print message if student is not found

# Function to delete a student record
def delete_student():        # Function to delete a student record
    roll_no = input("Enter roll number of student to delete: ")   # Prompt user for roll number to delete
    for student in students:       # Loop through each student in the students list
        if student['roll_no'] == roll_no:     # Check if the roll number matches
            students.remove(student)        # Remove the student from the list
            # Print confirmation message after deletion
            print("Student deleted successfully!\n")       # Print message after successful deletion
            return    # Return to exit the function
    print("Student not found.\n")     # Print message if student is not found

# Function to show the menu
def menu():        # Function to show the menu
    while True:      # Infinite loop to keep showing the menu until user chooses to exit
        print("===== Student Management System =====")     # Print menu header
        print("1. Add Student")    # Print option to add a student
        print("2. Display All Students")    # Print option to display all students
        print("3. Search Student")     # Print option to search for a student
        print("4. Update Student")   # Print option to update student details
        print("5. Delete Student")      # Print option to delete a student
        print("6. Exit")              # Print option to exit the program
        # Prompt user for choice
        
        choice = input("Enter your choice (1-6): ")     # Read user input for menu choice
        
        if choice == '1':                                        #            
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
menu()
