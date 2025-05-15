
"""
!📚 🎓 Student Management System (Mini Project)
🎯 Use Case:
A system where:

1. Admin can add student records

2. Student has personal info (public)

3. Marks are protected

4. Fees are private

5. Destructor shows when student record is deleted

"""

class Student:
    def __init__(self, name, roll_no, marks, fees):
        self.name = name                    # Public
        self.roll_no = roll_no              # Public
        self._marks = marks                # Protected
        self.__fees = fees                 # Private
        print(f"Student {self.name} added to system.")

    def show_public_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

    def show_marks(self):
        print(f"Marks (Protected): {self._marks}")

    def show_fees(self):
        print(f"Fees (Private): ₹{self.__fees}")

    def update_marks(self, new_marks):
        self._marks = new_marks

    def update_fees(self, new_fees):
        self.__fees = new_fees

    def __del__(self):
        print(f"Student record for {self.name} deleted from system.")

# Subclass for managing data
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_no, marks, fees):
        student = Student(name, roll_no, marks, fees)
        self.students.append(student)

    def show_all(self):
        for s in self.students:
            s.show_public_info()
            s.show_marks()
            s.show_fees()
            print("---")

    def delete_student(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                self.students.remove(s)
                del s
                print("Student removed.")
                return
        print("Student not found.")

# Main Program
manager = StudentManager()

# Add Students
manager.add_student("Ali", 101, 88, 50000)
manager.add_student("Sara", 102, 92, 55000)

# Show All Students
print("\nAll Student Records:")
manager.show_all()

# Update Student Marks (accessing protected)
print("\nUpdating Marks:")
manager.students[0].update_marks(95)
manager.students[0].show_marks()

# Try accessing private data directly
print("\nAccessing Private Data Directly:")
try:
    print(manager.students[0].__fees)  # ❌ Will give error
except AttributeError as e:
    print("Error:", e)

# Accessing private data via name mangling (not recommended)
print("Access via name mangling (not recommended):")
print(manager.students[0]._Student__fees)

# Delete a Student
print("\nDeleting Student Record:")
manager.delete_student(101)
