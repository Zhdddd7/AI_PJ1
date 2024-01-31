# Project 1 Informed Search

## 1. Problem
You are given a separate maze file in text format. In this maze, you can go up, down, left, or right. The maze is 81*81 binary matrix where each line in the file represents a row, and its values are separated with a space. 1 indicates a block that you cannot pass. 0 indicates a clear space that you can pass from.
You should implement a program using Informed Search that reads this maze and takes any two points (start and end indices) as inputs and tells whether there is a path in this maze between such points. Please note that the index starts at 0 in the following points. For example, given the start point (1,1) and the end point (1, 8), your program outputs ‘YES’ if there exists at least one path between those two points and ‘NO’ if no path exists.
![maze example](maze.png)

## 2. A* Search
Using Graph search method to solve this problem   
### State space   

1. maze[81][81]: has a value space {0, 1}
2. path: a map, which record the previous node(value) of the current node(key): {current node: previous node}
3. open_set:  all nodes open to be calculated. The data structure used is a priority heap: [(f_score, node)…]   

### Search strategy

When searching for the next step, use (x-1, y) to present upwards, use (x+1, y) to present backwards, use (x, y-1) to present towards left, use (x, y+1) to present towards right.
### Border
0 <= x <= 81; 
0 <= y <= 81; 
### Start state & Goal state
The open_set is only start state when initializing. And according to the algorithm, the G_Scoreis are inf for the rest of the nodes in the graph. Every time we choose the lowest F_Score in the open_set, which means the estimated path cost passing by this node.   
When the start point is equal to the end point, the search returns true and the path is also found.
### Heuristic method
A* algorithm uses F_Score= G_Score + H_Score to select the search direction.
For G_Score: The cost from start to the current position. For each move, the cost between previous node and current node is 1.
For H_Score: Computes the Manhattan distance between two points.
### update strategy
```
for neighbor in self.neighbors(current):
    temp_g_score = g_score[current] + 1
```
for every neighbor, we can calculate the current temp g_score, which measures the cost from start to the current position.
```
if temp_g_score < g_score.get(neighbor, float('inf')):
    path[neighbor] = current
```
This is a standard update strategy in A* algorithm. For the current node and now considering neighbor, we have the following cases:
1. this neighbor is first visited, it was assigned the inf value, so the neighbor node is sure to be add to the open set.
2. this neighbor has been visited before, so it has a finite value. However, now we found the new g_score is less than the previous one, which means a less cost(equal cost is not necessary to be updated) to reach the same position. Update this node state. 
