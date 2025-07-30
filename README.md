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

- **Custom Dice**: Create dice with any faces (numbers, letters, symbols) and custom weights
- **Game Simulation**: Run thousands of rolls with multiple dice configurations
- **Advanced Analytics**: Jackpot analysis, face counting, combination/permutation tracking
- **Visualization**: Built-in plotting capabilities for statistical insights
- **Language Modeling**: Generate words using English letter frequency distributions
- **Extensible Design**: Clean, object-oriented architecture for easy customization

## Project Structure

```
monte-carlo-simulator/
├── montecarlo/           # Main package
│   ├── die.py            # Die class
│   ├── game.py           # Game class
│   └── analyzer.py       # Analyzer class
├── tests.py              # Test suite
├── english_letters.txt   # Letter frequency data
├── scrabble_words.txt    # English word dictionary
└── README.md             # Project documentation
```

## Module Documentation

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


## Example

This [Demonstration Scenarios](https://angelo-orciuoli.github.io/monte-carlo-simulator/) page showcases the how the package is used through three real-world simulation scenarios, including weighted dice behavior, jackpot probability analysis, and English word generation using letter frequency distributions.


## Unit tests

Run the comprehensive test suite:

```bash
python tests.py
```

The test suite covers all major functionality including edge cases, error handling, and statistical accuracy validation.

## Outcomes

This project provides experience in applying Monte Carlo simulation techniques to probabilistic systems. Key competencies include constructing custom probability distributions, executing large-scale simulations, and conducting statistical analysis using Python. Emphasis is placed on object-oriented programming, data visualization, and interpretation of probabilistic outcomes. Real-world scenarios—such as coin bias detection and English word generation—demonstrate practical applications in statistics, computational modeling, and simulation-based inference.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
