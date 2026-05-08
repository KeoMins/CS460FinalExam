"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Keo Minato
Student ID:   130882684

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return (
        "Part 1: Problem Analysis \n"
        "   - Why a single shortest-path run from S is not enough: \n"
        "       - Because it only calculates the shortest path from the starting node to all other nodes. \n"
        "       - It doesn't calculate the route from start to end that visits all required nodes using the least amount of fuel. \n"
        "   - What decision remains after all inter-location costs are known: \n"
        "       - It must decide the optimal sequence of relics to visit to minimize fuel used. \n"
        "   - Why this requires a search over orders (one sentence): \n"
        "       - Because the order of which relics are visited result in different total fuel used. \n"
        "       - This means we have to explore each sequence of relics to see which one minimized fuel usage. \n"
    )


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    sources = [spawn] + relics
    return list(set(sources)) # Removes any duplicates


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    # Get all nodes (keys and neighbors) to ensure we initialize distances for all nodes in the graph
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        for v, _ in neighbors:
            all_nodes.add(v)

    # Initialization
    distances = {node: float('inf') for node in all_nodes}
    distances[source] = 0
    visited = set()
    min_heap = [(0, source)] # Start at the source node with distance 0

    while min_heap != []:
        curr_cost, u = heapq.heappop(min_heap)

        # Check if the current node has already been visited to avoid processing it multiple times
        if u in visited:
            continue
        visited.add(u)

        # Update distances for neighbors of u
        for v, edge_cost in graph.get(u, []):
            if v not in visited:
                new_cost = curr_cost + edge_cost
                # If a shorter path to v is found, update the distance and add it to the heap
                if new_cost < distances[v]:
                    distances[v] = new_cost
                    heapq.heappush(min_heap, (new_cost, v))
    return distances

def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    sources = select_sources(spawn, relics, exit_node)
    dist_hashTable = {}

    # Run Dijkstra's on each source
    for source in sources:
        dist_hashTable[source] = run_dijkstra(graph, source)
    return dist_hashTable



# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return (
        "Part 3a: What the Invariant Means \n"
        "   - For nodes already finalized (in S): \n"
        "      - The distance from S to the finalizd nodes is the absolute shortest distance to get from S to each of the other nodes. \n"
        "   - For nodes not yet finalized (not in S): \n"
        "       - The distance from S to the nodes that aren't finalized is the shortest distance so far to get from S to all other nodes. \n"
        "Part 3b: Why Each Phase Holds \n"
        "   - Initialization : why the invariant holds before iteration 1: \n"
        "       - The distance of the start/spawn node is set to 0 and all of the other nodes are set to infinity. \n"
        "   - Maintenance : why finalizing the min-dist node is always correct: \n"
        "       - Because taking an alternative path would require you to go through an unfinalized node, the distance to the unfinalized node is at least the same distance as the distance to the finalized min-dist node (since we always pick the min at each step). \n"
        "       - All edge weights are nonnegative, so taking any alternative path would either keep the distance the same or increase it. \n"
        "   - Termination : what the invariant guarantees when the algorithm ends: \n"
        "       - When the heap is empty, that means all reachable nodes have been finalized and all unreachable nodes are still set to infinity. This guarantees that the shortest path to every reachable node has been found. \n"
        "Part 3c: Why This Matters for the Route Planner \n"
        "   - When the planner tries to pick the order of which relics to go to, it would be relying on suboptimal distances, causing it to result in a suboptimal ordering. \n"
    )

# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return (
        "Why Greedy Fails \n"
        "   - The failure mode: \n"
        "       - Greedy always chooses to go to the relic that is closest to the current node, this locally cheap step can force greedy into paths with expensive costs, which can make the total cost suboptimal. \n"
        "   - Counter-example setup: \n"
        "       - S is the start/spawn node. A and B are relics. T is the exit. S->A = 2, S->B = 5, A->B = 25, B->A = 4, A->T = 1, B->T = 13. \n"
        "   - What greedy picks: \n"
        "       - Greedy first chooses S->A = 2, then A->B = 25, and finally B->T = 13. Total of 40. \n"
        "   - What optimal picks: \n"
        "       - Optimal chooses S->B = 5, B->A = 4, and finally A->T = 1. Total of 10. \n"
        "   - Why greedy loses: \n"
        "       - Greedy loses because it chooses the local optimal path, S->A, at step 1 and saves 2 units of fuel. \n"
        "       - However, the decision forces greedy to take an expensive path to B before exiting. \n"
        "       - Greedy didn't have the global context to know that taking S->B first would cost him more in the beginning, but save total fuel in the end. \n"
        "What the Algorithm Must Explore \n"
        "   - The algorithm has to explore all orders in which each of the relic chambers can be visited before exiting. \n"
    )


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    # Initialize the search state
    relics_remaining = set(relics)
    relics_visited_order = []
    cost_so_far = 0.0
    best = {'cost': float('inf'), 'order': []} # Keeps track of the best order and cost found so far

    _explore(dist_table, spawn, relics_remaining, relics_visited_order, cost_so_far, exit_node, best)

    # If no valid route was found return infinity for cost and an empty list for the order
    # Otherwise return the best total cost and the order of relics that achieves that cost
    if best['cost'] == float('inf'):
        return (float('inf'), [])
    return (best['cost'], best['order'])


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    
    # Base case: If there are no more relics to visit, calculate the cost to exit and update best if it's better
    if len(relics_remaining) == 0:
        total_cost = cost_so_far + dist_table.get(current_loc, {}).get(exit_node, float('inf'))
        if total_cost < best['cost']:
            best['cost'] = total_cost
            best['order'] = list(relics_visited_order)
        return
        
    # Pruning
    # The pruning is safe because if cost_so_far + lower_bound >= best solution found so far, 
    # then visiting more relics can only keep or increase the total cost (due to edge weights being nonnegative).
    # Therefore, we can safely prune this branch without discarding the optimal solution.
    lower_bound = dist_table.get(current_loc, {}).get(exit_node, float('inf'))
    if cost_so_far + lower_bound >= best['cost']:
        return

    # Recursive case: Explore each remaining relic as the next step
    for next_relic in list(relics_remaining):
        next_cost = dist_table.get(current_loc, {}).get(next_relic, float('inf'))
        # If the next relic is unreachable from the current location, skip it
        if next_cost == float('inf'):
            continue

        # Mark the next relic as visited and explore further
        relics_remaining.remove(next_relic)
        relics_visited_order.append(next_relic)
        _explore(dist_table, next_relic, relics_remaining, relics_visited_order, cost_so_far + next_cost, exit_node, best)

        # Backtracking: undo the changes to relics_remaining and relics_visited_order before exploring the next option
        relics_visited_order.pop()
        relics_remaining.add(next_relic)


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
