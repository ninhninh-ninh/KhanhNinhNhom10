from src.core_logic import get_start_goal, get_neighbors, print_maze_with_path

def dfs(maze):
    start, goal = get_start_goal(maze)
    stack = [(start, [start])]
    visited = set([start])

    while stack:
        current, path = stack.pop()

        # Nếu tới đích thì in kết quả
        if current == goal:
            print("DFS tìm thấy đường đi!")
            print_maze_with_path(maze, path, len(visited))
            return path

        # Duyệt các ô lân cận
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))

    print("DFS không tìm thấy đường đi!")
    return None