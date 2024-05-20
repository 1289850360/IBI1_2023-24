class Student:
    def __init__(students, name, major, code_portfolio_score, group_project_score, exam_score):
        students.name = name
        students.major = major
        students.code_portfolio_score = code_portfolio_score
        students.group_project_score = group_project_score
        students.exam_score = exam_score

    def print_details(students):
        print('Name: {}, Major: {}, Code Portfolio Score: {}, Group Project Score: {}, Exam Score: {}'.format(
            students.name, students.major, students.code_portfolio_score, students.group_project_score, students.exam_score))

# Example
student1 = Student('He Yiyang', 'BMI', 100, 100, 100)
student1.print_details()
