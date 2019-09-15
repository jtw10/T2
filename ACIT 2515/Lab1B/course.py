class Course:
    """ Represents a course """

    def __init__(self, course_id, crn, school, program):
        """ Constructor for the course object """
        self._course_id = course_id
        self._crn = crn
        self._school = school
        self._program = program
        
        self._stud_list = []

    def add_student(self, stud_id):
        """ Add student to the course """
        if stud_id not in self._stud_list:
            self._stud_list.append(stud_id)

    def remove_student(self, stud_id):
        """ Remove student from the course """
        if stud_id in self._stud_list:
            self._stud_list.remove(stud_id)

    def check_enrollment(self, stud_id):
        """ Check if student is enrolled in the course """
        if stud_id in self._stud_list:
            return True
        else:
            return False

    def course_crn(self):
        """ Returns the course id and its corresponding CRN as a string """
        return (self._course_id + ' - ' + str(self._crn))

    def course_details(self):
        """ Returns course details in sentence form """
        if self._stud_list == []:
            return (self._course_id + ' (CRN ' + str(self._crn) + ') ' + 'is a course in the ' + self._program + ' program in the ' + self._school + ' with the following students: None')
        else:
            return (self._course_id + ' (CRN ' + str(self._crn) + ') ' + 'is a course in the ' + self._program + ' program in the ' + self._school + ' with the following students: ' + ', '.join(self._stud_list))
