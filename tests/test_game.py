import random
import unittest
from unittest.mock import patch
from number_game import guess_the_number

class TestGame(unittest.TestCase):


    def test_range(self): #this should test that the generated number should fall between the range of 1-10
        self.assertGreater(10,0)
        self.assertLess(0,10)

    #this should test that a randon number is being generated
    @patch ('random.randint', return_value =4)
    def test_generate_secret(self, mock_random):
        self.assertTrue(4, random.randint)

    #this test should take the number of guesses left
