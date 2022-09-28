import random


class Employee:
    def attendance(self):
        is_present = 1
        emp_check = random.randrange(0, 2)
        if emp_check == is_present:
            print("Employee is Present")
        else:
            print("Employee is Absent")


if __name__ == "__main__":
    obj_emp = Employee()
    obj_emp.attendance()
