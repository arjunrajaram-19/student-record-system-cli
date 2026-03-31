def menu():
    print("\n1. View Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Clear all Records")
    print("7. Exit")

def load_students():
    try:
        with open("students.txt", "r") as f:
            lines=f.readlines()
        students=[]
        for line in lines:
            name, marks = line.strip().split(",")
            students.append([name.strip(), int(marks.strip())])
        return students
    except:
        return []

def save_students(students):
    with open("students.txt", "w") as f:
        for student in students:
            f.write(student[0]+","+str(student[1])+"\n")

def add_student(students):
    name=input("Enter name: ")
    name=name.strip().title()
    if name=="":
        print("Name cannot be empty")
        return
    for student in students:
        if student[0].lower()==name.lower():
            print("Student already exists")
            return
    try:
        marks=int(input("Enter marks: "))
    except ValueError:
        print("Invalid marks")
        return
    if marks<0:
        print("Marks cannot be negative")
        return
    students.append([name, marks])
    save_students(students)
    print("Record Added")

def view_students(students):
    if not students:
        print("No records available.")
        return
    for i in range(len(students)):
        print(str(i+1)+"."+students[i][0]+"-"+str(students[i][1]))


def search_student(students):
    if not students:
        print("No records available.")
        return
    name=input("Enter name to search: ")
    if name.strip()=="":
        print("Name cannot be empty")
        return
    for student in students:
        if student[0].lower()==name.lower():
            print("Found:", student[0], student[1])
            return
    print("Student not found")

def update_student(students):
    if not students:
        print("No records available.")
        return
    name=input("Enter name: ")
    if name.strip()=="":
        print("Name cannot be empty")
        return
    for student in students:
        if student[0].lower()==name.lower():
            try:
                new_marks=int(input("Enter new marks: "))
            except ValueError:
                print("Invalid marks")
                return
            if new_marks<0:
                print("Marks cannot be negative")
                return
            student[1]=new_marks
            save_students(students)
            print("Updated")
            return
    print("Student not found")

def delete_student(students):
    if not students:
        print("No records available.")
        return
    name=input("Enter name: ")
    if name.strip()=="":
        print("Name cannot be empty")
        return

    for student in students:
        if student[0].lower()==name.lower():
            confirm=input("Are you sure you want to delete? (y/n): ")
            if confirm.lower()!="y":
                print("Cancelled")
                return
            students.remove(student)
            save_students(students)
            print("Deleted")
            return
    print("Student not found")

def clear_all_students(students):
    if not students:
        print("No records to clear.")
        return
    confirm=input("Are you sure you want to delete ALL records? (y/n): ")
    if confirm.lower()=="y":
        students.clear()
        save_students(students)
        print("All records deleted.")
    else:
        print("Cancelled.")


students=load_students()
while True:
    menu()
    choice=input("Choose: ")
    if choice=="1":
        view_students(students)
    elif choice=="2":
        add_student(students)
    elif choice=="3":
        search_student(students)
    elif choice=="4":
        update_student(students)
    elif choice=="5":
        delete_student(students)
    elif choice=="6":
        clear_all_students(students)
    elif choice=="7":
        save_students(students)
        print("Exiting...")
        break
    else:
        print("Invalid choice")