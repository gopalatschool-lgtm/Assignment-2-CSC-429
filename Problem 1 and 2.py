from collections import deque


# ============================================================
# NODE
# ============================================================

class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action


# ============================================================
# GET PATH
# ============================================================

def get_path(node):
    path = []

    while node is not None:
        path.append(node.state)
        node = node.parent

    path.reverse()
    return path


# ============================================================
# PROBLEM 1(a) and 1(b)
# GRAPH
#
#       A
#       |
#       B
#      / \
#     C   D
#     |   |
#     E   F
# ============================================================

graph = {
    "A": ["B"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": [],
    "F": []
}


# ============================================================
# BFS FOR GRAPH
# ============================================================

def bfs_graph(graph, start, goal):

    frontier = deque()
    frontier.append(Node(start))

    explored = set()
    traversal_order = []

    while frontier:

        node = frontier.popleft()#queue implementation

        if node.state in explored:
            continue

        explored.add(node.state)
        traversal_order.append(node.state)

        # Check if goal was found
        if node.state == goal:
            return get_path(node), traversal_order

        # Add children to queue
        for neighbor in graph[node.state]:

            if neighbor not in explored:

                child = Node(
                    neighbor,
                    parent=node,
                    action=neighbor
                )

                frontier.append(child)

    return None, traversal_order


# ============================================================
# DFS FOR GRAPH
# ============================================================

def dfs_graph(graph, start, goal):

    frontier = []
    frontier.append(Node(start))

    explored = set()
    traversal_order = []

    while frontier:

        node = frontier.pop()#stack implementation

        if node.state in explored:
            continue

        explored.add(node.state)
        traversal_order.append(node.state)

        # Check if goal was found
        if node.state == goal:
            return get_path(node), traversal_order

        # Reverse order so C is explored before D
        for neighbor in reversed(graph[node.state]):

            if neighbor not in explored:

                child = Node(
                    neighbor,
                    parent=node,
                    action=neighbor
                )

                frontier.append(child)

    return None, traversal_order


# ============================================================
# RUN BFS ON GRAPH
# ============================================================

print("=" * 60)
print("PROBLEM 1(a): BFS FROM A TO E IN GRAPH")
print("=" * 60)

bfs_path, bfs_order = bfs_graph(graph, "A", "E")

print("BFS Traversal:", " -> ".join(bfs_order))
print("BFS Path:", " -> ".join(bfs_path))


# ============================================================
# RUN DFS ON GRAPH
# ============================================================

print()
print("=" * 60)
print("PROBLEM 1(b): DFS FROM A TO E IN GRAPH")
print("=" * 60)

dfs_path, dfs_order = dfs_graph(graph, "A", "E")

print("DFS Traversal:", " -> ".join(dfs_order))
print("DFS Path:", " -> ".join(dfs_path))


# ============================================================
# PROBLEM 1(c), 1(d) and PROBLEM 2
#
# GRID FROM ASSIGNMENT
#
# 0 = OPEN CELL
# 1 = WALL
#
# Grid:
#
#       C0 C1 C2 C3 C4 C5
# R0    .  #  #  #  #  #
# R1    .  .  .  .  .  .
# R2    .  #  #  .  #  #
# R3    .  #  #  B  #  #
# R4    .  #  .  .  #  #
# R5    .  #  .  #  #  #
# R6    A  .  .  #  #  #
#
# A = (6, 0)
# B = (3, 3)
# ============================================================

grid = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1]
]

start = (6, 0)
goal = (3, 3)


# ============================================================
# GET VALID GRID NEIGHBORS
# ============================================================

def get_neighbors(position, grid):

    row, col = position

    # Order:
    # Up, Down, Left, Right
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        # Check that the position is inside the grid
        if 0 <= new_row < len(grid) and \
           0 <= new_col < len(grid[0]):

            # 0 means the cell is open
            if grid[new_row][new_col] == 0:

                neighbors.append((new_row, new_col))

    return neighbors


# ============================================================
# BFS FOR GRID
# ============================================================

def bfs_grid(grid, start, goal):

    frontier = deque()
    frontier.append(Node(start))

    explored = set()
    traversal_order = []

    while frontier:

        node = frontier.popleft()

        if node.state in explored:
            continue

        explored.add(node.state)
        traversal_order.append(node.state)

        # Goal found
        if node.state == goal:
            return get_path(node), traversal_order

        # Expand node
        for neighbor in get_neighbors(node.state, grid):

            if neighbor not in explored:

                child = Node(
                    neighbor,
                    parent=node,
                    action=neighbor
                )

                frontier.append(child)

    return None, traversal_order


# ============================================================
# DFS FOR GRID
# ============================================================

