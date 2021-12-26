class Person:
    """
    This is a class that houses the common properties shared by professor and student classes
    These properties include their names, date_of_birth, phone_number, and address
    """

    # the init method for creating instances of the class
    def __init__(self, first_name, surname, date_of_birth, phone_number, address=None):
        self.first_name = first_name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        if address is None:
            self.address = []
        else:
            self.address = address


class Student(Person):
    # the init method for creating a student
    def __init__(self, first_name, surname, date_of_birth, phone_number, is_local, is_full_time, address=None, grades=None, list_of_courses_offered=None):
        super().__init__(first_name, surname, date_of_birth, phone_number, address)
        self.is_local = is_local
        self.is_full_time_student = is_full_time
        if grades is None:
            grades = []
        else:
            self.grades = grades
        if list_of_courses_offered is None:
            self.list_of_courses_offered = []
        else:
            self.list_of_courses_offered = list_of_courses_offered

        # a function to set the courses offered by students
    def set_course_list(self, name_of_course):
        if len(self.list_of_courses_offered) < 6:
            self.list_of_courses_offered.append(name_of_course)

        # a function to set the grade of the course offered by the student
    def set_grade(self, name_of_course, course_score):
        print(self.list_of_courses_offered)
        for name in self.list_of_courses_offered:
            if name == name_of_course:
                self.grades.append(course_score)


student = Student("John", "Sampson",  "2000-12-18", "0545336286", is_local=True, is_full_time=False, grades=[34.5, 56.7])
print(student.__dict__)
student.list_of_courses_offered = ["English", "Mathematics", "Biology"]
print(student.__dict__)
print(student.list_of_courses_offered)
student.set_grade('Biology', 87.9)
print(student.__dict__)