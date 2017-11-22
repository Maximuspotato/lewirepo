import unittest

from event import Event

class userTest(unittest.TestCase):
    def setUp(self):
        self.bbq=Event("bbqlive","entertainment","kicc","lewis")
        self.eve

    def testadd(self):
        self.bbq.addEvent("bbqlive","entertainment","kicc","lewis")
        self.assertEqual(self.bbq.name,"bbqlive",msg="invalid name")

    def testUpdate(self):
        self.bbq.addEvent("raveup","entertainment","uhuru gardens","eve")
        self.assertEqual(self.bbq.name,"rave",msg="invalid name")

    