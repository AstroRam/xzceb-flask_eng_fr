"""Module providingFunction printing python version."""
import unittest
from translator import englishToFrench, french_english

class TestEnglish(unittest.TestCase): 
    """Function translating english to french"""
    def test1(self): 
        self.assertEqual(englishToFrench("Good Morning"),"Bonjour")# \nEOF
class TestFrench(unittest.TestCase): 
    """Function translating french to english"""
    def test1(self): 
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

unittest.main()
