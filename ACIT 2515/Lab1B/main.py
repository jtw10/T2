from course import Course


def main():
    """ Testing of the course class"""

    """ Creating an instance of the Course class for ACIT2515 """
    print('<--- ACIT 2515 --->')
    acit2515 = Course('ACIT 2515', 713456, 'BCIT School of Computing', 'CIT')
    acit2515.add_student('A01054709')
    acit2515.add_student('A01054938')
    acit2515.add_student('A00492893')
    acit2515.remove_student('A01054709')
    if acit2515.check_enrollment('A01054709') is False:
        print('I should be enrolled in ACIT2515!')
    print(acit2515.course_details())

    """ Creating an instance of the Course class for ACIT 1515 """
    print('<--- ACIT 1515 --->')
    acit1515 = Course('ACIT 1515', 340923, 'BCIT School of Computing', 'CIT')
    acit1515.add_student('A01054709')
    acit1515.add_student('A01054708')
    acit1515.add_student('A01054707')
    acit1515.add_student('A01054706')
    acit1515.add_student('A01054705')
    acit1515.remove_student('A01054707')
    acit1515.remove_student('A01054706')
    acit1515.remove_student('A01054705')
    acit1515.add_student('A01054709')
    print(acit1515.course_details())

    """ Creating an instance of the Course class for ACIT 1420 """
    print('<--- ACIT 1420 --->')
    acit1420 = Course('ACIT 1420', 348209, 'BCIT School of Computing', 'CIT')
    print(acit1420.course_details())


if __name__ == "__main__":
    main()
