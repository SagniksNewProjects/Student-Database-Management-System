import csv
import os


# ------------------------------------------------------------
# Student Database Management System
# B.Tech CSE Project
# ------------------------------------------------------------

FILE_NAME = "students.csv"

FIELDNAMES = [
    "Roll No",
    "Name",
    "Department",
    "Semester",
    "Phone",
    "Email",
    "CGPA"
]


# ------------------------------------------------------------
# Student Class
# ------------------------------------------------------------

class Student:

    def __init__(
        self,
        roll_no,
        name,
        department,
        semester,
        phone,
        email,
        cgpa
    ):
        self.roll_no = roll_no
        self.name = name
        self.department = department
        self.semester = semester
        self.phone = phone
        self.email = email
        self.cgpa = cgpa

    def to_dict(self):
        """Convert student object into a dictionary."""

        return {
            "Roll No": self.roll_no,
            "Name": self.name,
            "Department": self.department,
            "Semester": self.semester,
            "Phone": self.phone,
            "Email": self.email,
            "CGPA": self.cgpa
        }


# ------------------------------------------------------------
# File Handling Functions
# ------------------------------------------------------------

def initialize_file():
    """Create the CSV file if it does not already exist."""

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=FIELDNAMES
            )

            writer.writeheader()


def load_students():
    """Read all student records from the CSV file."""

    initialize_file()

    with open(FILE_NAME, "r", newline="") as file:

        reader = csv.DictReader(file)

        return list(reader)


def save_students(students):
    """Save the complete student list to the CSV file."""

    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=FIELDNAMES
        )

        writer.writeheader()
        writer.writerows(students)


# ------------------------------------------------------------
# Input Validation Functions
# ------------------------------------------------------------

def get_non_empty_input(message):
    """Get input that cannot be left empty."""

    while True:

        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_semester():
    """Get a valid semester number."""

    while True:

        semester = input("Enter Semester (1-8): ").strip()

        if semester.isdigit():

            semester = int(semester)

            if 1 <= semester <= 8:
                return str(semester)

        print("Please enter a valid semester between 1 and 8.")


def get_cgpa():
    """Get a valid CGPA value."""

    while True:

        cgpa = input("Enter CGPA (0.0-10.0): ").strip()

        try:

            cgpa = float(cgpa)

            if 0 <= cgpa <= 10:
                return f"{cgpa:.2f}"

            print("CGPA must be between 0 and 10.")

        except ValueError:

            print("Please enter a valid numeric CGPA.")


def get_phone():
    """Get a valid phone number."""

    while True:

        phone = input("Enter Phone Number: ").strip()

        if phone.isdigit() and len(phone) == 10:
            return phone

        print("Please enter a valid 10-digit phone number.")


def get_email():
    """Get a basic valid email address."""

    while True:

        email = input("Enter Email: ").strip()

        if "@" in email and "." in email:
            return email

        print("Please enter a valid email address.")


# ------------------------------------------------------------
# Display Functions
# ------------------------------------------------------------

def display_student(student):
    """Display a single student record."""

    print("\n------------------------------------------")
    print(f"Roll Number : {student['Roll No']}")
    print(f"Name        : {student['Name']}")
    print(f"Department  : {student['Department']}")
    print(f"Semester    : {student['Semester']}")
    print(f"Phone       : {student['Phone']}")
    print(f"Email       : {student['Email']}")
    print(f"CGPA        : {student['CGPA']}")
    print("------------------------------------------")


def display_all_students():
    """Display all student records."""

    students = load_students()

    if not students:

        print("\nNo student records found.")
        return

    print("\n" + "=" * 110)
    print("                         ALL STUDENT RECORDS")
    print("=" * 110)

    print(
        f"{'Roll No':<10}"
        f"{'Name':<20}"
        f"{'Department':<15}"
        f"{'Semester':<10}"
        f"{'Phone':<15}"
        f"{'Email':<30}"
        f"{'CGPA':<6}"
    )

    print("-" * 110)

    for student in students:

        print(
            f"{student['Roll No']:<10}"
            f"{student['Name'][:19]:<20}"
            f"{student['Department'][:14]:<15}"
            f"{student['Semester']:<10}"
            f"{student['Phone']:<15}"
            f"{student['Email'][:29]:<30}"
            f"{student['CGPA']:<6}"
        )

    print("=" * 110)


