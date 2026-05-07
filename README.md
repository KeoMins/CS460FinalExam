# The Torchbearer

**Student Name:** Keo Minato
**Student ID:** 130882684
**Course:** CS 460 – Algorithms | Spring 2026


---

## Part 1: Problem Analysis


- **Why a single shortest-path run from S is not enough:**
  _Because it only calculates the shortest path from the starting node to all other nodes. It doesn't calculate the route from start to end that visits all required nodes using the least amount of fuel._

- **What decision remains after all inter-location costs are known:**
  _It must decide the optimal sequence of relics to visit to minimize fuel used._

- **Why this requires a search over orders (one sentence):**
  _Because the order of which relics are visited result in different total fuel used. This means we have to explore each sequence of relics to see which one minimized fuel usage._

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

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _Your answer here._

- **For nodes not yet finalized (not in S):**
  _Your answer here._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _Your answer here._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Your answer here._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _Your answer here._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Your answer here._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

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
