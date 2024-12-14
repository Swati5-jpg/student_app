import json

class Student:
    def __init__(self, student_id, name, age, grade, subjects):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects

    def display_details(self):
        """Format the student details for display."""
        subjects_str = ', '.join(self.subjects)
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Subjects: {subjects_str}"

    def update_student_info(self, name=None, age=None, grade=None, subjects=None):
        """Update student information with optional parameters."""
        if name: self.name = name
        if age: self.age = age
        if grade: self.grade = grade
        if subjects: self.subjects = subjects


class StudentManagement:
    def __init__(self):
        self.students = []
        self.load_students_from_file()

        # Add initial list of students if the file is empty
        if not self.students:
            self.students = [
                Student(101, "Aarav Singh", 18, "A", ["Math", "Physics"]),
                Student(102, "Saanvi Kapoor", 19, "B", ["English", "History"]),
                Student(103, "Vihaan Sharma", 20, "A-", ["Chemistry", "Biology"]),
                Student(104, "Ishita Reddy", 21, "B+", ["Geography", "History"]),
                Student(105, "Advit Gupta", 22, "A+", ["Computer Science", "Physics"]),
                Student(106, "Kiara Iyer", 23, "B", ["Math", "Economics"]),
                Student(107, "Reyansh Patel", 20, "A", ["Chemistry", "Math"]),
                Student(108, "Mira Deshmukh", 18, "B+", ["English", "Biology"]),
                Student(109, "Arjun Rao", 21, "A-", ["Physics", "Economics"]),
                Student(110, "Tara Verma", 22, "A", ["Computer Science", "Math"]),
            ]

    def load_students_from_file(self):
        """Load student data from a file."""
        try:
            with open('students.txt', 'r') as file:
                data = json.load(file)
                self.students = [Student(d["id"], d["name"], d["age"], d["grade"], d["subjects"]) for d in data]
        except FileNotFoundError:
            print("No existing data found. Starting with an empty list of students.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def save_students_to_file(self):
        """Save student data to a file."""
        try:
            with open('students.txt', 'w') as file:
                json.dump([{"id": s.student_id, "name": s.name, "age": s.age, "grade": s.grade, "subjects": s.subjects} for s in self.students], file, indent=4)
            print("Data saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_student(self):
        """Add a new student to the list."""
        try:
            student_id = int(input("Enter student ID: "))
            if any(student.student_id == student_id for student in self.students):
                print("Error: Student ID must be unique.")
                return
            name = input("Enter student name: ").strip()
            age = input("Enter student age: ").strip()
            grade = input("Enter student grade: ").strip()
            subjects_input = input("Enter subjects (comma-separated): ").strip()

            if not age.isdigit():
                print("Error: Age must be a valid number.")
                return
            age = int(age)

            subjects = [subject.strip() for subject in subjects_input.split(",") if subject.strip()]
            if not subjects:
                print("Error: At least one subject is required.")
                return

            new_student = Student(student_id, name, age, grade, subjects)
            self.students.append(new_student)
            print("Student added successfully.")
        except ValueError as e:
            print(f"Error: Invalid input. Details: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def view_students(self):
        """Display all students."""
        if not self.students:
            print("No students available.")
        else:
            print("\n--- All Students ---")
            for student in self.students:
                print(student.display_details())

    def update_student(self):
        """Update a student's details."""
        try:
            student_id = int(input("Enter student ID to update: "))
            student = next((s for s in self.students if s.student_id == student_id), None)
            if not student:
                print("Error: Student not found.")
                return

            print("\nUpdate Options:")
            print("1. Name\n2. Age\n3. Grade\n4. Subjects")
            choice = int(input("Enter the number of the attribute to update: "))
            if choice == 1:
                student.name = input("Enter new name: ").strip()
            elif choice == 2:
                age = input("Enter new age: ").strip()
                if not age.isdigit():
                    print("Error: Age must be a valid number.")
                    return
                student.age = int(age)
            elif choice == 3:
                student.grade = input("Enter new grade: ").strip()
            elif choice == 4:
                subjects_input = input("Enter new subjects (comma-separated): ").strip()
                student.subjects = [subject.strip() for subject in subjects_input.split(",") if subject.strip()]
            else:
                print("Error: Invalid choice.")
                return

            print("Student details updated successfully.")
        except ValueError:
            print("Error: Invalid input.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def delete_student(self):
        """Delete a student by their ID."""
        try:
            student_id = int(input("Enter student ID to delete: "))
            student = next((s for s in self.students if s.student_id == student_id), None)
            if student:
                self.students.remove(student)
                print(f"Student with ID {student_id} deleted successfully.")
            else:
                print("Error: Student not found.")
        except ValueError:
            print("Error: Please enter a valid numeric ID.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def display_menu(self):
        """Display the main menu."""
        print("\n--- Student Management System ---")
        print("1. View all students\n2. Add a new student\n3. Update a student's information\n4. Delete a student\n5. Save and Exit")

    def main(self):
        """Main loop to manage the menu and operations."""
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1: 
                    self.view_students()
                elif choice == 2: 
                    self.add_student()
                elif choice == 3: 
                    self.update_student()
                elif choice == 4: 
                    self.delete_student()
                elif choice == 5:
                    self.save_students_to_file()
                    print("Exiting. Goodbye!")
                    break
                else: 
                    print("Invalid choice.")
            except ValueError:
                print("Error: Please enter a valid number.")
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt detected. Exiting program.")
                break

if __name__ == "__main__":
    student_management = StudentManagement()
    student_management.main()



