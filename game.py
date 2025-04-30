# game.py

import pandas as pd
pd.set_option('display.multi_sparse', False) # Display MultiIndex without collapsing levels
from die import Die

class Game:
    """
    A Game object consists of rolling one or more similar dice (Die objects) one or more times and then saves result to DataFrame.
    
    'Similar dice' have the same number of sides and associated faces, though each die may have different weights.
    
    Attributes:
        _dice (list): A list of Die objects.
        _play_results (pandas.DataFrame): A private DataFrame storing the results of the most recent game play.
    """

    def __init__(self, dice):
        """
        Initialize the Game with a list of similar dice.
        
        Args:
            dice (list): A list of already-instantiated Die objects.
        
        Behavior:
            - Stores the list of dice for use in gameplay.
            - Validates that all dice are instances of Die.
            - Validates that all dice have the same faces (weights do not need to be the same).
        """

        # Check if input is Die objects list
        if not isinstance(dice, list) or not all(isinstance(die, Die) for die in dice): 
            raise TypeError("Input must be a list of Die objects.")

        # Check if dice have same number of faces and same face values
        reference_faces = list(dice[0].faces)  # Save first die's faces as reference
        for die in dice[1:]:
            if list(die.faces) != reference_faces:
                raise ValueError("All dice must have the same number and identical faces.")

        self.dice = dice
        self._play_results = None  # Store result


    def play(self, num_rolls=1):
        """
        Play the game by rolling all dice a specified number of times.
        
        Args:
            num_rolls (int): The number of times to roll all the dice.
        
        Behavior:
            - Rolls each die the specified number of times.
            - Stores the outcomes in a private DataFrame in wide format.
            - In the wide format, the index is the roll number and each die is a separate column.
        """

        # Check if die is rolled at least once
        if not isinstance(num_rolls, int) or num_rolls < 1: 
            raise ValueError("Number of rolls must be at least 1.")

        roll_results = [] # Initialize results list

        # Roll dice num_rolls times and store result
        for _ in range(num_rolls): 
            die_results = []
            for idx, die in enumerate(self.dice):
                result = die.roll(1)[0] # Calling roll function
                die_results.append(result)
            roll_results.append(die_results) # Store result

        # Results DataFrame from results list
        self._play_results = pd.DataFrame(roll_results, columns=[str(i) for i in range(len(self.dice))])
        self._play_results.index.name = "Roll Number" # Naming index
        
        return self._play_results


    def show_results(self, form='wide'):
        """
        Display the results of the most recent play.
        
        Args:
            form (str): Format of the returned DataFrame; either 'wide' (default) or 'narrow'.
        
        Returns:
            pandas.DataFrame: A copy of the results in the requested format.
        
        Behavior:
            - 'Wide' format: one column per die, with roll number as index.
            - 'Narrow' format: MultiIndex (roll number, die number) and a single outcome column.
        
        Raises:
            ValueError: If the form parameter is not 'wide' or 'narrow'.
        """

        # Check if a game has been played and Arg is valid
        if self._play_results is None:  
            raise ValueError("No play results found. Please play the game first.")

        if form not in ['wide', 'narrow']:
            raise ValueError("Invalid option for 'form'. Choose 'wide' or 'narrow'.")

        # SingleIndex DataFrame
        if form == 'wide':
            return self._play_results.copy()
        
        # MultiIndex DataFrame
        elif form == 'narrow':
            narrow_results = self._play_results.copy()
            narrow_results.columns = pd.MultiIndex.from_product([['Die Number'], narrow_results.columns])

            return narrow_results.copy()