import unittest

from greetings.sayhi import SayHi

class TestGreetingClass(unittest.TestCase):

    def test_greeting(self):
        say_hi = SayHi("Nicolas")
        result = say_hi.greeting()
        self.assertEqual(result, "Greeting I'm Nicolas, emissary of the Gorgonites")

    def test_greeting_without_name(self):
        say_hi = SayHi("")
        result = say_hi.greeting()
        self.assertEqual(result, "Greeting I'm , emissary of the Gorgonites")

    def test_greeting_with_none_name(self):
        say_hi = SayHi(None)
        result = say_hi.greeting()
        self.assertEqual(result, "Greeting I'm None, emissary of the Gorgonites")

    def test_say_hi_with_empty_name(self):
        self.assertRaises(TypeError, SayHi)