# ------------------------------------------------------------
# Add Student
# ------------------------------------------------------------

def add_student():

    print("\n" + "=" * 50)
    print("                    ADD STUDENT")
    print("=" * 50)

    students = load_students()

    roll_no = get_non_empty_input("Enter Roll Number: ")

    # Check for duplicate roll number
    for student in students:

        if student["Roll No"].lower() == roll_no.lower():

            print("\nA student with this Roll Number already exists.")
            return

    name = get_non_empty_input("Enter Name: ")
    department = get_non_empty_input("Enter Department: ")
    semester = get_semester()
    phone = get_phone()
    email = get_email()
    cgpa = get_cgpa()

    student = Student(
        roll_no,
        name,
        department,
        semester,
        phone,
        email,
        cgpa
    )

    students.append(student.to_dict())

    save_students(students)

    print("\nStudent record added successfully.")


# ------------------------------------------------------------
# Search Student
# ------------------------------------------------------------

def search_student():

    print("\n" + "=" * 50)
    print("                  SEARCH STUDENT")
    print("=" * 50)

    students = load_students()

    if not students:

        print("\nNo student records found.")
        return

    keyword = input(
        "Enter Roll Number or Name to search: "
    ).strip().lower()

    found_students = []

    for student in students:

        if (
            keyword == student["Roll No"].lower()
            or keyword in student["Name"].lower()
        ):
            found_students.append(student)

    if found_students:

        print(
            f"\n{len(found_students)} student record(s) found."
        )

        for student in found_students:
            display_student(student)

    else:

        print("\nNo matching student record found.")


# ------------------------------------------------------------
# Update Student
# ------------------------------------------------------------

def update_student():

    print("\n" + "=" * 50)
    print("                  UPDATE STUDENT")
    print("=" * 50)

    students = load_students()

    roll_no = get_non_empty_input(
        "Enter Roll Number to update: "
    )

    student_found = None

    for student in students:

        if student["Roll No"].lower() == roll_no.lower():

            student_found = student
            break

    if student_found is None:

        print("\nStudent record not found.")
        return

    print("\nCurrent Student Information:")
    display_student(student_found)

    print("\nEnter the new information:")

    student_found["Name"] = get_non_empty_input(
        "Enter Name: "
    )

    student_found["Department"] = get_non_empty_input(
        "Enter Department: "
    )

    student_found["Semester"] = get_semester()
    student_found["Phone"] = get_phone()
    student_found["Email"] = get_email()
    student_found["CGPA"] = get_cgpa()

    save_students(students)

    print("\nStudent record updated successfully.")


# ------------------------------------------------------------
# Delete Student
# ------------------------------------------------------------

def delete_student():

    print("\n" + "=" * 50)
    print("                  DELETE STUDENT")
    print("=" * 50)

    students = load_students()

    roll_no = get_non_empty_input(
        "Enter Roll Number to delete: "
    )

    student_found = None

    for student in students:

        if student["Roll No"].lower() == roll_no.lower():

            student_found = student
            break

    if student_found is None:

        print("\nStudent record not found.")
        return

    print("\nStudent record found:")
    display_student(student_found)

    confirmation = input(
        "Are you sure you want to delete this record? (Y/N): "
    ).strip().lower()

    if confirmation == "y":

        students.remove(student_found)

        save_students(students)

        print("\nStudent record deleted successfully.")

    else:

        print("\nDeletion cancelled.")


# ------------------------------------------------------------
# Main Menu
# ------------------------------------------------------------

def display_menu():

    print("\n")
    print("=" * 60)
    print("          STUDENT DATABASE MANAGEMENT SYSTEM")
    print("=" * 60)

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    print("=" * 60)


def main():

    initialize_file()

    while True:

        display_menu()

        choice = input(
            "Enter your choice (1-6): "
        ).strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            display_all_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            print("\nThank you for using the")
            print("Student Database Management System.")
            print("\nProgram terminated successfully.")
            break

        else:

            print(
                "\nInvalid choice. "
                "Please select an option from 1 to 6."
            )


# ------------------------------------------------------------
# Program Execution
# ------------------------------------------------------------

if __name__ == "__main__":
    main()