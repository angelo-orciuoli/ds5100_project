# Monte Carlo Dice Simulator

A comprehensive Python package for simulating dice games and analyzing probability distributions using Monte Carlo methods. This project demonstrates advanced statistical modeling techniques through interactive dice simulations and real-world applications.

## Overview

Monte Carlo methods are powerful computational techniques for understanding complex probabilistic systems. This simulator provides:

- **Flexible Die Creation**: Custom dice with any number of faces and weighted probabilities
- **Multi-Die Simulations**: Large-scale games with multiple dice configurations
- **Statistical Analysis**: Comprehensive tools for analyzing patterns, frequencies, and distributions
- **Real-World Applications**: From basic probability to language modeling and word generation

Perfect for statisticians, game developers, educators, researchers, or anyone interested in probability theory and simulation techniques.

## Features

- 🎲 **Custom Dice**: Create dice with any faces (numbers, letters, symbols) and custom weights
- 🎮 **Game Simulation**: Run thousands of rolls with multiple dice configurations
- 📊 **Advanced Analytics**: Jackpot analysis, face counting, combination/permutation tracking
- 📈 **Visualization**: Built-in plotting capabilities for statistical insights
- 🔤 **Language Modeling**: Generate words using English letter frequency distributions
- 🧪 **Extensible Design**: Clean, object-oriented architecture for easy customization

## Quick Start

### Installation

```bash
git clone https://github.com/angelo-orciuoli/monte-carlo-simulator.git
cd monte-carlo-simulator
pip install -e .
```

### Basic Usage

```python
from montecarlo.die import Die
from montecarlo.game import Game
from montecarlo.analyzer import Analyzer
import numpy as np

# Create a weighted six-sided die
die = Die(np.array([1, 2, 3, 4, 5, 6]))
die.change_weight(6, 5.0)  # Make 6 five times more likely

# Run a simulation with multiple dice
game = Game([die, die, die])
game.play(1000)

# Analyze the results
analyzer = Analyzer(game)
jackpots = analyzer.jackpot()  # Count of all-same-face rolls
face_counts = analyzer.face_count()  # Detailed face frequency analysis

print(f"Jackpots found: {jackpots}")
print(f"Face distribution:\n{face_counts.mean()}")
```

## Demonstration Scenarios

The `scenarios.ipynb` notebook showcases three comprehensive use cases:

1. **Fair vs. Unfair Coins**: Demonstrates how weighted dice affect probability distributions and jackpot frequencies
2. **Six-Sided Dice Analysis**: Explores complex multi-die scenarios with various bias configurations
3. **English Word Generation**: Real-world application using letter frequencies to generate and validate English words

Run the notebook to see interactive visualizations and detailed statistical analysis.

## API Reference

### Die Class

Creates and manages individual dice with customizable faces and weights.

**Constructor:**
- `Die(faces, weights=None)`: Initialize with faces array and optional weights

**Methods:**
- `change_weight(face, weight)`: Modify the weight of a specific face
- `roll(num_rolls)`: Roll the die specified number of times
- `show()`: Display current faces and weights as DataFrame

### Game Class

Manages multi-die simulations and stores results.

**Constructor:**
- `Game(dice_list)`: Initialize with list of Die objects

**Methods:**
- `play(num_rolls)`: Execute the specified number of rolls for all dice
- `show_results(form='narrow')`: Return results as DataFrame (narrow or wide format)

### Analyzer Class

Provides statistical analysis tools for completed games.

**Constructor:**
- `Analyzer(game)`: Initialize with a completed Game object

**Methods:**
- `jackpot()`: Count rolls where all dice show the same face
- `face_count()`: DataFrame of face counts per roll
- `combo_count()`: Unique combinations with frequencies
- `perm_count()`: Unique permutations with frequencies

## Project Structure

```
monte-carlo-simulator/
├── montecarlo/           # Main package
│   ├── die.py           # Die class implementation
│   ├── game.py          # Game simulation engine
│   └── analyzer.py      # Statistical analysis tools
├── scenarios.ipynb      # Interactive demonstration notebook
├── tests.py            # Comprehensive test suite
├── english_letters.txt  # Letter frequency data
├── scrabble_words.txt  # English word dictionary
└── README.md           # This file
```

## Advanced Examples

### Weighted Coin Simulation

```python
# Create fair and unfair coins
fair_coin = Die(['H', 'T'])
unfair_coin = Die(['H', 'T'])
unfair_coin.change_weight('H', 5)  # Heads 5x more likely

# Compare jackpot frequencies
fair_game = Game([fair_coin, fair_coin])
unfair_game = Game([unfair_coin, unfair_coin])

fair_game.play(10000)
unfair_game.play(10000)

fair_analyzer = Analyzer(fair_game)
unfair_analyzer = Analyzer(unfair_game)

print(f"Fair coins jackpot rate: {fair_analyzer.jackpot() / 10000:.3f}")
print(f"Unfair coins jackpot rate: {unfair_analyzer.jackpot() / 10000:.3f}")
```

### Letter-Based Word Generation

```python
import pandas as pd

# Load English letter frequencies
letter_data = pd.read_csv('english_letters.txt', sep=r'\s+', header=None)
letter_die = Die(letter_data[0].values)

# Apply frequency weights
for i, (letter, freq) in letter_data.iterrows():
    letter_die.change_weight(letter, freq)

# Generate 4-letter combinations
word_game = Game([letter_die] * 4)
word_game.play(1000)

# Analyze for real English words
analyzer = Analyzer(word_game)
perms = analyzer.perm_count()

# Check against dictionary
vocab = pd.read_csv('scrabble_words.txt', header=None)
vocab_set = set(vocab[0].str.upper())
generated_words = [''.join(perm) for perm in perms.index]
valid_words = [word for word in generated_words if word in vocab_set]

print(f"Generated {len(valid_words)} valid English words!")
```

## Testing

Run the comprehensive test suite:

```bash
python tests.py
```

The test suite covers all major functionality including edge cases, error handling, and statistical accuracy validation.

## Contributing

This project welcomes contributions! Areas for enhancement include:

- Additional statistical analysis methods
- Performance optimizations for large simulations
- Extended visualization capabilities
- New demonstration scenarios
- Documentation improvements

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Angelo Orciuoli**  
[GitHub Profile](https://github.com/angelo-orciuoli)

---

*Explore the fascinating world of probability and statistics through interactive Monte Carlo simulation!*
