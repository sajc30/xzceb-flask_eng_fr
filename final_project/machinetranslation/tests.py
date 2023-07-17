import unittest
from deep_translator import MyMemoryTranslator
from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('hello'),'bonjour')
        self.assertEqual(english_to_french('goodbye'),'au revoir')
        self.assertNotEqual(english_to_french('hello'),'hello')
        
        

class TestMyModuleFrToEng(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('bonjour'),'hello')
        self.assertEqual(french_to_english('au revoir'),'goodbye')
        self.assertNotEqual(french_to_english('bonjour'),'bonjour')
        
        
        

unittest.main()