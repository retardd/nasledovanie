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

    def __str__(self):
        return 'Имя: {}\nФамилия: {}\nСредняя оценка за домашние задания: {}' \
               '\nКурсы в процессе изучения: {}\nЗавершенные курсы: {}'.format(
            self.name, self.surname, sum(sum(x) for x in self.grades.values())/sum(len(x) for x in self.grades.values()),
        ','.join(self.courses_in_progress), ','.join(self.finished_courses))

    def __lt__(self, other):
        return sum([sum(x) for x in self.grades.values()]) < sum([sum(x) for x in other.grades.values()])

    def __le__(self, other):
        return sum([sum(x) for x in self.grades.values()]) <= sum([sum(x) for x in other.grades.values()])

    def __gt__(self, other):
        return sum([sum(x) for x in self.grades.values()]) > sum([sum(x) for x in other.grades.values()])

    def __ge__(self, other):
        return sum([sum(x) for x in self.grades.values()]) >= sum([sum(x) for x in other.grades.values()])

    def __eq__(self, other):
        return sum([sum(x) for x in self.grades.values()]) == sum([sum(x) for x in other.grades.values()])

    def __ne__(self, other):
        return sum([sum(x) for x in self.grades.values()]) != sum([sum(x) for x in other.grades.values()])



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

    def __str__(self):
        return 'Имя: {}\nФамилия: {}'.format(self.name, self.surname)

class Lector(Mentor):
    def __init__(self, *args):
        super().__init__(*args)
        self.rates = {}

    def __str__(self):
        return 'Имя: {}\nФамилия: {}\nСредняя оценка за лекции: {}'.format(self.name, self.surname,
                                                                           sum(sum(x) for x in self.rates.values())/sum(len(x) for x in self.rates.values()))

    def __lt__(self, other):
        return sum([sum(x) for x in self.rates.values()]) < sum([sum(x) for x in other.rates.values()])

    def __le__(self, other):
        return sum([sum(x) for x in self.rates.values()]) <= sum([sum(x) for x in other.rates.values()])

    def __gt__(self, other):
        return sum([sum(x) for x in self.rates.values()]) > sum([sum(x) for x in other.rates.values()])

    def __ge__(self, other):
        return sum([sum(x) for x in self.rates.values()]) >= sum([sum(x) for x in other.rates.values()])

    def __eq__(self, other):
        return sum([sum(x) for x in self.rates.values()]) == sum([sum(x) for x in other.rates.values()])

    def __ne__(self, other):
        return sum([sum(x) for x in self.rates.values()]) != sum([sum(x) for x in other.rates.values()])


#Создаем 2 студентов
best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python', 'Java']
normal_student = Student('John', 'Cena', 'man')
normal_student.courses_in_progress += ['Python', 'Java']

#Создаем 2 лекторов
cool_lector = Lector('Some', 'Buddy')
cool_lector.courses_attached += ['Python', 'Java']
cool_lector2 = Lector('Some2', 'Buddy2')
cool_lector2.courses_attached += ['Python', 'Java']

#Создаем ревьювера
cool_reviewer = Reviewer('Some3', 'Buddy3')
cool_reviewer.courses_attached += ['Python', 'Java']

#Ставим оценки 2 студентам
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Java', 10)
cool_reviewer.rate_hw(normal_student, 'Python', 7)
cool_reviewer.rate_hw(normal_student, 'Python', 8)
cool_reviewer.rate_hw(normal_student, 'Java', 8)

#Ставим оценки лекторам (все происходит на курсе Python)
best_student.rate_lection(cool_lector, 9, 'Python')
best_student.rate_lection(cool_lector, 9, 'Python')
normal_student.rate_lection(cool_lector, 7, 'Java')
best_student.rate_lection(cool_lector, 7, 'Java')
normal_student.rate_lection(cool_lector2, 10, 'Java')
best_student.rate_lection(cool_lector2, 9, 'Python')

#ПЕРЕГРУЗКА __STR__
print(cool_reviewer, end='\n\n')
print(cool_lector, end='\n\n')
print(best_student, end='\n\n')
print()

#ПЕРЕГРУЗКА СРАВНЕНИЙ
print(cool_lector > cool_lector2, end='\n\n')
print(cool_lector <= cool_lector2, end='\n\n')
print(best_student == normal_student, end='\n\n')
print(best_student >= normal_student, end='\n\n')
print()