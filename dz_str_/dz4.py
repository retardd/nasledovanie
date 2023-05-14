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


#Средняя оценка лекторов на курсе
#Реализовал таким образом, что сначала суммируются средние оценки каждого лектора/студента,
#а потом делятся на общее кол-во лекторов/студентов
def avg_rate_lector(course, lectors_list):
    avg = 0
    for lector in lectors_list:
        if isinstance(lector, Lector) and course in lector.rates:
            avg += sum(lector.rates[course]) / len(lector.rates[course])
    return avg / len(lectors_list)

#Средняя оценка студентов на курсе
def avg_rate_students(course, students_list):
    avg = 0
    for student in students_list:
        if isinstance(student, Student) and course in student.grades:
            avg += sum(student.grades[course]) / len(student.grades[course])
    return avg / len(students_list)

#Создаем 2 студентов
best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python']
normal_student = Student('John', 'Cena', 'man')
normal_student.courses_in_progress += ['Python']

#Создаем 2 лекторов
cool_lector = Lector('Some', 'Buddy')
cool_lector.courses_attached += ['Python']
cool_lector2 = Lector('Some2', 'Buddy2')
cool_lector2.courses_attached += ['Python', 'Java']

#Создаем ревьювера
cool_reviewer = Reviewer('Some3', 'Buddy3')
cool_reviewer.courses_attached += ['Python', 'Java']

#Ставим оценки 2 студентам
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(normal_student, 'Python', 7)
cool_reviewer.rate_hw(normal_student, 'Python', 8)

#Ставим оценки лекторам (все происходит на курсе Python)
best_student.rate_lection(cool_lector, 10, 'Python')
best_student.rate_lection(cool_lector, 10, 'Python')
normal_student.rate_lection(cool_lector, 10, 'Python')
normal_student.rate_lection(cool_lector2, 10, 'Python')

print(f'Средняя оценка лекторов на к. Python {avg_rate_lector("Python", [cool_lector, cool_lector2])}', end='\n\n')
print(f'Средняя оценка студентов на к. Python {avg_rate_students("Python", [best_student, normal_student])}', end='\n\n')