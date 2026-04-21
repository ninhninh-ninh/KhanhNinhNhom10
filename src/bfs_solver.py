from collections import deque
from src.core_logic import get_start_goal, get_neighbors, print_maze_with_path

def bfs(maze):
    start, goal = get_start_goal(maze)
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        # Nếu tới đích thì in kết quả
        if current == goal:
            print("BFS tìm thấy đường đi!")
            print_maze_with_path(maze, path, len(visited))
            return path

        # Duyệt các ô lân cận
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    print("BFS không tìm thấy đường đi!")
    return None