import unittest

from Admin import Admin


class AdminTest(unittest.TestCase):

    def test_create_employee(self):
        actual = Admin("trick")
        expected = Admin("trick")
        self.assertNotEqual(actual, expected)

    def test_set_first_name_success(self):
        admin = Admin("trick")
        actual = admin.get_password()
        expected = "trick"
        self.assertEqual(actual, expected)
