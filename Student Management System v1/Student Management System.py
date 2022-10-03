def infoPrint():
    print("Select one option-------------")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Edit Student")
    print("4. Query Student")
    print("5. View Student")
    print("6. Add Student")
    print("-" * 30)


students = []


def addStu():
    """Adding a student"""
    new_id = input("Input student Id: ")
    new_name = input("Input student name: ")
    new_tel = input("Input student mobile phone: ")

    global students

    for i in students:
        if new_name == i["name"]:
            print("This student name already exists!!  ")
            return

    student_dict = {}
    student_dict["id"] = new_id
    student_dict["name"] = new_name
    student_dict["tel"] = new_tel

    students.append(student_dict)

    print(students)


def del_student():
    del_name = input("Input the student name to delete: ")
    global students
    for i in students:
        if del_name == i["name"]:
            students.remove(i)
            print(f"{i['name']} is deleted")
            break
    else:
        print("The student doesn't exist!!")
    print(students)


def modify_student():
    modify_student = input("Input the student name to modify: ")

    global students
    for i in students:
        if modify_student == i["name"]:
            i["tel"] = input("Input the student new mobile number: ")
            input(f"Modify of {i['name']} succeeds!")
            break
    else:
        print("The student doesn't exist!!")

    print(students)


def search_student():
    search_name = input("Input the student name to search: ")
    global students
    for i in students:
        if search_name == i["name"]:
            print("The student info:-------------")
            print(f"id:{i['id']}, name:{i['name']}, phone:{i['tel']}")
            break
    else:
        print("The student doesn't exist!!")


def print_all():
    print("ID\tName\tTel")
    for i in students:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")


while True:
    infoPrint()
    userOption = int(input("Input your option: "))
    match userOption:
        case 1:
            addStu()
        case 2:
            del_student()
        case 3:
            modify_student()
        case 4:
            search_student()
        case 5:
            print_all()
        case 6:
            exit_flag = input("Are you sure to exit? yes or no: ")
            if exit_flag == "yes":
                break
        case _:
            print("Wrong Option, please input again:")
