# Wiut attendance tracking app

# Dictionary to store attendance records
attendance_records = {}

def mark_attendance(student_id):
    # Check if the student ID is valid (8 digits)
    if len(student_id) != 8 or not student_id.isdigit():
        print("Invalid ID. Please enter an 8-digit ID number.")
        return False
    else:
        # Mark attendance for the student
        attendance_records[student_id] = "Attended"
        print(f"Student's Attendance marked: {student_id}")
        return True

def display_attendance():
    # Display all attendance records
    print("\nAttendance Records:")
    print("Student ID\tStatus")
    for student_id, status in attendance_records.items():
        print(f"{student_id}\t\t{status}")

def main():
    while True:
        # Display menu options
        print("\n1. Mark Attendance")
        print("2. View Attended Students")
        print("3. Go Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt user for student ID
            student_id = input("Enter your Student ID(8 numbers): ")
            mark_attendance(student_id)
        elif choice == '2':
            # Show all marked attendance
            display_attendance()
        elif choice == '3':
            # Exit the program
            print("Exiting the program.")
            break
        else:
            # Handle invalid input
            print("Error")

# Entry point of the program
if name == "main":
    main()