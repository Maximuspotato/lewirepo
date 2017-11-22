import unittest

from user import User

class userTest(unittest.TestCase):
    def setUp(self):
        self.lewis=User("rickylui28","pass")

    def testRegistration(self):
        self.lewis.regUser("rickylui28","pass","pass")
        self.assertEqual(self.lewis.email,"rickylui28",msg="invalid email")
        self.assertEqual(self.lewis.password,"pass",msg="invalid password")

    def testLogin(self):
        self.lewis.logUser("rickylui28","pass")
        self.assertEqual(self.lewis.email,"rickylui28",msg="invalid email")
        self.assertEqual(self.lewis.password,"pass",msg="invalid pass")