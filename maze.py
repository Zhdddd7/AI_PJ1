import heapq
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
#use the Manhatten distance 
class Search:
    def __init__(self, maze) -> None:
        self.maze = maze
        pass

    def heuristic(self, a: list[int]  , b: list[int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    #return the neighbor set of current point
    def neighbors(self, temp: (int, int)) ->list[(int, int)]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = temp
        result = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            #border and connectivity
            if 0 <= nx < len(self.maze) and 0 <= ny < len(self.maze[0]) and self.maze[nx][ny] == 0:
                result.append((nx, ny))
        return result

    # A* algorithm uses F= G + H to calculate the total cost to the target
    def A_Search(self, start, end) -> str:
        open_set = []
        # The open_set is a priority heap: (f_score, node)
        heapq.heappush(open_set, (0, start))
        # path is a map, {current node: previous node}
        path = {}
        # the score is a map: {node: score}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, end)}
        while open_set:
            _, current = heapq.heappop(open_set)

            if current == end:
                return 'YES'

            for neighbor in self.neighbors(current):
                temp_g_score = g_score[current] + 1
                if temp_g_score < g_score.get(neighbor, float('inf')):
                    path[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + self.heuristic(neighbor, end)
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
        # no node in the open_set, meanwhile the end point is not found.
        return 'NO'

file_path = 'maze.txt'
maze= read_array(file_path)
if maze is not None:
    print("Array read successfully!")

test_0 = Search(maze)
#input the start and end coordinate.
start = (1, 75)
end = (39, 40)
print("the start point is ", start)
print('the end point is', end)
print(test_0.A_Search(start, end))
