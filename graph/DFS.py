# 재귀를 이용한 DFS
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []

def dfs_recursion(adjacent_graph, cur_node, visited_array):
        visited_array.append(cur_node)

        for i in adjacent_graph[cur_node]:
            if i not in visited_array:
                dfs_recursion(adjacent_graph, i, visited_array)
            
        return

dfs_recursion(graph, 1, visited)
print(visited)

# 스택을 이용한 DFS
def dfs_stack(adjacent_graph, stack_node):
    stack = [stack_node]
    visited = []
    while stack:
        current_node = stack.pop()
        visited.append(current_node)
        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
        return visited
