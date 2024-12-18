from pulp import LpProblem, LpVariable, LpMaximize, lpSum, value

# Data initialization (example data, replace with actual input)
students = ["S1", "S2", "S3", "S4"]  # List of students
projects = ["P1", "P2"]  # List of projects
teams = ["T1", "T2", "T3"]  # Teams for projects

# Preferences: desirability[s][t] represents the desirability of student s for team t
desirability = {
    ("S1", "T1"): 10, ("S1", "T2"): 7, ("S1", "T3"): 4,
    ("S2", "T1"): 8, ("S2", "T2"): 9, ("S2", "T3"): 5,
    ("S3", "T1"): 6, ("S3", "T2"): 8, ("S3", "T3"): 7,
    ("S4", "T1"): 7, ("S4", "T2"): 6, ("S4", "T3"): 9
}

# Team size limits (lower bound = 0, upper bound = 2 for simplicity)
team_limits = {
    "T1": (0, 2),
    "T2": (0, 2),
    "T3": (0, 2)
}

# Problem definition
problem = LpProblem("Student_Project_Assignment", LpMaximize)

# Variables: x[s][t] = 1 if student s is assigned to team t, 0 otherwise
x = { (s, t): LpVariable(f"x_{s}_{t}", cat="Binary") for s in students for t in teams }

# Objective: Maximize total desirability
problem += lpSum(desirability[s, t] * x[s, t] for s in students for t in teams)

# Constraints
# Each student is assigned to exactly one team
for s in students:
    problem += lpSum(x[s, t] for t in teams) == 1, f"One_Team_Per_Student_{s}"

# Team size limits
for t in teams:
    lower, upper = team_limits[t]
    problem += lpSum(x[s, t] for s in students) >= lower, f"Team_{t}_Lower_Bound"
    problem += lpSum(x[s, t] for s in students) <= upper, f"Team_{t}_Upper_Bound"

# Solve the problem
problem.solve()

# Output results
assignments = {s: t for s in students for t in teams if value(x[s, t]) > 0.5}
objective_value = value(problem.objective)

print("Assignments:", assignments)
print("Total Desirability (Objective Value):", objective_value)
