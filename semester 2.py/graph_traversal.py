from collections import deque

# representasi graph menggunakan adjacency list
adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# representasi graph menggunakan adjacency matrix
nodes = ['A', 'B', 'C', 'D']
adj_matrix = [
    [0, 1, 1, 0],  # A
    [1, 0, 0, 1],  # B
    [1, 0, 0, 1],  # C
    [0, 1, 1, 0]   # D
]

# fungsi DFS rekursif dengan adjacency list
def dfs_list(node, visited, graph):
    visited.add(node)
    print(node, end=' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_list(neighbor, visited, graph)

# fungsi DFS dengan adjacency matrix
def dfs_matrix(start_index, visited):
    print(nodes[start_index], end=' ')
    visited[start_index] = True
    for i in range(len(adj_matrix[start_index])):
        if adj_matrix[start_index][i] == 1 and not visited[i]:
            dfs_matrix(i, visited)

# fungsi BFS dengan adjacency list
def bfs_list(start_node, graph):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# fungsi BFS dengan adjacency matrix
def bfs_matrix(start_index):
    visited = [False] * len(nodes)
    queue = deque([start_index])
    visited[start_index] = True

    while queue:
        idx = queue.popleft()
        print(nodes[idx], end=' ')
        for i in range(len(nodes)):
            if adj_matrix[idx][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

# output
def main():
    print("Pilih representasi graf:")
    print("1. Adjacency List")
    print("2. Adjacency Matrix")
    choice = input("Masukkan pilihan (1/2): ").strip()

    print("\n=== Traversal DFS dari A ===")
    if choice == '1':
        dfs_list('A', set(), adj_list)
    elif choice == '2':
        dfs_matrix(0, [False]*len(nodes))
    else:
        print("Pilihan tidak valid.")
        return

    print("\n\n=== Traversal BFS dari A ===")
    if choice == '1':
        bfs_list('A', adj_list)
    elif choice == '2':
        bfs_matrix(0)
    else:
        return

    print("\n")  # newline penutup

if __name__ == '__main__':
    main()
