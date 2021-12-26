import Person

"""
This is the class used to create a student. It inherits properties from the Person module.
It has the separate attributes the list_of_courses_of_offered, is_local() method, is_full_time() method, grades
"""


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

    # a decorated function to set the courses offered by students
    def set_course_list(self, name_of_course):
        if len(self.list_of_courses_offered) < 6:
            self.list_of_courses_offered.append(name_of_course)

    # a decorated function to set the grade of the course offered by the student
    def set_grade(self, name_of_course, course_score):
        for index, name in enumerate(self.list_of_courses_offered):
            if name is name_of_course:
                self.grades.append(course_score)
        else:
            print("Student does not offer the mentioned course")


student = Student("John", "Sampson",  "2000-12-18", "0545336286", is_local=True, is_full_time=False, grades=[34.5, 56.7],list_of_courses_offered=["Biology", "Chemistry"])
print(student)