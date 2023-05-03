def dfs(graph, start, goal, visited=None, stack=None):
    if visited is None:
        visited = []
    if stack is None:
        stack = []

    traversal_path = []
    visited.append(start)
    stack.append(start)

    while visited:
        current_node = stack.pop()
        traversal_path.append(current_node)

        if current_node == goal:
            return traversal_path

        for element in graph[current_node]:
            if element not in visited:
                visited.append(element)
                stack.append(element)

    print("Path doesn't exist!!!")

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
print(*dfs(graph, start_state, goal_state))