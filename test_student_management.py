import unittest
import json
import os

class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, age, grade, subjects):
        """Add a new student."""
        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }
        self.students.append(student)

    def view_students(self):
        """Return a list of students' details as strings."""
        return [f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Subjects: {', '.join(student['subjects'])}" for student in self.students]

    def update_student(self, student_id, name=None, age=None, grade=None, subjects=None):
        """Update an existing student's details."""
        for student in self.students:
            if student['id'] == student_id:
                if name:
                    student['name'] = name
                if age:
                    student['age'] = age
                if grade:
                    student['grade'] = grade
                if subjects:
                    student['subjects'] = subjects
                return True
        return False

    def delete_student(self, student_id):
        """Delete a student by their ID."""
        self.students = [student for student in self.students if student['id'] != student_id]

    def save_students_to_file(self, filename):
        """Save students to a file."""
        with open(filename, 'w') as file:
            json.dump(self.students, file)

    def load_students_from_file(self, filename):
        """Load students from a file."""
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.students = json.load(file)
        else:
            print(f"{filename} not found. No students loaded.")

class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        # Setup a fresh StudentManagement instance before each test
        self.student_management = StudentManagement()

    def test_add_student(self):
        # Test that students are added correctly
        self.student_management.add_student(1, "Alice", 20, "A", ["Math", "Science"])
        self.student_management.add_student(2, "Bob", 22, "B", ["English", "History"])

        students = self.student_management.view_students()
        self.assertEqual(len(students), 2)
        self.assertIn("Alice", students[0])
        self.assertIn("Bob", students[1])

    def test_view_students_empty(self):
        # Test viewing students when there are no students
        students = self.student_management.view_students()
        self.assertEqual(len(students), 0)

    def test_update_student(self):
        # Test updating a student's details
        self.student_management.add_student(1, "Alice", 20, "A", ["Math", "Science"])
        self.student_management.update_student(1, age=21, grade="A+")
        
        students = self.student_management.view_students()
        self.assertIn("21", students[0])  # Age should be updated to 21
        self.assertIn("A+", students[0])  # Grade should be updated to A+

    def test_update_student_nonexistent(self):
        # Test updating a student that does not exist
        result = self.student_management.update_student(999, name="Charlie")
        self.assertFalse(result)  # No student with ID 999

    def test_delete_student(self):
        # Test deleting a student
        self.student_management.add_student(1, "Alice", 20, "A", ["Math", "Science"])
        self.student_management.delete_student(1)

        students = self.student_management.view_students()
        self.assertEqual(len(students), 0)  # No students should be present

    def test_save_students_to_file(self):
        # Test saving students to the "student.txt" file
        self.student_management.add_student(1, "Alice", 20, "A", ["Math", "Science"])
        self.student_management.add_student(2, "Bob", 22, "B", ["English", "History"])

        # Define the file name
        filename = "student.txt"
        
        # Save the students to the file
        self.student_management.save_students_to_file(filename)

        # Now check if the file was written correctly
        with open(filename, 'r') as file:
            data = json.load(file)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]["name"], "Alice")
            self.assertEqual(data[1]["subjects"], ["English", "History"])

        # Clean up the file after test
        os.remove(filename)

    def test_load_students_from_file(self):
        # Test loading students from the "student.txt" file
        student_data = [{"id": 1, "name": "Alice", "age": 20, "grade": "A", "subjects": ["Math", "Science"]}]
        
        # Define the file name
        filename = "student.txt"
        
        # Save the student data to the file
        with open(filename, 'w') as file:
            json.dump(student_data, file)
        
        # Load the students from the file
        self.student_management.load_students_from_file(filename)
        
        students = self.student_management.view_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0], "ID: 1, Name: Alice, Age: 20, Grade: A, Subjects: Math, Science")
        
        # Clean up the file after test
        os.remove(filename)

    def test_load_students_from_file_file_not_found(self):
        # Test that the load function handles a missing file gracefully
        self.student_management.load_students_from_file("non_existing_file.txt")
        students = self.student_management.view_students()
        self.assertEqual(len(students), 0)  # No students should be loaded

if __name__ == "__main__":
    unittest.main()
