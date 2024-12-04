student_data = []
course_data = []
student_marks = {}

def input_students():
    num_students = int(input("Enter number of students: "))
    for _ in range(num_students):
        student_id = input("Student ID: ")
        student_name = input("Student Name: ")
        student_dob = input("Student Date of Birth (DoB): ")
        print("------")
        student_data.append({"id": student_id, "name": student_name, "dob": student_dob})
    main_menu()

def delete_student():
    if not student_data:
        print("No students to delete.")
    else:
        remove_id = input("Enter ID of the student to remove: ")
        student_data[:] = [s for s in student_data if s["id"] != remove_id]
        print("Student removed successfully.")
    main_menu()

def display_students():
    if not student_data:
        print("No students available.")
    else:
        print("\nStudent List:")
        for s in student_data:
            print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")
    print("------")
    main_menu()

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    for _ in range(num_courses):
        course_id = input("Course ID: ")
        course_name = input("Course Name: ")
        print("------")
        course_data.append({"id": course_id, "name": course_name})
    main_menu()

def display_courses():
    if not course_data:
        print("No courses available.")
    else:
        print("\nCourse List:")
        for c in course_data:
            print(f"ID: {c['id']}, Name: {c['name']}")
    print("------")
    main_menu()

def enter_marks():
    if not student_data or not course_data:
        print("Add students and courses first.")
    else:
        display_courses()
        selected_course = input("Enter the Course ID for entering marks: ")
        if selected_course not in [c["id"] for c in course_data]:
            print("Invalid Course ID.")
        else: 
            for s in student_data:
                mark = float(input(f"Enter mark for {s['name']} (ID: {s['id']}): "))
                student_marks[(s["id"], selected_course)] = mark
            print("Marks added.")
    main_menu()

def show_marks():
    if not student_marks:
        print("No marks available.")
    else:
        display_courses()
        selected_course = input("Enter the Course ID to view marks: ")
        if selected_course not in [c["id"] for c in course_data]:
            print("Invalid Course ID.")
        else:
            print(f"\nMarks for Course ID: {selected_course}")
            for s in student_data:
                mark = student_marks.get((s["id"], selected_course), "No mark entered")
                print(f"{s['name']} (ID: {s['id']}): {mark}")
    main_menu()

def handle_choice(choice):
    if choice == 1:
        input_students()
    elif choice == 2:
        delete_student()
    elif choice == 3:
        display_students()
    elif choice == 4:
        input_courses()
    elif choice == 5:
        display_courses()
    elif choice == 6:
        enter_marks()
    elif choice == 7:
        show_marks()
    elif choice == 8:
        print("Exiting program. Goodbye!")
    else:
        print("Invalid option. Please try again.")
        main_menu()

def main_menu():
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
    handle_choice(choice)

main_menu()