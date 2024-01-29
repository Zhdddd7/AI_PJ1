def read_array(file_path: str)->None:
    array = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                numbers = line.split()
                array.append([int(num) for num in numbers])
        return array
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None
#1 indicates a block that you cannot pass. 0 indicates a clear space.
    
class Search:
    def __init__(self, maze) -> None:
        self.maze = maze
        self.path = []
        self.visited = set()

    def DFS(self, x: int, y: int, x_end: int, y_end: int) -> bool:
        if (x, y) == (x_end, y_end):
            self.path.append((x, y))
            return True

        if (x, y) in self.visited or self.maze[x][y] == 1:
            return False

        self.visited.add((x, y))
        self.path.append((x, y))

        # Define directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(self.maze) and 0 <= ny < len(self.maze[0]):
                if self.DFS(nx, ny, x_end, y_end):
                    return True

        # Backtrack
        self.path.pop()
        return False


file_path = 'maze.txt'
maze= read_array(file_path)
if maze is not None:
    print("Array read successfully!")

test_0 = Search(maze)
#input the start and end coordinate.
start = (1,2)
end = (2, 39)
if test_0.DFS(start[0], start[1], end[0], end[1]):
    print('YES')
else: 
    print('NO')
    
