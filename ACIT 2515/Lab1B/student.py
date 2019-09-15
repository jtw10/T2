class Student:
    """Represents a student"""

    def __init__(self, f_name, l_name, school, program, courses=None):
        """Constructor for a student object"""
        self.f_name = f_name
        self.l_name = l_name
        self.school = school
        self.program = program

        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course_id):
        """Method to add course to a student"""
        if course_id not in self.courses:
            self.courses.append(course_id)

    def remove_course(self, course_id):
        """Method to remove course from a student"""
        if course_id in self.courses:
            self.courses.remove(course_id)

    def confirm_enrollment(self, course_id):
        """Method to check if a student is enrolled in a course"""
        if course_id in self.courses:
            return True
        else:
            return False

    def student_summary(self):
        """Method to print a summary of the student status"""
        if self.courses == []:
            return (self.f_name.capitalize() + ' ' + self.l_name.capitalize() + ' is a student in the ' + self.program + ' program in the ' + self.school + ' taking the following courses: None')
        else:
            return (self.f_name.capitalize() + ' ' + self.l_name.capitalize() + ' is a student in the ' + self.program + ' program in the ' + self.school + ' taking the following courses: ' + ', '.join(self.courses))
