import unittest

from Registerpage import RegisterPage


class TestRegisterPage(unittest.TestCase):

    def test_name(self):
        emp_1=RegisterPage()
        self.assertEqual(emp_1.page,RegisterPage)
    def test_ecrement(self):
        self.assertEqual(3,4)
        


if __name__=='__main__':
    unittest.main()