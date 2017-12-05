from heapq import heappush, heappop


def bfs(graph, start, goal):
    queue = [[start]]
    visited = set()
    path=[]
    while len(queue) > 0:
        yield 1
        cur = queue[0]
        last = cur[-1]
        graph.display(queue, last, visited)
        path.append(last)
        if last == goal:
            return (cur,path,path_length(graph,cur))
        queue.pop(0)
        for a in graph.get_connected_nodes(last):
            if a not in visited:
                queue.append(cur + [a])
        visited.add(last)
    return ([],path,0)

def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    path=[]
    while len(stack) > 0:
        yield 1
        cur = stack.pop()
        last = cur[-1]
        graph.display(stack, last, visited)
        path.append(last)
        if (last == goal):
            return (cur,path,path_length(graph,cur))
        for a in graph.get_connected_nodes(last):
            if (a not in visited):
                stack.append(cur + [a])
        visited.add(last)
    return ([],path,0)

def uniform_cost(graph, start, goal):
    heap = []
    heappush(heap, (0, [start], start))
    visited = set()
    path=[]
    while heap:
        yield 1
        cur = heappop(heap)
        last = cur[1][-1]
        graph.display(heap, last, visited)
        path.append(last)
        if (last == goal):
            return (cur[1],path,path_length(graph,cur[1]))
        for a in graph.get_connected_nodes(last):
            if (a not in visited):
                heappush(heap, (cur[0] + graph.get_edge(last, a).length, cur[1] + [a], a))
        visited.add(last)
    return ([],path,0)

def a_star(graph, start, goal):
    graph.diplay_heuristique(goal)
    heap = []
    heappush(heap, (graph.get_heuristic(start, goal), [start], start))
    visited = set()
    path=[]
    while heap:
        yield 1
        cur = heappop(heap)
        last = cur[1][-1]
        graph.display(heap, last, visited)
        path.append(last)
        if (last == goal):
            return (cur[1],path,path_length(graph,cur[1]))
        visited.add(last)
        for a in graph.get_connected_nodes(last):
            if a not in visited:
                heappush(heap,
                         (cur[0] + graph.get_edge(last, a).length + graph.get_heuristic(a, goal), cur[1] + [a], a))
    return ([],path,0)

def iterative_deepening(graph, start, goal):
    level=0
    path=[]
    while 1:
        level+=1
        stack = [(1,[start],start)]
        visited = set()
        isNextLevel=False
        while stack:
            yield 1
            cur = stack.pop()
            last = cur[1][-1]
            graph.display(stack, last, visited)
            path.append(last)
            if last == goal:
                return (cur,path,path_length(graph,cur))
            if cur[0]<level:
                for a in graph.get_connected_nodes(last):
                    if a not in visited:
                        stack.append((cur[0]+1,cur[1] + [a],a))
            else:
                isNextLevel=True
            visited.add(last)
        if not (isNextLevel):
            break
    return ([],path,0)

def best_first(graph, start, goal):
    graph.diplay_heuristique(goal)
    heap = []
    heappush(heap, (graph.get_heuristic(start, goal), [start], start))
    visited = set()
    path=[]
    while heap:
        yield 1
        cur = heappop(heap)
        last = cur[1][-1]
        graph.display(heap, last, visited)
        path.append(last)
        if (last == goal):
            return (cur[1],path,path_length(graph,cur[1]))
        visited.add(last)
        for a in graph.get_connected_nodes(last):
            if a not in visited:
                heappush(heap,
                         (graph.get_heuristic(a, goal), cur[1] + [a], a))
    return ([],path,0)

def iterative_a_star(graph, start, goal):
    graph.diplay_heuristique(goal)
    level=0
    path=[]
    while 1:
        level+=1
        heap = []
        heappush(heap, (graph.get_heuristic(start, goal), [start], start))
        visited = set()
        isNextLevel=False
        while heap:
            yield 1
            cur = heappop(heap)
            last = cur[1][-1]
            graph.display(heap, last, visited)
            path.append(last)
            if (last == goal):
                return (cur[1], path, path_length(graph, cur[1]))
            if len(cur[1])<level:
                for a in graph.get_connected_nodes(last):
                    if a not in visited:
                        heappush(heap,
                                 (cur[0] + graph.get_edge(last, a).length + graph.get_heuristic(a, goal), cur[1] + [a],a))
            else:
                isNextLevel=True
            visited.add(last)
        if not (isNextLevel):
            break
    return ([],path,0)

def path_length(graph, node_names):
    length=0
    for i in range(len(node_names)-1):
        length+=graph.get_edge(node_names[i],node_names[i+1]).length
    return length

# def is_admissible(graph, goal):
#     for a in graph.nodes:
#         d=path_length(graph,branch_and_bound(graph, a, goal))
#         h=graph.get_heuristic(a,goal)
#         if(h>d):
#             return False
#     return True
