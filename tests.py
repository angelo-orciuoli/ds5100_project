# tests.py

import unittest
import numpy as np
import pandas as pd
from montecarlo.die import Die
from montecarlo.game import Game
from montecarlo.analyzer import Analyzer

class TestDie(unittest.TestCase):

    def setUp(self):
        """Set up a simple fair die for most tests"""
        self.faces = np.array(['A', 'B', 'C'])
        self.die = Die(self.faces)

    def test_init_(self):
        """
        1. Checks _die_df is a pandas DataFrame
        2. Checks faces were correctly set to DataFrame's index
        3. Checks weights were initialized correctly
        """
        self.assertIsInstance(self.die._die_df, pd.DataFrame) # 1. Checks data structure
        self.assertListEqual(self.die._die_df.index.tolist(), self.faces.tolist()) # 2. Checks index initialization
        self.assertTrue((self.die._die_df['weights'] == 1.0).all()) # 3. Checks weight initialization

    def test_change_weight(self):
        """
        1. Change the weight of a valid face and check it updates in the DataFrame
        2. Check that changing the weight of an invalid face raises IndexError
        3. Check that assigning a non-numeric weight raises TypeError
        """
        # 1. Valid weight change
        new_weight = 2.5
        self.die.change_weight('A', new_weight)
        self.assertEqual(self.die._die_df.at['A', 'weights'], new_weight)

        # 2. Invalid face (should raise IndexError)
        with self.assertRaises(IndexError):
            self.die.change_weight('Z', 3.0)

        # 3. Invalid weight type (should raise TypeError)
        with self.assertRaises(TypeError):
            self.die.change_weight('A', 'high')

    def test_roll(self):
        """
        1. Check that what is returned is a Python list
        2. Check that the list length matches the number of rolls requested
        3. Check that rolling with invalid input (e.g. 0 rolls) raises ValueError
        """
        num_rolls = 10
        results = self.die.roll(num_rolls)

        self.assertIsInstance(results, list) # 1. Valid return type
        self.assertEqual(len(results), num_rolls) # 2. Correct number of rolls
        with self.assertRaises(ValueError): # 3. Less than 1 roll raises ValueError
            self.die.roll(0)

    def test_show(self):
        """
        1. Check that return is DataFrame structure
        2. Check that return is copy and not original
        """
        self.assertIsInstance(self.die.show(), pd.DataFrame) # 1. Valid return type
        self.assertIsNot(self.die.show(), self.die._die_df) # 2. Checks return is not original object


class TestGame(unittest.TestCase):

    def setUp(self):
        """Set up a simple fair die for most tests"""
        self.faces = np.array(['A', 'B', 'C'])
        self.die1 = Die(self.faces)
        self.die2 = Die(self.faces)
        self.game = Game([self.die1, self.die2])

    def test_init_(self):
        """
        1. Check that the argument is a list of Die objects
        2. Check that all dice have the same number of faces
        """
        # 1. Check that the argument is a list of Die objects
        with self.assertRaises(TypeError):
            Game([self.die1, "not_a_die"])  # Invalid die in list
        
        # 2. Check that all dice have the same faces
        die3 = Die(np.array(['A', 'B', 'D']))  # Different faces
        with self.assertRaises(ValueError):
            Game([self.die1, die3])  # Dice faces mismatch

    def test_play(self):
        """
        1. Check that play function creates the correct DataFrame format
        2. Check that ValueError is raised if num_rolls < 1
        """
        # 1. Check correct DataFrame format (wide format)
        self.game.play(5)
        self.assertIsInstance(self.game._play_results, pd.DataFrame)
        self.assertEqual(self.game._play_results.shape[1], 2)  # 2 dice in the game

        # 2. Check ValueError is raised if num_rolls < 1
        with self.assertRaises(ValueError):
            self.game.play(0)  # Invalid number of rolls

    def test_show_results(self):
        """
        1. Check that ValueError is raised if no game has been played
        2. Check that ValueError is raised for invalid 'form' argument
        3. Check both 'wide' and 'narrow' formats
        """
        # 1. Check ValueError is raised if no game has been played
        empty_game = Game([self.die1, self.die2])
        with self.assertRaises(ValueError):
            empty_game.show_results()  # No game played yet

        # 2. Check ValueError is raised for invalid 'form' argument
        self.game.play(5)  # Make sure a game is played
        with self.assertRaises(ValueError):
            self.game.show_results(form='invalid_form')  # Invalid 'form' value

        # 3. Check 'wide' and 'narrow' formats
        wide_results = self.game.show_results(form='wide')
        self.assertIsInstance(wide_results, pd.DataFrame)

        narrow_results = self.game.show_results(form='narrow')
        self.assertIsInstance(narrow_results, pd.DataFrame)
        self.assertTrue(narrow_results.columns.nlevels == 2)  # MultiIndex columns in narrow format


class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        """Create a die and play a simple game with 3 rolls and 3 dice"""
        self.die = Die(np.array([1, 2, 3]))
        self.game = Game([self.die, self.die, self.die])
        self.game.play(3)
        self.analyzer = Analyzer(self.game)

    def test_init_(self):
        """
        Check that argument is a Game object
        """
        with self.assertRaises(ValueError):
            Analyzer("not a game object")

    def test_jackpot(self):
        """
        Check that returned number of jackpots is an integer
        """
        self.assertIsInstance(self.analyzer.jackpot(), int)

    def test_face_count(self):
        """
        1. Check that returned object is pandas DataFrame
        2. Check that DataFrame columns match die faces
        3. Check each roll has a row
        """
        df = self.analyzer.face_count()
        self.assertIsInstance(df, pd.DataFrame) # 1. Valid return type
        self.assertEqual(set(df.columns), set(self.die.faces)) # 2. Correct number of columns
        self.assertEqual(df.shape[0], 3) # 3. Correct number of rows

    def test_combo_count(self):
        """
        1. Check that returned object is pandas DataFrame
        2. Check that index is a MultiIndex
        3. Check that DataFrame has a 'count' column
        """
        df = self.analyzer.combo_count()
        self.assertIsInstance(df, pd.DataFrame)  # 1. Valid return type
        self.assertIsInstance(df.index, pd.MultiIndex)  # 2. Correct index type
        self.assertIn('count', df.columns)  # 3. Count column present

    def test_perm_count(self):
        """
        1. Check that returned object is pandas DataFrame
        2. Check that index is a MultiIndex
        3. Check that DataFrame has a 'count' column
        """
        df = self.analyzer.perm_count()
        self.assertIsInstance(df, pd.DataFrame)  # 1. Valid return type
        self.assertIsInstance(df.index, pd.MultiIndex)  # 2. Correct index type
        self.assertIn('count', df.columns)  # 3. Count column present