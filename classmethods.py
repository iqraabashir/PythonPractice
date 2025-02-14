class College:
    total_students = 0  # Shared class-level attribute for total students

    @classmethod
    def admit_student(cls):
        cls.total_students += 1  # Increment total student count
        print(f"Student admitted! Total students in college: {cls.total_students}")

    @classmethod
    def get_total_students(cls):
        return f"Total students in the college: {cls.total_students}"


class Department:
    @classmethod
    def admit_student_to_department(cls, department_name):
        print(f"Admitting a student to the {department_name} department...")
        College.admit_student()  # Call the College class method to update total students

# Admit students to different departments
Department.admit_student_to_department("Computer Science")
Department.admit_student_to_department("Electrical Engineering")
Department.admit_student_to_department("Mechanical Engineering")

# Get the total number of students in the college
print(College.get_total_students())