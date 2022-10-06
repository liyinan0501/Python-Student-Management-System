from student import *


class StudentManager(object):
    def __init__(self):
        self.student_list = []

    def run(self):
        self.load_student()

        while True:
            self.show_menu()

            menu_num = int(input("Input your option: "))

            match menu_num:
                case 1:
                    self.add_student()
                case 2:
                    self.del_student()
                case 3:
                    self.modify_student()
                case 4:
                    self.search_student()
                case 5:
                    self.show_student()
                case 6:
                    self.save_student()
                case 7:
                    break

    @staticmethod
    def show_menu():
        print("Select one option-------------")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Edit Student")
        print("4. Search Student")
        print("5. View Student")
        print("6. Save Student")
        print("7. Exit")
        print("-" * 30)

    def add_student(self):
        name = input("Input student name: ")
        gender = input("Input student gender: ")
        tel = input("Input student phone number: ")

        new_student = Student(name, gender, tel)
        self.student_list.append(new_student)

    def del_student(self):
        del_name = input("Input student name want to delete: ")

        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)
                print("Delete succeeds!")
                break
        else:
            print("This name not exist!")

        print(self.student_list)

    def modify_student(self):
        modify_name = input("Input the student name want to modify: ")

        for i in self.student_list:
            if i.name == modify_name:
                i.name = input("Input the new name: ")
                i.gender = input("Input the new gender: ")
                i.tel = input("Input the new tel: ")
                print(
                    f"Modify succeeds! name: {i.name}, gender: {i.gender}, tel: {i.tel}"
                )
                break
        else:
            print("The student not exist!!")

    def search_student(self):
        search_name = input("Input the name want to search: ")

        for i in self.student_list:
            if i.name == search_name:
                print(f"name: {i.name}, gender: {i.gender}, tel: {i.tel}")
                break
        else:
            print("The student not exist!!")

    def show_student(self):
        print("name\tgender\ttel")
        for i in self.student_list:
            print(f"{i.name}\t{i.gender}\t{i.tel}")

    def save_student(self):
        print("Save a student")

    def load_student(self):
        print("Load students")
