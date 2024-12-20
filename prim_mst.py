import heapq

def prim_mst(graph):
    start_node = 0
    visited = set()
    min_heap = [(0, start_node)]
    mst_cost = 0

    while min_heap:
        weight, current = heapq.heappop(min_heap)
        if current in visited:
            continue
        visited.add(current)
        mst_cost += weight

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (cost, neighbor))

    return mst_cost

graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}

print("Minimum Cost of MST:", prim_mst(graph))
