# DS5100 Final Project: Monte Carlo Simulator

**Author:** Angelo Orciuoli  
**Version:** 0.1  
**License:** MIT  
**GitHub Repository:** [https://github.com/angelorciuoli2/ds5100_project](https://github.com/angelorciuoli2/ds5100_project)

A Python package for simulating dice games using Monte Carlo methods. The package includes modules for modeling dice (`Die`), running simulations (`Game`), and analyzing results (`Analyzer`).

## Synopsis

Below are examples demonstrating how to use the `Die`, `Game`, and `Analyzer` classes in the `montecarlo` package.

### Die
Create a die with custom faces and roll it.

```python
from montecarlo.die import Die

# Create a 6-sided die
die = Die(['1', '2', '3', '4', '5', '6'])

# Change the weight of a face
die.change_weight('6', 5.0)

# Roll the die 10 times
rolls = die.roll(10)

# Show die faces and weights
print(die.show())
```

### Game
Play a game with multiple dice.

```python
from montecarlo.game import Game

# Create three dice
d1 = Die(['1', '2', '3', '4', '5', '6'])
d2 = Die(['1', '2', '3', '4', '5', '6'])
d3 = Die(['1', '2', '3', '4', '5', '6'])

# Start a game with the dice
game = Game([d1, d2, d3])

# Play the game for 5 rolls
game.play(5)

# Output results in narrow format
game.show_results(form='narrow')
```

### Analyzer
Analyze the results of a game.

```python
from montecarlo.analyzer import Analyzer

# Create an analyzer for the game
analyzer = Analyzer(game)

# Outputs the number of jackpots
analyzer.jackpot()

# DataFrame indexed by roll number, with face values as columns and count values in cells
analyzer.face_count()

# MultiIndex DataFrame of distinct combinations and an associated counts column
analyzer.combo_count()

# MultiIndex DataFrame of distinct permutations and an associated counts column
analyzer.perm_count()
```