def dfs_grid(grid, start, goal):

    frontier = []
    frontier.append(Node(start))

    explored = set()
    traversal_order = []

    while frontier:

        node = frontier.pop()

        if node.state in explored:
            continue

        explored.add(node.state)
        traversal_order.append(node.state)

        # Goal found
        if node.state == goal:
            return get_path(node), traversal_order

        # Get neighbors
        neighbors = get_neighbors(node.state, grid)

        # Reverse order because this is a stack
        for neighbor in reversed(neighbors):

            if neighbor not in explored:

                child = Node(
                    neighbor,
                    parent=node,
                    action=neighbor
                )

                frontier.append(child)

    return None, traversal_order


# ============================================================
# PROBLEM 1(c): BFS ON GRID
# ============================================================

print()
print("=" * 60)
print("PROBLEM 1(c): BFS FROM A TO B IN GRID")
print("=" * 60)

bfs_grid_path, bfs_grid_order = bfs_grid(
    grid,
    start,
    goal
)

if bfs_grid_path:

    print("BFS Traversal:")
    print(bfs_grid_order)

    print("BFS Path:")
    print(bfs_grid_path)

    print("Path Length:", len(bfs_grid_path) - 1)

else:

    print("No path found.")
    print("Nodes explored:", bfs_grid_order)


# ============================================================
# PROBLEM 1(d): DFS ON GRID
# ============================================================

print()
print("=" * 60)
print("PROBLEM 1(d): DFS FROM A TO B IN GRID")
print("=" * 60)

dfs_grid_path, dfs_grid_order = dfs_grid(
    grid,
    start,
    goal
)

if dfs_grid_path:

    print("DFS Traversal:")
    print(dfs_grid_order)

    print("DFS Path:")
    print(dfs_grid_path)

    print("Path Length:", len(dfs_grid_path) - 1)

else:

    print("No path found.")
    print("Nodes explored:", dfs_grid_order)


# ============================================================
# PROBLEM 2: DEPTH-LIMITED SEARCH
# ============================================================

def dls_grid(grid, start, goal, depth_limit):

    frontier = []

    # Store:
    # (Node, depth)
    frontier.append((Node(start), 0))

    explored = set()
    traversal_order = []

    while frontier:

        node, depth = frontier.pop()

        if node.state in explored:
            continue

        explored.add(node.state)
        traversal_order.append(node.state)

        # Goal found
        if node.state == goal:
            return get_path(node), traversal_order

        # Do not expand beyond depth limit
        if depth >= depth_limit:
            continue

        neighbors = get_neighbors(node.state, grid)

        # Reverse because we are using a stack
        for neighbor in reversed(neighbors):

            if neighbor not in explored:

                child = Node(
                    neighbor,
                    parent=node,
                    action=neighbor
                )

                frontier.append(
                    (child, depth + 1)
                )

    return None, traversal_order


# ============================================================
# PROBLEM 2: DLS LIMIT = 6
# ============================================================

print()
print("=" * 60)
print("PROBLEM 2: DLS WITH DEPTH LIMIT = 6")
print("=" * 60)

dls6_path, dls6_order = dls_grid(
    grid,
    start,
    goal,
    6
)

if dls6_path:

    print("DLS Path:")
    print(dls6_path)

    print("Path Length:", len(dls6_path) - 1)

else:

    print("Goal not found within depth limit 6.")

print("Nodes explored:", dls6_order)
print("Number of nodes explored:", len(dls6_order))


# ============================================================
# PROBLEM 2: DLS LIMIT = 10
# ============================================================

print()
print("=" * 60)
print("PROBLEM 2: DLS WITH DEPTH LIMIT = 10")
print("=" * 60)

dls10_path, dls10_order = dls_grid(
    grid,
    start,
    goal,
    10
)

if dls10_path:

    print("DLS Path:")
    print(dls10_path)

    print("Path Length:", len(dls10_path) - 1)

else:

    print("Goal not found within depth limit 10.")

print("Nodes explored:", dls10_order)
print("Number of nodes explored:", len(dls10_order))


# ============================================================
# COMPARISON
# ============================================================

print()
print("=" * 60)
print("COMPARISON")
print("=" * 60)

print("""
BFS:
- Uses a queue (FIFO).
- Explores the shallowest nodes first.
- Finds the shortest path when all moves have the same cost.
- Usually uses more memory because it stores many frontier nodes.

DFS:
- Uses a stack (LIFO).
- Explores deeper nodes first.
- Does not guarantee the shortest path.
- Usually uses less memory than BFS.

DLS:
- Uses the DFS strategy with a depth limit.
- Prevents the search from going deeper than the specified limit.
- A smaller depth limit can prevent the algorithm from reaching the goal.
- Increasing the depth limit allows the search to explore deeper paths.

For this grid:
- BFS finds a path of length 6.
- DFS finds a path of length 10.
- DLS with limit 6 can reach the goal because the goal is 6 moves away.
- DLS with limit 10 can explore deeper and finds the 10-move DFS-style path.

Overall, BFS finds the shorter path in this example, while DFS and DLS can find a longer path depending on the order in which nodes are explored.
""")
