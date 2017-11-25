from heapq import heappush, heappop

def bfs(graph, start, goal):
    queue = [[start]]
    visited = set()
    while len(queue) > 0:
        yield 1
        cur = queue[0]
        last = cur[-1]
        graph.display(queue, last, visited)
        if (last == goal):
            return cur
        queue.pop(0)
        for a in graph.get_connected_nodes(last):
            if (a not in cur):
                queue.append(cur + [a])
        visited.add(last)
    return []

def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    while (len(stack) > 0):
        yield 1
        cur = stack.pop()
        last = cur[-1]
        graph.display(stack, last, visited)
        if (last == goal):
            return cur
        for a in graph.get_connected_nodes(last):
            if (a not in cur):
                stack.append(cur + [a])
        visited.add(last)
    return []

def uniform_cost(graph, start, goal):
    heap = []
    heappush(heap, (0, [start], start))
    visited = set()
    while heap:
        yield 1
        cur = heappop(heap)
        last = cur[1][-1]
        graph.display(heap, last, visited)
        if (last == goal):
            return cur[1]
        for a in graph.get_connected_nodes(last):
            if (a not in cur[1]):
                heappush(heap, (cur[0] + graph.get_edge(last, a).length, cur[1] + [a], a))
        visited.add(last)
    return []

def a_star(graph, start, goal):
    graph.diplay_heuristique(goal)
    heap = []
    heappush(heap, (graph.get_heuristic(start, goal), [start], start))
    visited = set()
    while heap:
        yield 1
        cur = heappop(heap)
        last = cur[1][-1]
        graph.display(heap, last, visited)
        if (last == goal):
            return cur[1]
        visited.add(last)
        for a in graph.get_connected_nodes(last):
            if (a not in visited):
                heappush(heap,
                         (cur[0] + graph.get_edge(last, a).length + graph.get_heuristic(a, goal), cur[1] + [a], a))
    return []





# def is_admissible(graph, goal):
#     for a in graph.nodes:
#         d=path_length(graph,branch_and_bound(graph, a, goal))
#         h=graph.get_heuristic(a,goal)
#         if(h>d):
#             return False
#     return True
