import networkx as nx

def solve_min_cut(graph, source, sinks):
    # Step 1: Create a super-sink node
    super_sink = max(graph.nodes) + 1
    for sink in sinks:
        graph.add_edge(sink, super_sink, capacity=float('inf'))
    
    # Step 2: Compute the minimum cut using the max-flow algorithm
    cut_value, partition = nx.minimum_cut(graph, _s=source, _t=super_sink)
    reachable, non_reachable = partition
    
    # Step 3: Extract the edges in the minimum cut
    cut_edges = []
    for u in reachable:
        for v in graph[u]:
            if v in non_reachable:
                cut_edges.append((u, v))
    
    return cut_value, cut_edges

# Example usage
graph = nx.DiGraph()

# Define graph edges and capacities (effort to block)
graph.add_edge(1, 2, capacity=5)
graph.add_edge(1, 3, capacity=10)
graph.add_edge(2, 4, capacity=2)
graph.add_edge(3, 4, capacity=8)
graph.add_edge(3, 5, capacity=7)
graph.add_edge(4, 5, capacity=4)

source = 1  # Infection source
sinks = [4, 5]  # Nodes at risk

# Solve the minimum cut problem
cut_value, cut_edges = solve_min_cut(graph, source, sinks)

# Output results
print("Minimal Blocking Effort (Total Effort):", cut_value)
print("Edges to Block to Prevent Infection:")
for edge in cut_edges:
    print(edge)
