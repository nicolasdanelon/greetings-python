import unittest

from src.greetings.sayhi import SayHi

class TestGreetingClass(unittest.TestCase):

    def test_greeting(self):
        say_hi = SayHi("Nicolas")
        result = say_hi.greeting()
        self.assertEqual(result, "Greeting I'm Nicolas, emissary of the Gorgonites")

