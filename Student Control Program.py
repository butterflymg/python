class Student:
    def __init__(self, name, id, grades, attendance):
        self.name = name
        self.id = id
        self.grades = grades
        self.attendance = attendance

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                print(f"Student with ID {student_id} removed successfully.")
                return
        print(f"Student with ID {student_id} not found.")

    def search_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                print(f"Student found - Name: {student.name}, ID: {student.id}, Grades: {student.grades}, Attendance: {student.attendance}")
                return
        print(f"Student with ID {student_id} not found.")

    def gpa_calculate(self, student_id):
        for student in self.students:
            if student.id == student_id:
                total_grades = sum(student.grades)
                gpa = total_grades / len(student.grades)
                print(f"GPA for student with ID {student_id}: {gpa}")
                return

    def mark_attendance(self, student_id, status):
        for student in self.students:
            if student.id == student_id:
                student.attendance.append(status)
                print(f"Attendance marked for student with ID {student_id}.")
                return
        print(f"Student with ID {student_id} not found.")

    def display_students(self):
        for student in self.students:
            print(f"Name: {student.name}, ID: {student.id}, Grades: {student.grades}, Attendance: {student.attendance}")

def main():
    manager = StudentManager()

    while True:
        print("\nMenu:")
        print("1. Enter student information")
        print("2. Display student information")
        print("3. Search, add or remove student")
        print("4. Mark attendance")
        print("5. GPA Calculate")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            id = int(input("Enter student's ID: "))
            grades = [float(x) for x in input("Enter student's grades (separated by comma): ").split(",")]
            attendance = []
            student = Student(name, id, grades, attendance)
            manager.add_student(student)
            print("Student information added successfully.")
        elif choice == '2':
            manager.display_students()
        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            manager.search_student(student_id)
            action = input("Do you want to add (A) or remove (R) this student? ")
            if action.lower() == 'a':
                name = input("Enter student's name: ")
                grades = [int(x) for x in input("Enter student's grades (separated by comma): ").split(",")]
                attendance = []
                student = Student(name, student_id, grades, attendance)
                manager.add_student(student)
                print("Student added successfully.")
            elif action.lower() == 'r':
                manager.remove_student(student_id)
        elif choice == '4':
            student_id = int(input("Enter student ID: "))
            status = input("Enter attendance status (P for present, A for absent): ")
            manager.mark_attendance(student_id, status)
        elif choice == '5':
            student_id = int(input("Enter student ID: "))
            manager.gpa_calculate(student_id)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()