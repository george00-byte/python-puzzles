class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.marks = {}

    def add_marks(self, subject, mark):
        self.marks[subject] = mark

    def get_average_marks(self):
        return sum(self.marks.values()) / len(self.marks)


student_list = []

while True:
    id = int(input('Enter student id: '))
    name = input('Enter student name: ')
    student = Student(id, name)
    while True:
        subject = input('Enter subject: ')
        if subject == '':
            break
        mark = int(input('Enter marks: '))
        student.add_marks(subject, mark)
    student_list.append(student)
    print('Student added successfully!')
    choice = input('Do you want to add another student (y/n): ')
    if choice == 'n':
        break

for student in student_list:

    print(f'Name: {student.name}')
    print(f'ID: {student.id}')
    print(f'Average marks: {student.get_average_marks():.2f}')
    print('-' * 25)



