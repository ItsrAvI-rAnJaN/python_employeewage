import random


class Employee:
    def emp_mnth_wage(self):
        is_part_time = 1
        is_full_time = 2
        emp_rate_per_hrs = 20
        num_of_wrkng_days = 20
        emp_hrs = 0
        total_emp_wage = 0

        for day in range(num_of_wrkng_days):
            emp_check = random.randrange(0, 3)
            if emp_check == is_full_time:
                # print("Employee is worinking Full TIme")
                emp_hrs = 8
            elif emp_check == is_part_time:
                # print("Employee is working Part time")
                emp_hrs = 4
            else:
                # print("Employee is Absent")
                emp_hrs = 0

            emp_wage = emp_hrs*emp_rate_per_hrs
            total_emp_wage += emp_wage

        print("Total Employee Wage of a Month :", total_emp_wage)


if __name__ == "__main__":
    obj_emp = Employee()
    obj_emp.emp_mnth_wage()
