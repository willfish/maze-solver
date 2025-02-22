# maze-solver

A simple UI-driven maze generator and solver

This is for personal learning and is not a serious project.

![2025-01-09-121059_806x806_scrot](https://github.com/user-attachments/assets/f050097d-77ad-40a6-9dd6-82a3b80f3ada)

It solves two problems:

1. It generates a grid and breaks down the walls of unvisited cells which has a best case complexity of linear O(m * n)
2. It solves the maze from a static starting cell (0, 0) to a static end cell (n - 1, m - 1) which has a best case complexity of O(d) - where d is the distance to the end from the start.

I'm using a BFS (Breadth First Search) approach to solve both of these problems in both a recursive and an iterative form. The iterative form is much better since it lets us maintain a much larger stack and therefore handle very deep traversal of large mazes.
