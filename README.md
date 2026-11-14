# Creating the `tennisplayermatches` Python Package

Brooke Huynh  
Stat 159, Fall 2026  

## Project Overview
In this project, I created a Python Package `tennisplayermatches` which retrieves an inputted player's career match data and visualizes the age difference between them and their opponent and result of a match for all games in their career.

## Data Source

The data is sourced from [Tennis Abstract](https://www.tennisabstract.com/).

## Repository Structure

```text
hw03-3-brooke-huynh/
├── pyproject.toml
├── src/
│   └── tennisplayermatches/
│       ├── __init__.py
│       ├── plot_data.py
│       └── retrieve_data.py
├── tests/
│   └── test_retrieve.py
├── .gitignore
└── README.md
```

- `src/` : Contains the core source code modules for data retrieval (`retrieve_data.py`) and data visualization (`plot_data.py`).
- `tests/`: Contains tests suites such as `test_retreive.py` to verify package functionality.


## How to Install

To install the `tennisplayermatches` package directly from GitHub:
```bash
pip install git+https://github.com/UCB-stat159-f26/hw03-3-brooke-huynh.git
```

When working in Python:
```bash
import tennisplayermatches as tpm
```


## Personal Reflection

This homework helped me better understand what goes into the creation of a Python package. In this assigment, I gained experience 
structuring modular Python code, organizing scripts, and managing package dependencies. I also got to deepen my understanding of 
establishing reproducible workflows, from taking raw data sourced from the web all the way to visualizing the cleaned output. 
Overall, this homework emphasized the importance of clear documentation, modularity, and reproducibility.
