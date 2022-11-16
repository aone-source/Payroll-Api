from Employee import Employee
from Exceptions import ValueIsNumberError
from Exceptions.ValueTooLargeError import ValueTooLargeError
from Exceptions.ValueTooSmallError import ValueTooSmallError

error = "Something went wrong. Please try again"


def verify_admin():
    flag = True
    check = "password"
    while flag:
        password = input("Please enter your password: ")
        if password != check:
            print("That is the wrong password. Please try again. ")
        else:
            print("Welcome to the Weekly Payroll Report Program")

            flag = False


def collect_num():
    while True:
        try:
            num = int(input("Enter the number of employees for this period: "))
            if num < 1:
                raise ValueTooSmallError
            break

        except ValueError as e:
            print(e)
            print("Please enter a number")

        except ValueTooSmallError:
            print("Please enter a rate greater or equal to 1")

        except Exception as e:
            print(e)
            print(error)

    return num


def collect_firstname(num):
    while True:
        try:
            firstname = input(f"Enter the first name of Employee #{num} ")
            if firstname.isnumeric():
                raise ValueIsNumberError
            break

        except TypeError as e:
            print(e)
            print("Names cannot start with a number. Please try again")

        except ValueIsNumberError:
            print("Names cannot start with a number. Please try again")

        except Exception as e:
            print(e)
            print(error)

    return firstname


def collect_lastname(num):
    while True:
        try:
            lastname = input(f"Enter the last name of Employee #{num} ")
            if lastname.isnumeric():
                raise ValueIsNumberError
            break

        except TypeError as e:
            print(e)
            print("Names cannot start with a number. Please try again")

        except ValueIsNumberError:
            print("Names cannot start with a number. Please try again")

        except Exception as e:
            print(e)
            print(error)

    return lastname


def collect_rate(num):
    while True:
        try:
            rate = float(input(f"Enter the hourly rate of Employee #{num} "))
            if rate < 1:
                raise ValueTooSmallError
            break

        except ValueError as e:
            print(e)
            print("Please enter a number")

        except ValueTooSmallError:
            print("Please enter a rate greater or equal to 1")

        except Exception as e:
            print(e)
            print(error)

    return rate


def collect_hours(num):
    while True:
        try:
            hours = float(input(f"Enter the total hours worked for Employee #{num} "))
            if hours < 1:
                raise ValueTooSmallError
            elif hours > 168:
                raise ValueTooLargeError
            break

        except ValueError as e:
            print(e)
            print("Please enter a number")

        except ValueTooSmallError:
            print("Please enter hours greater or equal to 1")

        except ValueTooLargeError:
            print("Please enter hours less than or equal to 168")

        except Exception as e:
            print(e)
            print(error)

    return hours


def display_key():
    print("{:^15} {:^15} {:^15} {:^15} {:^15} {:^15} {:^15} {:^15} {:^15} {:^15}".format
          ("Employee Name", "Hours Worked", "Pay Rate", "Regular Pay", "OT Pay",
           "Gross Pay", "Fed Tax", "State Tax", "FICA", "Net Pay"))


def create_employee(i):
    employee = Employee("None", "None")
    firstname = collect_firstname(i)
    lastname = collect_lastname(i)
    rate = collect_rate(i)
    hours = collect_hours(i)

    employee.set_id(i)
    employee.set_firstname(firstname)
    employee.set_lastname(lastname)
    employee.set_rate(rate)
    employee.set_hours(hours)
    employee.set_reg(rate, hours)
    employee.set_ot(rate, hours)
    employee.set_gross(rate, hours)
    employee.set_fed(rate, hours)
    employee.set_state(rate, hours)
    employee.set_fica(rate, hours)
    employee.set_net(rate, hours)

    return employee


def create_employees(num):
    employee_list = []
    i = 1
    while True:
        employee = create_employee(i)
        employee_list.append(employee)
        i += 1
        if i > num:
            break

    return employee_list


def display_payroll():
    display_key()


def run_program():
    verify_admin()

    while True:
        num = collect_num()
        employee_list = create_employees(num)
        print(f'{"PAYROLL":^175s}')
        print("-".center(175, "-"))
        display_payroll()
        i = 0

        while i <= employee_list.__len__() - 1:
            print(employee_list[i].__str__())
            i += 1

        again = input("Would you like to run payroll for another pay period? (Y/N) ")
        if again == "N" or again == "n":
            break
