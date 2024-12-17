class Person:
    def __init__(self, person_id, name, dob):
        self.id = person_id
        self.name = name
        self.dob = dob
    def display_info(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"
    
class Course:
    def __init__(self, course_id, course_name):
        self.id = course_id
        self.name = course_name
    def display_info(self):
        return f"ID: {self.id}, Name: {self.name}"

class Marks:
    def __init__(self):
        self.marks = {}
    def add_mark(self, student_id, course_id, mark):
        self.marks[(student_id, course_id)] = mark
    def get_mark(self, student_id, course_id):
        return self.marks.get((student_id, course_id), "No mark entered")
    def display_marks(self, students, course_id):
        print(f"\nMarks for Course ID: {course_id}")
        for student in students:
            mark = self.get_mark(student.id, course_id)
            print(f"{student.name} (ID: {student.id}): {mark}")

class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Marks()
    def input_students(self):
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            student_id = input("Student ID: ")
            student_name = input("Student Name: ")
            student_dob = input("Student Date of Birth (DoB): ")
            self.students.append(Person(student_id, student_name, student_dob))
        print("Students added successfully.\n")
        self.main_menu()
    def delete_student(self):
        if not self.students:
            print("No students to delete.")
        else:
            remove_id = input("Enter ID of the student to remove: ")
            self.students = [s for s in self.students if s.id != remove_id]
            print("Student removed successfully.\n")
        self.main_menu()
    def display_students(self):
        if not self.students:
            print("No students available.")
        else:
            print("\nStudent List:")
            for student in self.students:
                print(student.display_info())
        self.main_menu()
    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            course_id = input("Course ID: ")
            course_name = input("Course Name: ")
            self.courses.append(Course(course_id, course_name))
        print("Courses added successfully.\n")
        self.main_menu()
    def display_courses(self):
        if not self.courses:
            print("No courses available.")
        else:
            print("\nCourse List:")
            for course in self.courses:
                print(course.display_info())
        self.main_menu()
    def enter_marks(self):
        if not self.students or not self.courses:
            print("Add students and courses first.")
        else:
            self.display_courses()
            selected_course = input("Enter the Course ID for entering marks: ")
            if selected_course not in [c.id for c in self.courses]:
                print("Invalid Course ID.")
            else:
                for student in self.students:
                    mark = float(input(f"Enter mark for {student.name} (ID: {student.id}): "))
                    self.marks.add_mark(student.id, selected_course, mark)
                print("Marks added successfully.\n")
        self.main_menu()
    def show_marks(self):
        if not self.marks.marks:
            print("No marks available.")
        else:
            self.display_courses()
            selected_course = input("Enter the Course ID to view marks: ")
            if selected_course not in [c.id for c in self.courses]:
                print("Invalid Course ID.")
            else:
                self.marks.display_marks(self.students, selected_course)
        self.main_menu()
    def handle_choice(self, choice):
        if choice == 1:
            self.input_students()
        elif choice == 2:
            self.delete_student()
        elif choice == 3:
            self.display_students()
        elif choice == 4:
            self.input_courses()
        elif choice == 5:
            self.display_courses()
        elif choice == 6:
            self.enter_marks()
        elif choice == 7:
            self.show_marks()
        elif choice == 8:
            print("Exiting program. Goodbye!")
        else:
            print("Invalid option. Please try again.")
            self.main_menu()
    def main_menu(self):
        print("\nMAIN MENU")
        print("1. Add students")
        print("2. Remove a student")
        print("3. View student list")
        print("4. Add courses")
        print("5. View course list")
        print("6. Input marks for a course")
        print("7. View marks for a course")
        print("8. Exit")
        choice = int(input("Choose an option: "))
        self.handle_choice(choice)

if __name__ == "__main__":
    system = ManagementSystem()
    system.main_menu()
