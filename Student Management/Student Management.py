import csv
import re


FILE_NAME = 'students.csv'

def print_title():
    title = " Student Management System "
    width = len(title) + 4
    print("+" + "-" * (width - 2) + "+")
    print("|" + title.center(width - 2) + "|")
    print("+" + "-" * (width - 2) + "+")


def initialize_file():
    """Initialize the CSV file if it doesn't exist."""
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Age', 'Email'])
    except FileExistsError:
        pass  


#   adding a student
def add_student(student_id, name, age, email):
    """Add a student to the CSV file."""
    if not validate_email(email):
        print("Invalid email format.")
        return
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, email])
    print("Student added successfully!")


#  View all students
def view_students():
    """Read and display all students from the CSV file."""
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No students found. Initialize the system by adding students.")


#  Update a student
def update_student(student_id, name=None, age=None, email=None):
    """Update a student's information based on ID."""
    updated = False
    try:
        rows = []
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == student_id:
                    if name:
                        row[1] = name
                    if age:
                        row[2] = age
                    if email and validate_email(email):
                        row[3] = email
                    updated = True
                rows.append(row)
        
        if updated:
            with open(FILE_NAME, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Student updated successfully.")
        else:
            print("Student ID not found.")
    except FileNotFoundError:
        print("No students found. Initialize the system by adding students.")


#  Delete a student
def delete_student(student_id):
    """Delete a student based on ID."""
    deleted = False
    try:
        rows = []
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != student_id:
                    rows.append(row)
                else:
                    deleted = True

        if deleted:
            with open(FILE_NAME, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Student deleted successfully.")
        else:
            print("Student ID not found.")
    except FileNotFoundError:
        print("No students found. Initialize the system by adding students.")


# ✅ Search Students
def search_students(keyword):
    """Search students by ID, Name, Age, or Email."""
    found = False
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader, None)  
            print(headers)  
            for row in reader:
                if any(keyword.lower() in str(field).lower() for field in row):
                    print(row)
                    found = True
        if not found:
            print("No matching student found.")
    except FileNotFoundError:
        print("No students found. Initialize the system by adding students.")



def validate_email(email):
    """Validate email format using a regular expression."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None



def main():
    initialize_file()
    
    while True:
        print_title()
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")   
        print("6. Exit")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                student_id = input("Enter Student ID: ")
                name = input("Enter Name: ")
                age = input("Enter Age: ")
                email = input("Enter Email: ")
                add_student(student_id, name, age, email)
            elif choice == 2:
                view_students()
            elif choice == 3:
                student_id = input("Enter Student ID to update: ")
                name = input("Enter new Name (leave blank to keep current): ")
                age = input("Enter new Age (leave blank to keep current): ")
                email = input("Enter new Email (leave blank to keep current): ")
                update_student(student_id, name or None, age or None, email or None)
            elif choice == 4:
                student_id = input("Enter Student ID to delete: ")
                delete_student(student_id)
            elif choice == 5:  
                keyword = input("Enter keyword to search (ID, Name, Age, or Email): ")
                search_students(keyword)
            elif choice == 6:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")



if __name__ == "__main__":
    main()
