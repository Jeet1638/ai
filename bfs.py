from collections import deque

def bfs(graph, start, goal):
    traversal_path = []
    visited = [start]
    queue = deque([start])

    while queue:
        current_node = queue.popleft()
        traversal_path.append(current_node)
        if current_node == goal:
            return traversal_path
        for element in graph[current_node]:
            if element not in visited:
                visited.append(element)
                queue.append(element)
    
    print("Path Doesn't exist!!!")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}

start_state = input("Enter the start state: ")
goal_state = input("Enter the goal state: ")
print("Start state is", start_state, "and goal state is", goal_state)
print(*bfs(graph, start_state, goal_state))