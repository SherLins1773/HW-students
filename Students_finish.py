class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        sum_ = 0
        k = 0
        for course in self.grades:
            for grade in self.grades[course]:
                sum_ += grade
                k += 1
        return sum_ / k

    def __str__(self):
        return f"Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за домашнюю работу: {self.average_grade()} \n " \
               f"Курсы в процессе: {self.courses_in_progress} \n Завершенные курсы: {self.finished_courses} "

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student!')
            return
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        sum_ = 0
        k = 0
        for course in self.grades:
            for grade in self.grades[course]:
                sum_ += grade
                k += 1
        return sum_ / k

    def __str__(self):
        return f"Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за домашнюю работу: {self.average_grade()}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer!')
            return
        return self.average_grade() < other.average_grade()


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
        return f"Имя: {self.name} \n Фамилия: {self.surname}"


def avr_course(students, course):
    sum_ = 0
    i = 0
    for scholar in students:
        if isinstance(scholar, Student) and course in scholar.courses_in_progress:
            for grade in scholar.grades[course]:
                sum_ += grade
                i += 1
    return sum_ / i

def avr_course_lect(lecturers, course):
    sum_ = 0
    i = 0
    for lect in lecturers:
        if isinstance(lect, Lecturer) and course in lect.courses_attached:
            for grade in lect.grades[course]:
                sum_ += grade
                i += 1
    return sum_ / i

student_1 = Student('Ruby', 'Eman', 'female')
student_1.courses_in_progress += ['Python']

student_2 = Student('Vanya', 'Egorov', 'non-binary')
student_2.courses_in_progress += ['Java']

student_3 = Student('Rock', 'Lee', 'male')
student_3.courses_in_progress += ['Python', 'Java']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Kate', 'Riddle')
reviewer_2.courses_attached += ['Java']

lecturer_1 = Lecturer('Gena', 'Vozov')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Alik', 'Ru')
lecturer_2.courses_attached += ['Java']

lecturer_3 = Lecturer('Sakura', 'Haruno')
lecturer_3.courses_attached += ['Python', 'Java']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)

reviewer_2.rate_hw(student_2, 'Java', 10)
reviewer_2.rate_hw(student_2, 'Java', 5)
reviewer_2.rate_hw(student_2, 'Java', 9)

reviewer_1.rate_hw(student_3, 'Python', 7)
reviewer_1.rate_hw(student_3, 'Python', 10)
reviewer_1.rate_hw(student_3, 'Python', 5)

reviewer_2.rate_hw(student_3, 'Java', 10)
reviewer_2.rate_hw(student_3, 'Java', 7)
reviewer_2.rate_hw(student_3, 'Java', 9)

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 9)

student_2.rate_lecturer(lecturer_2, 'Java', 10)
student_2.rate_lecturer(lecturer_2, 'Java', 10)
student_2.rate_lecturer(lecturer_2, 'Java', 8)

student_1.rate_lecturer(lecturer_3, 'Python', 8)
student_1.rate_lecturer(lecturer_3, 'Python', 3)
student_1.rate_lecturer(lecturer_3, 'Python', 9)

student_2.rate_lecturer(lecturer_3, 'Java', 7)
student_2.rate_lecturer(lecturer_3, 'Java', 5)
student_2.rate_lecturer(lecturer_3, 'Java', 8)

student_3.rate_lecturer(lecturer_3, 'Python', 5)
student_3.rate_lecturer(lecturer_3, 'Python', 8)
student_3.rate_lecturer(lecturer_3, 'Python', 9)

student_3.rate_lecturer(lecturer_3, 'Java', 7)
student_3.rate_lecturer(lecturer_3, 'Java', 3)
student_3.rate_lecturer(lecturer_3, 'Java', 8)

print(student_1)
print(student_2)
print(student_1 > student_2)

print(lecturer_1)
print(lecturer_2)
print(lecturer_1 > lecturer_2)

print(reviewer_1)
print(reviewer_2)

print(avr_course([student_2, student_3], 'Java'))
print(avr_course_lect([lecturer_3, lecturer_1], 'Python'))