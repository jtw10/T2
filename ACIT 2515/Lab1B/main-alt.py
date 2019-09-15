from student import Student

"""Creating an instance of the Student class for myself"""
print('<--- Student #0 --->')
myself = Student('josh', 'w', 'BCIT School of Computing', 'CIT')
myself.add_course('ACIT2420')
myself.add_course('ACIT2515')
myself.add_course('ACIT2520')
myself.add_course('ACIT2620')
myself.add_course('ACIT2831')
myself.add_course('COMM2216')
myself.add_course('MATH1350')
myself.remove_course('ACIT2515')
if myself.confirm_enrollment('ACIT2515') is False:
    print('I should be enrolled in ACIT2515!')
print(myself.student_summary())

"""Creating an instance of the Student class for classmate 1"""
print('<--- Student #1 --->')
classmate1 = Student('jim', 'bob', 'BCIT School of Computing', 'CIT')
classmate1.add_course('ACIT2515')
classmate1.add_course('ACIT2420')
classmate1.add_course('ACIT2520')
classmate1.add_course('ACIT2620')
classmate1.add_course('ACIT2831')
classmate1.add_course('COMM2216')
classmate1.add_course('MATH1350')
classmate1.add_course('ACIT2420')
classmate1.add_course('ACIT2515')
classmate1.remove_course('ACIT2520')
classmate1.remove_course('ACIT2620')
classmate1.remove_course('ACIT2831')
classmate1.remove_course('COMM2216')
classmate1.remove_course('MATH1350')
classmate1.add_course('ACIT2515')
print(classmate1.student_summary())

"""Creating an instance of the Student class for classmate 2"""
print('<--- Student #2 --->')
classmate2 = Student('dhruvdeep', 'singh',
                     'BCIT School of Geniuses', 'Smart People')
print(classmate2.student_summary())
