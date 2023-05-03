def get_child(j1, j2, a, b):
    possibleValues = []
    if a == 0 and b == 0:
        possibleValues.append([j1, 0])
        possibleValues.append([0, j2])
    if a != 0:
        possibleValues.append([0, b])
    if b != 0:
        possibleValues.append([a, 0])
    if a != j1:
        possibleValues.append([j1, b])
    if b != j2:
        possibleValues.append([a, j2])
    if a != j1 and b <= j1 - a:
        possibleValues.append([a + b, 0])
    if b != j2 and a <= j2 - b:
        possibleValues.append([0, a + b])
    if a != j1 and b > j1 - a:
        possibleValues.append([a + (j1 - a), b - (j1 - a)])
    if b != j2 and a > j2 - b:
        possibleValues.append([a - (j2 - b), b + (j2 - b)])
    return possibleValues


def dfs(j1, j2, a, b, result, visited=[], stack=[]):
    traversalPath = []
    visited.append(str([a, b]))
    stack.append(str([a, b]))

    while visited != []:
        currentNode = eval(stack.pop())
        traversalPath.append(str(currentNode))
        if (currentNode[0] == result and currentNode[1] == 0) or (currentNode[1] == result and currentNode[0] == 0):
            return traversalPath
        childs = get_child(j1, j2, currentNode[0], currentNode[1])
        for child in childs:
            if str(child) not in visited:
                visited.append(str(child))
                stack.append(str(child))

    print("Path doesn't exist!!!")
    return None


result = dfs(3, 4, 0, 0, 2)
for index, data in enumerate(result):
    print(f"{index + 1} : {data}")