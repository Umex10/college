# College Data Analysis Project

A data analysis project exploring college statistics using Python, pandas, and the ISLP (Introduction to Statistical Learning with Python) library.

## Overview

This project performs exploratory data analysis on a college dataset, examining various metrics such as acceptance rates, student demographics, and institutional characteristics.

## Requirements

- Python 3.x
- pandas
- ISLP (Introduction to Statistical Learning with Python)

## Installation

```bash
pip install pandas ISLP
```

## Running the Project

```bash
python Main.py
```

## Exercises

### Exercise 1: Data Cleaning
- Renames column names by replacing dots (`.`) with underscores (`_`) for better Python compatibility
- Makes column names more readable and accessible for pandas operations

### Exercise 2: Acceptance Rate Calculation
- Calculates the acceptance rate for each college using the formula: `(Accept / Apps) * 100`
- Adds a new `Acceptance_Rate` column to the dataset
- Displays the top 5 colleges with their application and acceptance statistics

### Exercise 3: Data Sorting
- Sorts the college dataset by two criteria:
  1. Private status (Yes/No)
  2. Number of applications received
- Demonstrates multi-column sorting in ascending order

### Exercise 4: Elite University Classification
- Creates a new `Elite` variable based on the percentage of students from the top 10% of their high school class
- Classifies colleges as "Elite" if more than 50% of students are from the top 10% of their class
- Adds the classification as a new column to the dataset

### Exercise 5: Summary Statistics
- Generates comprehensive descriptive statistics for all numerical variables
- Displays mean, standard deviation, min, max, and quartile values
- Transposes the output for better readability

### Exercise 6: Private vs Public Analysis
- Groups colleges by their private/public status
- Calculates mean values for key variables:
  - Acceptance Rate
  - Room & Board costs
  - Book costs
  - Percentage of faculty with PhDs
  - Graduation Rate
- Compares averages between private and public institutions

### Exercise 7: Combined Private & Elite Analysis
- Performs a two-way grouping by both `Private` and `Elite` status
- Calculates means for the same variables as Exercise 6
- Provides insights into how elite private, elite public, non-elite private, and non-elite public colleges compare

## Contributors

- **Friend Name**: Exercises 1-4 (Data cleaning, acceptance rate calculation, sorting, and elite classification)
- **Your Name**: Exercises 5-7 (Summary statistics and grouped analyses)

## Dataset

The project uses the College dataset from the ISLP library, which contains statistics for a large number of US colleges from the 1995 issue of US News and World Report.
