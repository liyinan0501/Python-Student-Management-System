class StudentManager(object):
    def __init__(self) -> None:
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
        print("Add a student")

    def del_student(self):
        print("Delete a student")

    def modify_student(self):
        print("Modify a student")

    def search_student(self):
        print("Search a student")

    def show_student(self):
        print("Show all students")

    def save_student(self):
        print("Save a student")

    def load_student(self):
        print("Load students")
