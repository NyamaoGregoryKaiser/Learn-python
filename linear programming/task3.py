from pulp import LpProblem, LpVariable, LpMinimize, lpSum, value


V = [1, 2, 3, 4]  # Set of vertices
E = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]  # Edges
problem = LpProblem("Graph_Labeling", LpMinimize)
k = len(V)  # Max 
x = { (v, l): LpVariable(f"x_{v}_{l}", cat="Binary") for v in V for l in range(1, k + 1) }

y = {l: LpVariable(f"y_{l}", cat="Binary") for l in range(1, k + 1)}
problem += lpSum(y[l] for l in range(1, k + 1)), "Minimize_Labels"

# Constraints
# Each vertex = label
for v in V:
    problem += lpSum(x[v, l] for l in range(1, k + 1)) == 1, f"Vertex_{v}_Label"

for (u, v) in E:
    for l in range(1, k + 1):
        problem += x[u, l] + x[v, l] <= 1, f"Edge_{u}_{v}_Label_{l}"
for v in V:
    for l in range(1, k + 1):
        problem += x[v, l] <= y[l], f"Track_Label_{l}_for_Vertex_{v}"

problem.solve()

solution = {
    "labels_used": [l for l in range(1, k + 1) if value(y[l]) > 0.5],
    "vertex_labels": {v: [l for l in range(1, k + 1) if value(x[v, l]) > 0.5][0] for v in V},
    "objective": value(problem.objective)
}

print("Labels used:", solution["labels_used"])
print("Vertex Labels:", solution["vertex_labels"])
print("Objective Value (Minimized Labels):", solution["objective"])
