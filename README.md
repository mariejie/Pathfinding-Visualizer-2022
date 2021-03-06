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
5. **Graph-search A Star** using the Manhattan distance as heuristic.

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
      - Required: `pygame`
  - Cost.
```
22 18
2 2 19 16
3
4 4 5 9 8 10 9 5
8 12 8 17 13 12
11 1 11 6 14 6 14 1
```

## Map

<img width="350" src="https://user-images.githubusercontent.com/83217673/157218345-59533c7c-eb16-4129-9a30-b0337983a8b3.png">

## Breadth-first search

<img width="350" src="https://user-images.githubusercontent.com/83217673/157218184-f1d57f76-849c-463a-b35e-b446aab5b914.png">

## Uniform-cost search

<img width="350" src="https://user-images.githubusercontent.com/83217673/157218184-f1d57f76-849c-463a-b35e-b446aab5b914.png">

## Iterative deepening search

<img width="350" src="https://user-images.githubusercontent.com/83217673/157218502-3b4e1317-469c-4fe5-8458-96f75185e22e.png">

## Greedy best-first search

<img width="350" src="https://user-images.githubusercontent.com/83217673/157245238-00b6d1e4-ea58-4bf4-afbd-2fcb6f635b7d.png">

## A Star

<img width="350" src="https://user-images.githubusercontent.com/83217673/157218758-c51b5c40-3002-4881-a8b5-36313ad885ff.png">


