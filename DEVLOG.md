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

## Entry 4 – [Date]: [Short description]

_Your entry here._

---

## Entry 5 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
