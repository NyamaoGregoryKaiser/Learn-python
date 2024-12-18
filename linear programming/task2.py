from pulp import LpProblem, LpVariable, LpMaximize, value, PULP_CBC_CMD

def solve_knapsack():
    problem = LpProblem("Knapsack", LpMaximize)

    x1 = LpVariable("x1", lowBound=0, upBound=1)
    x2 = LpVariable("x2", lowBound=0, upBound=1)
    x3 = LpVariable("x3", lowBound=0, upBound=1)
    x4 = LpVariable("x4", lowBound=0, upBound=1)

    problem += 42 * x1 + 44 * x2 + 56 * x3 + 26 * x4
    problem += 80 * x1 + 87 * x2 + 53 * x3 + 50 * x4 <= 92

    problem.solve(PULP_CBC_CMD(msg=False))
    print("Initial LP Solution:")
    print(f"x1: {value(x1)}, x2: {value(x2)}, x3: {value(x3)}, x4: {value(x4)}")
    print(f"Objective: {value(problem.objective)}")

    def branch_and_bound(node_problem, variables):
        status = node_problem.solve(PULP_CBC_CMD(msg=False))
        if status != 1:  # Infeasible or unbounded
            return None

        solution = {var.name: value(var) for var in variables}
        objective = value(node_problem.objective)

        if all(int(val) == val for val in solution.values()):
            return {"solution": solution, "objective": objective}

        fractional_var = next((var for var in variables if not int(value(var)) == value(var)), None)
        if not fractional_var:
            return None

        left_problem = node_problem.copy()
        left_problem += (fractional_var <= int(value(fractional_var)))

        right_problem = node_problem.copy()
        right_problem += (fractional_var >= int(value(fractional_var)) + 1)

        left_result = branch_and_bound(left_problem, variables)
        right_result = branch_and_bound(right_problem, variables)

        if left_result and right_result:
            return left_result if left_result["objective"] > right_result["objective"] else right_result
        return left_result or right_result

    variables = [x1, x2, x3, x4]
    optimal_solution = branch_and_bound(problem, variables)

    if optimal_solution:
        print("\nOptimal Solution:")
        for var, val in optimal_solution["solution"].items():
            print(f"{var}: {val}")
        print(f"Objective: {optimal_solution['objective']}")
    else:
        print("No feasible solution found.")

if __name__ == "__main__":
    solve_knapsack()
