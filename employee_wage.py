import random


class Employee:
    def daily_wage(self):
        is_present = 1
        emp_rate_per_hrs = 20
        emp_hrs = 0
        emp_check = random.randrange(0, 2)
        if emp_check == is_present:
            print("Employee is Present")
            emp_hrs = 8
        else:
            print("Employee is Absent")
            emp_hrs = 0
        emp_wage = emp_hrs*emp_rate_per_hrs
        print("Employee Wage : ", emp_wage)


if __name__ == "__main__":
    obj_emp = Employee()
    obj_emp.daily_wage()
