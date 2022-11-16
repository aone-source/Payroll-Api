import unittest

from Employee import Employee


class EmployeeTest(unittest.TestCase):

    def test_create_employee(self):
        actual = Employee("Test", "Test")
        expected = Employee("Test", "Test")
        self.assertNotEqual(actual, expected)

    def test_set_first_name_success(self):
        employee = Employee("Test", "Test")
        actual = employee.get_firstname()
        expected = "Test"
        self.assertEqual(actual, expected)


