import unittest

from user import User

class userTest(unittest.TestCase):
    def setUp(self):
        self.lewis=User("rickylui28@gmail.com","pass")

    def testRegistration(self):
        self.lewis.regUser("rickylui28@gmail.com","pass","pass")
        self.assertEqual(self.lewis.email,"rickylui28@gmail.com",msg="invalid email")
        self.assertEqual(self.lewis.password,"pass",msg="invalid password")

    def testLogin(self):
        self.lewis.logUser("rickylui28@gmail.com","pass")
        self.assertEqual(self.lewis.email,"rickylui28@gmail.com",msg="invalid email")
        self.assertEqual(self.lewis.password,"pass",msg="invalid pass")

    def testDeleteUser(self):
        self.lewis.delUser("rickylui28@gmail.com")
        self.assertEqual(self.lewis.email,"",msg="invalid name")
        self.assertEqual(self.lewis.password,"",msg="invalid name")