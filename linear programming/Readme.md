# Linear and Integer Programming Project

## Overview

This project contains solutions to various linear and integer programming problems, focusing on advanced optimization techniques including:

- Cutting Planes Algorithm
- Branch and Bound Method
- Mixed Integer Linear Programming (MILP) Modeling
- Network Flow Problem Solving
- Student-Project Assignment Optimization

## Project Structure

The project includes solutions for the following tasks:

### Task 1: Cutting Planes
- Implementation of the Gomory cutting plane algorithm
- Solving fractional optimal solutions

### Task 2: Branch and Bound
- Solution to a knapsack problem using branch and bound method
- Tracking linear programming relaxations and node processing

### Task 3-4: MILP Modeling
- Graph theory problem modeling
- Social network infection blocking problem

### Task 5: Student-Project Assignment Problem (SPAP)

#### Subtask 5.a
- Network flow problem formulation
- Total desirability optimization

#### Subtask 5.b
- Mixed integer linear programming model
- Fairness-oriented optimization

#### Subtask 5.c & 5.d
- Python implementation using Gurobi
- Solution quality analysis and comparison

## Prerequisites

- Python 3.x
- Gurobi Optimizer (recommended)
- Packages:
  - pandas
  - gurobipy (optional, for Gurobi solver)

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/linear-programming-project.git
cd linear-programming-project
```

2. Install required packages
```bash
python3 -m pip install pandas
```

3. (Optional) Install Gurobi
   - Follow Gurobi's official installation guide
   - Obtain a license (academic licenses are available)

## Usage

### Running the Code

```bash
python3 main.py
```

## Key Files

- `main.py`: Primary implementation of the models
- `load_data.py`: Data loading and preprocessing
- `check_sol.py`: Solution validation functions
- `data/`: Directory containing input data files

## Methodology

The project explores various optimization techniques:
- Linear Programming
- Integer Linear Programming
- Branch and Bound
- Cutting Planes
- Network Flow Modeling

## Performance Metrics

- Solution optimality
- Computational efficiency
- Social welfare maximization
- Fairness in assignment

## Limitations

- Requires Gurobi for full functionality
- Designed for specific problem instances
- Performance may vary with input data

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)

