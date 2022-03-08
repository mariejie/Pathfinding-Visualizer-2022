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
```
22 18
2 2 5 5
3
4 4 5 9 8 10 9 5
8 12 8 17 13 12
11 1 11 6 14 6 14 1
```

## Breadth-first search
![Screenshot from 2022-03-07 23-52-00](https://user-images.githubusercontent.com/83217673/157216697-6011ebcb-ab82-4704-81cc-a999e6377215.png)

## Uniform-cost search
![Screenshot from 2022-03-07 23-52-00](https://user-images.githubusercontent.com/83217673/157216697-6011ebcb-ab82-4704-81cc-a999e6377215.png)

## Iterative deepening search
![Screenshot from 2022-03-08 00-47-25](https://user-images.githubusercontent.com/83217673/157216749-83cb9529-dfc2-4096-b466-ccca4c6a6148.png)

## Greedy best-firts search
![Screenshot from 2022-03-08 08-40-05](https://user-images.githubusercontent.com/83217673/157216924-1dce5eef-6767-4468-8333-02774be9431a.png)

