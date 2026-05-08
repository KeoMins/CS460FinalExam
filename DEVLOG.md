# Development Log – The Torchbearer

**Student Name:** Keo Minato
**Student ID:** 130882684


---

## Entry 1 – [05/06/2026]: Initial Plan

_I plan to implement the explanations in README.md first, starting from part 1. After completing the part in the README.md, I will switch over to torchbearer.py and start implementing the code for that part. Then I will add entries to the DEVLOG.md. I think part 6 will be difficult because it requires us to cut deadend plans early w/o ever cutting the optimal plan, which doesn't seem very intuitive. I plan to test by using the given tests at the bottom of torchbearer.py, and also by drawing out the graphs and tracing them._

---

## Entry 2 - [05/06/2026]: [Finished part 1 and started part 2]

_I finished part 1 and started part 2. I got through part 2a, but while implementing part 2b, I ran into some trouble. My initialization for the nodes in the graph weren't getting initialized to infinity correctly._

---

## Entry 3 – [05/07/2026]: [Fixed bug when initializing all nodes to infinity in run_dijkstra()]

_In part 2b, in the run_dijkstra() function, we have to initialize unreachable nodes to infinity. I assumed that the graph we were given contained every node as a key in the dictionary. However, I later realized that the code I wrote only initialized those keys to infinity. If a node only appeared as an edge target/neighbor and not a key, it wouldn't be initialized to infinity. I fixed this by getting all nodes in the graph (meaning keys and their edge targets/neighbors), and storing them in a new set called all_nodes and initializing them to infinity._

---

## Entry 4 – [05/07/2026]: [Finished parts 2, 3, 4, 5, and 6]

_I fixed the initialization bug in run_dijkstra() in part 2 and I also finished all of the remaining parts. I had some trouble with figuring out a lower bound to use in the pruning step in the `_explore()` function. I thought that maybe I could just use the shortest distance to the remaining relic plus the shortest distance from that relic to the exit node, but I ended up using the shortest distance from the current node to the exit node. This prunes more branches as is still safe because all valid routes have to eventually end at the exit. Because there are no negative edge weights, detours through other relic chambers can only increase the total cost._

---

## Entry 5 – [05/07/2026]: Post-Implementation Reflection

_After finishing my operating systems course, I think if I had more time I would try to implement the functions in part 5/6 in a low level language like C to help improve overhead. Python is very high level and has to be interpreted at runtime, but languages like C get translated into machine code before execution. Because of this, the `_explore()` recursion would run a lot faster. 

---

## Final Entry – [05/07/2026]: Time Estimate

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 0.5 |
| Part 2: Precomputation Design | 0.75 |
| Part 3: Algorithm Correctness | 1 |
| Part 4: Search Design | 1 |
| Part 5: State and Search Space | 0.75 |
| Part 6: Pruning | 1.5 |
| Part 7: Implementation | 3.5 |
| README and DEVLOG writing | 1.5 |
| **Total** | 10.5 |
