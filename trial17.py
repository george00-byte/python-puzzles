class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.marks = {}

    def add_Marks(self,mark,subject):
        self.marks[subject] = mark

    def average_marks(self):
       return sum(self.marks.values()) / len(self.marks)


student_list = []

while True:
    id=int(input("Enter the Id"))
    name = input("Enter the name of the student: ")
    student = Student(id,name)

    while True:
        mark= int(input("Enter the marks of the student"))
        subject = input("Enter the subject")
        student.add_Marks(mark, subject)

        if subject == "":
            break
    student_list.append(student)
    choice = input("Do you want to continue Y/N")
    if choice == "n":
        break


for student in student_list:
    print('f',student.id)
    print('f', student.name)
    print(student.average_marks())

    print("*"*23)














