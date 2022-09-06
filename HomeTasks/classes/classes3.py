# Добавить метод в  класс Student get_average_score().
# Добавить метод в  класс Student is_excellent(),
# который возвращает True, если все оценки от 8 до 10, иначе False.

class Student:
    def __init__(self, name, age, marks=None):
        self.name = name
        self.age = age
        self.marks = marks or []

    def get_bio_info(self):
        return self.name, self.age

    def set_mark(self, mark):
        self.marks.append(mark)

    def statistics(self):
        for i in self.marks:
            print(i.score, i.subject.name)

    def get_average_score(self):
        return sum(self.marks) / len(self.marks)

    def is_excellent(self):
        for i in self.marks:
            if i in ['1', '2', '3', '4', '5', '6', '7']:
                return False
            break
        else:
            return True


class Group:
    def __init__(self, number, students=None, subjects=None):
        self.number = number
        self.students = students or []
        self.subjects = subjects or []


class Subject:
    def __init__(self, name):
        self.name = name


class Mark:
    def __init__(self, score, subject):
        self.score = score
        self.subject = subject


student_1 = Student('ivan', 39)
student_2 = Student('oleg', 50)
student_3 = Student('vasya', 13)

subject_python = Subject('python')
subject_java = Subject('java')

group = Group(
    'the best of the best',
    students=[student_1, student_2, student_3],
    subjects=[subject_python, subject_java]
)

student_1.set_mark(Mark(4, subject_python))
student_1.set_mark(Mark(9, subject_java))
student_2.set_mark(Mark(10, subject_python))
student_2.set_mark(Mark(8, subject_java))
student_3.set_mark(Mark(6, subject_python))
student_3.set_mark(Mark(6, subject_java))

for student in group.students:
    print(student.get_bio_info())
    student.statistics()
#    print(student.get_average_score())
    print(student_1.is_excellent())
