class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lection(self, lector, rate, course):
        if isinstance(lector, Lector) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.rates:
                lector.rates[course] += [rate]
            else:
                lector.rates[course] = [rate]
        else:
            print('Ошибка')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lector(Mentor):
    def __init__(self, *args):
        super().__init__(*args)
        self.rates = {}


best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python']

normal_student = Student('John', 'Cena', 'man')
normal_student.courses_in_progress += ['Java']

cool_lector = Lector('Some', 'Buddy')
cool_lector.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Java']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)

best_student.rate_lection(cool_lector, 10, 'Python')
normal_student.rate_lection(cool_lector, 10, 'Java')

print(best_student.grades)
print(cool_lector.rates)