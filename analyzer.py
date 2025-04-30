# analyzer.py

import pandas as pd
pd.set_option('display.multi_sparse', False) # Display MultiIndex without collapsing levels
from game import Game

class Analyzer:
    """
    The Analyzer class takes a completed Game object and provides various analyses.

    Methods include counting jackpots (all faces the same in a roll),
    face counts per roll, distinct combination counts, and distinct permutation counts.

    Attributes:
        game (Game): A completed Game object containing roll results.
    """

    def __init__(self, game):
        """
        Initialize the Analyzer with a completed Game object.

        Args:
            game (Game): The Game object to analyze.

        Raises:
            ValueError: If the input is not an instance of the Game class.
        
        Behavior:
            - Stores the Game object for analysis.
        """

        # Check if input is Game object
        if not isinstance(game, Game):
            raise ValueError("Input must be a Game object.")

        self.game = game


    def jackpot(self):
        """
        Count the number of jackpots in the game.

        A jackpot is defined as a roll where all faces are identical.

        Returns:
            int: The number of jackpots found.
        """

        # Game results and jackpot count
        results = self.game._play_results
        jackpot_count = 0

        # Iterate through every roll
        for _, row in results.iterrows():
            if len(set(row)) == 1:  # Converts the row into set — sets only keep unique values
                jackpot_count += 1

        return jackpot_count


    def face_count(self):
        """
        Count the number of times each face appeared in each roll.

        Returns:
            pandas.DataFrame: A DataFrame indexed by roll number, with face values as columns
            and counts as cell values.
        """

        # Game results
        results = self.game.show_results(form='wide')

        # Face DataFrame
        stacked = results.stack()
        df = stacked.groupby(level=0).value_counts().unstack()
        df = df.reindex(columns=self.game.dice[0].faces, fill_value=0) # Ensure each face has a column
        df = df.fillna(0).astype(int) # Convert to int and fill NaN with 0
        df.columns.name = "Face Value"

        return df


    def combo_count(self):
        """
        Count distinct combinations of faces rolled, regardless of order.

        Returns:
            pandas.DataFrame: A DataFrame with a MultiIndex representing the combination
            of faces, and a single 'count' column for the number of occurrences.
        """

        # Game results
        results = self.game._play_results

        # Sort results and convert to tuple
        sorted_tuples = [tuple(sorted(row)) for _, row in results.iterrows()]

        # Count combinations and create DataFrame
        count = pd.Series(sorted_tuples).value_counts()
        df = count.to_frame(name='count')
        df.index = pd.MultiIndex.from_tuples(df.index, names=[str(i) for i in range(len(results.columns))])  # Set MultiIndex

        return df


    def perm_count(self):
        """
        Count distinct permutations of faces rolled, where order matters.

        Returns:
            pandas.DataFrame: A DataFrame with a MultiIndex representing the ordered
            faces rolled, and a single 'count' column for the number of occurrences.
        """

        # Game results
        results = self.game._play_results

        # Convert results to tuple
        tuples = [tuple(row) for _, row in results.iterrows()]

        # Count permutation and create DataFrame
        count = pd.Series(tuples).value_counts()
        df = count.to_frame(name='count')
        df.index = pd.MultiIndex.from_tuples(df.index, names=[str(i) for i in range(len(results.columns))]) # Set MultiIndex 

        return df