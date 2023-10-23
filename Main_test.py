import unittest
import Main as MainClass

class MainTest(unittest.TestCase):
    main = MainClass.Main()  # instantiate the Person Class

    # test case function to check the Person.set_name function
    def test_shall_pass(self):
        self.assertTrue(self.main.handle())
