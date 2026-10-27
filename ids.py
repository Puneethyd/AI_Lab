CUTOFF = 'cutoff'
FAILURE = 'failure'

def iterative_deepening_search(initial, goal, graph, maximum_depth):
    for depth in range(maximum_depth + 1):
        result = depth_limited_search(initial, goal, graph, depth, [])
        if isinstance(result, list):
            return result
    return FAILURE

def depth_limited_search(node, goal, graph, limit, path):
    if node == goal:
        return path + [node]
        
    if limit == 0:
        return CUTOFF
        
    cutoff_occurred = False
    neighbors = graph.get(node, [])
    
    for child in neighbors:
        if child not in path:
            result = depth_limited_search(child, goal, graph, limit - 1, path + [node])
            if isinstance(result, list):
                return result
            if result == CUTOFF:
                cutoff_occurred = True
                
    if cutoff_occurred:
        return CUTOFF
    else:
        return FAILURE

if __name__ == "__main__":
    print("--- Test Case 1 ---")
    graph1 = {'A': ['B', 'C'], 'B': [], 'C': []}
    print(iterative_deepening_search('A', 'B', graph1, 3))

    print("\n--- Test Case 2 ---")
    graph2 = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': [], 'E': [], 'F': [], 'G': []}
    print(iterative_deepening_search('A', 'G', graph2, 3))

    print("\n--- Test Case 3 ---")
    graph3 = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}
    print(iterative_deepening_search('A', 'Z', graph3, 2))

    print("\n--- Test Case 4 ---")
    graph4 = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': [], 'E': [], 'F': [], 'G': []}
    print(iterative_deepening_search('A', 'G', graph4, 2))

    print("\n--- Test Case 5 ---")
    graph5 = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
    print(iterative_deepening_search('A', 'Z', graph5, 2))
