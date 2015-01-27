def eh_star(graph, start, goal, h):
    closedset = []
    openset = [start]
    came_from = {}
    g_score = {}
    f_score = {}

    g_score[start] = 0
    f_score[start] = g_score[start] + h(graph, start, goal)

    count = 0
    while len(openset) > 0:
        count += 1
        current = openset[0]
        for node in openset:
            if f_score[node] < f_score[current]:
                current = node
        if current == goal:
            return reconstruct_path(came_from, goal)
        
        openset.remove(current)
        closedset.append(current)

        for neighbor in graph.edges_out(current):
            if neighbor.dest in closedset:
                continue
            temp_g_score = g_score[current] + neighbor.weight

            if neighbor.dest not in openset or temp_g_score < g_score[neighbor.dest]:
                came_from[neighbor.dest] = current
                g_score[neighbor.dest] = temp_g_score
                f_score[neighbor.dest] = g_score[neighbor.dest] + h(graph, neighbor.dest, goal)
                if neighbor.dest not in openset:
                    openset.append(neighbor.dest)

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0,current)
    return path

def bad_heuristic(graph, node_A, node_B):
    return 0

def SLD(graph, node_A, node_B):
    return ((graph.verticies[node_A].x - graph.verticies[node_B].x)**2+(graph.verticies[node_A].y - graph.verticies[node_B].y)**2)**.5

def find_paths(graph, start, dest, path=[]):
    path = path + [start]
    if start == dest:
        return [path]
    paths = []
    for edge in graph.edges_out(start):
        if edge.dest not in path:
            newPaths = find_paths(graph, edge.dest, dest, path)
            for newPath in newPaths:
                paths.append(newPath)
    return paths

def bfs(graph, start, end):
    queue = []
    queue.append([start])
    while queue:
        #print queue
        path = queue.pop(0)
        tail = path[-1]
        if tail == end:
            return path
        for edge in graph.edges_out(tail):
            if edge.dest not in path:
                newPath = list(path)
                newPath.append(edge.dest)
                queue.append(newPath)

def dfs(graph, start, end):
    queue = []
    queue.append([start])
    while queue:
        #print queue
        path = queue.pop(-1)
        tail = path[-1]
        if tail == end:
            return path
        for edge in graph.edges_out(tail):
            if edge.dest not in path:
                newPath = list(path)
                newPath.append(edge.dest)
                queue.append(newPath)