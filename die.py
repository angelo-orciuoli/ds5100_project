# die.py

import numpy as np
import pandas as pd

class Die:
    """
    A Die object has N sides (faces) each with an associated weight.
    
    Faces can be strings or numbers, but must be unique.
    By default, each face is assigned an equal weight of 1.0, but weights can be changed.
    The die can be rolled to select a face based on its weights.
    
    Attributes:
        _die (pandas.DataFrame): Private DataFrame with faces as index and weights as a column.
    """
        
    def __init__(self, faces):
        """
        Initialize the Die with a given set of faces.
        
        Args:
            faces (numpy.ndarray): A 1D array of unique faces (strings or numbers).
        
        Raises:
            TypeError: If faces is not a NumPy array.
            ValueError: If faces are not unique.
        
        Behavior:
            - Assigns a default weight of 1.0 to each face.
            - Stores faces and weights in a private DataFrame.
        """

        # Check if faces is a NumPy array and values are unique
        if not isinstance(faces, np.ndarray):
            raise TypeError("faces must be an array")

        if len(faces) != len(np.unique(faces)):
            raise ValueError("faces must contain distinct values")

        # Initialize faces, weights, and DataFrame
        self.faces = faces
        self.weights = np.ones(len(faces))  # Default weight is 1.0
        self._die_df = pd.DataFrame({
            'weights': self.weights
        }, index=self.faces)


    def change_weight(self, face, new_weight):
        """
        Change the weight of a specified face.
        
        Args:
            face (str or number): The face whose weight is to be changed.
            new_weight (float): The new weight for the face.
        
        Raises:
            IndexError: If the given face is not found in the die.
            TypeError: If the new weight is not a number or cannot be cast to a float.
        
        Behavior:
            - Updates the weight for the specified face in the internal DataFrame.
        """

        if face not in self.faces: # Check if face exists and weight is numeric (int or float)
            raise IndexError(f"Face {face} not found in the die.")

        if not isinstance(new_weight, (int, float)):
            raise TypeError("Weight must be a numeric value.")

        self._die_df.at[face, 'weights'] = new_weight # Update weight in DataFrame


    def roll(self, num_rolls=1):
        """
        Roll the die one or more times and return the outcomes.
        
        Args:
            num_rolls (int): Number of times to roll the die (default is 1).
        
        Returns:
            list: A list of outcomes corresponding to the faces rolled.
        
        Behavior:
            - Randomly selects faces with replacement based on weights.
            - Does not store the roll outcomes internally.
        """

        if not isinstance(num_rolls, int) or num_rolls < 1: # Check if die is rolled at least once
            raise ValueError("Number of rolls must be at least 1.")

        # Sample with replacement using weights
        results = np.random.choice(
            self._die_df.index, # the faces
            size=num_rolls, # number of rolls
            replace=True,
            p=self._die_df['weights'] / self._die_df['weights'].sum()  # normalize weights
        )

        return results.tolist()
    

    def show(self):
        """
        Show the current state of the die (faces and weights).
        
        Returns:
            pandas.DataFrame: A copy of the internal DataFrame with faces and their weights.
        """

        return self._die_df.copy()