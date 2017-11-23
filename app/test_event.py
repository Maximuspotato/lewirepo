import unittest

from event import Event

class userTest(unittest.TestCase):
    def setUp(self):
        self.dunda=Event("bbqlive","entertainment","kicc")

    def testadd(self):
        self.dunda.addEvent("bbqlive","entertainment","kicc")
        self.assertEqual(self.dunda.name,"bbqlive",msg="invalid name")
        self.assertEqual(self.dunda.category,"entertainment",msg="invalid category")
        self.assertEqual(self.dunda.location,"kicc",msg="invalid location")

    def testUpdate(self):
        self.dunda.modifyEvent("raveup","entertainment","uhuru gardens")
        self.assertEqual(self.dunda.name,"raveup",msg="invalid name")
        self.assertEqual(self.dunda.category,"entertainment",msg="invalid category")
        self.assertEqual(self.dunda.location,"uhuru gardens",msg="invalid location")

    def testDelete(self):
        self.dunda.deleteEvent("bbqlive")
        self.assertEqual(self.dunda.name,"",msg="invalid name")
        self.assertEqual(self.dunda.category,"",msg="invalid category")
        self.assertEqual(self.dunda.location,"",msg="invalid location")

    def testSearch(self):
        self.dunda.searchEvent("bbqlive")
        self.assertEqual(self.dunda.name,"bbqlive",msg="invalid name")
        self.assertEqual(self.dunda.category,"entertainment",msg="invalid category")
        self.assertEqual(self.dunda.location,"kicc",msg="invalid location")

    