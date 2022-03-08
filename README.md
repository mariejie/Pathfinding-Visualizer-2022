## Problem description
The robot has been sent to a maze of size M x N, and the robot has to find
the path from the Source (starting position) to the Goal (ending position).
The robot allows to move in 4 directions: up, down, left, right. In the maze,
there are some obstacles.
The student as asked to implement 5 search algorithms:
1. **Breadth-first search**
2. **Uniform-cost search**
3. **Iterative deepening search** that uses depth-first tree search as core
component and avoids loops by checking a new node against the
current path.
4. **Greedy-best first search** using the Manhattan distance as heuristic.
5. **Graph-search A** using the Manhattan distance as heuristic.

## Input/output format
- The format of the input file:
  - First line: the size of the maze width, height.
  - Second line: the position of the Source and Goal. For example: 2 2 19
16 meaning source point is (2, 2) and goal point is (19, 16).
  - Third line: the number of the obstacles in the maze.
  - The next following line, defining the obstacle by the rule:
    - The obstacle is a Convex polygon.
    - A polygon is a set of points that are next to each other
clockwise. The last point will be implicitly concatenated to the
first point to form a valid convex polygon.
- The output:
  - Graphical representation of polygons and path.
  - Cost.