# The Torchbearer

**Student Name:** Keo Minato
**Student ID:** 130882684
**Course:** CS 460 – Algorithms | Spring 2026


---

## Part 1: Problem Analysis


- **Why a single shortest-path run from S is not enough:**
  - _Because it only calculates the shortest path from the starting node to all other nodes. It doesn't calculate the route from start to end that visits all required nodes using the least amount of fuel._

- **What decision remains after all inter-location costs are known:**
  - _It must decide the optimal sequence of relics to visit to minimize fuel used._

- **Why this requires a search over orders (one sentence):**
  - _Because the order of which relics are visited result in different total fuel used. This means we have to explore each sequence of relics to see which one minimized fuel usage._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection


| Source Node Type | Why it is a source |
|---|---|
| _Start/Spawn_ | _Because we always start at start node S_ |
| _Relic_ | _Because we must visit all relic chambers in the set M_ |

### Part 2b: Distance Storage


| Property | Your answer |
|---|---|
| Data structure name | Hash table of hash tables |
| What the keys represent | _u_ represents the source node, _v_ represents the destination node |
| What the values represent | The minimum fuel cost from _u_ to _v_ |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Hash tables convert a key into an array index, so lookups go directly to the storage location |

### Part 2c: Precomputation Complexity


- **Number of Dijkstra runs:** _k+1 (represents all source nodes), where k = # of relics, and the +1 covers the start/spawn node_
- **Cost per run:** _O(mlogn) when using a min heap, where m = # of edges, and n = # of vertices_
- **Total complexity:** _O((k+1)(mlogn))_
- **Justification (one line):** _We have to do an entire Dijkstra run using a min heap (O(mlogn)) for each source node (k+1 nodes). These are independent runs, so we multiply the number of runs by the cost per run._

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  - _The distance from S to the finalizd nodes is the absolute shortest distance to get from S to each of the other nodes._

- **For nodes not yet finalized (not in S):**
  - _The distance from S to the nodes that aren't finalized is the shortest distance so far to get from S to all other nodes._

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  - _The distance of the start/spawn node is set to 0 and all of the other nodes are set to infinity._ 

- **Maintenance : why finalizing the min-dist node is always correct:**
  - _Because taking an alternative path would require you to go through an unfinalized node, the distance to the unfinalized node is at least the same distance as the distance to the finalized min-dist node (since we always pick the min at each step)._
  - _All edge weights are nonnegative, so taking any alternative path would either keep the distance the same or increase it._

- **Termination : what the invariant guarantees when the algorithm ends:**
  - _When the heap is empty, that means all reachable nodes have been finalized and all unreachable nodes are still set to infinity. This guarantees that the shortest path to every reachable node has been found._

### Part 3c: Why This Matters for the Route Planner

_When the planner tries to pick the order of which relics to go to, it would be relying on suboptimal distances, causing it to result in a suboptimal ordering._

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** 
  - _Greedy always chooses to go to the relic that is closest to the current node, this locally cheap step can force greedy into paths with expensive costs, which can make the total cost suboptimal._
- **Counter-example setup:** 
  - _S is the start/spawn node. A and B are relics. T is the exit. S->A = 2, S->B = 5, A->B = 25, B->A = 4, A->T = 1, B->T = 13._
- **What greedy picks:** 
  - _Greedy first chooses S->A = 2, then A->B = 25, and finally B->T = 13. Total of 40._
- **What optimal picks:** 
  - _Optimal chooses S->B = 5, B->A = 4, and finally A->T = 1. Total of 10._
- **Why greedy loses:** 
  - _Greedy loses because it chooses the local optimal path, S->A, at step 1 and saves 2 units of fuel._
  - _However, the decision forces greedy to take an expensive path to B before exiting._
  - _Greedy didn't have the global context to know that taking S->B first would cost him more in the beginning, but save total fuel in the end._

### What the Algorithm Must Explore

- _The algorithm has to explore all orders in which each of the relic chambers can be visited before exiting._

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc | node | The current node we are at in the graph |
| Relics already collected | relics_visited_order & relics_remaining | list[node] & set[node] | `relics_visited_order` = the relics that we have visitedso far (in order of when they were visited). `relics_remaining` = the relics that still need to be visited. |
| Fuel cost so far | cost_so_far | float | The amount of fuel that has been used to reach the current node. |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | Hash set |
| Operation: check if relic already collected | Time complexity: O(1) |
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | Every time we backtrack, we add and remove a relic. A hash set allows for constant insertions, deletions, and checks, which make backtracking efficient. |

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** _O(k!), where k = # of relic chambers._
- **Why:** _The algorithm has to calculate every order of visiting all of the k relics._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- https://docs.python.org/3/library/heapq.html Used for part 2 in torchbearer.py for Dijkstra implementation. Verified by going to replit, copying my run_dijkstra() function and the graph from test 1 at the bottom of torchbearer.py, and then calling and printing the run_dijkstra() function. I then compared the function output to the output I got from hand tracing the graph. 
- https://www.geeksforgeeks.org/python/python-ways-to-remove-duplicates-from-list/ Used for part 2 in torchbearer.py for selecting sources. Verified by putting duplicated numbers in the sources list and then using list(set(sources)) and printing the result.
