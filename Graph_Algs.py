# Heuristic search algorithm A*
def a_star(graph, start, is_goal, heuristic, trans):
    closedset = []
    openset = [start]
    came_from = {}
    g_score = {}
    f_score = {}

    g_score[start.label] = 0
    f_score[start.label] = g_score[start.label] + heuristic(graph, start, is_goal)

    count = 0
    while len(openset) > 0:
        count += 1
        current = openset[0]

        for open_state in openset:
            if f_score[open_state.label] < f_score[current.label]:
                current = open_state

        if is_goal(current):
            return (reconstruct_path(came_from, current), g_score[current.label], count)

        openset.remove(current)
        closedset.append(current)

        for neighbor in trans(graph, current):
            skip = False
            for closed_state in closedset:
                if closed_state.label == neighbor[0].label:
                    skip = True
            if skip:
                continue

            temp_g_score = g_score[current.label] + neighbor[1]

            doStuff = True
            for open_state in openset:
                if open_state.label == neighbor[0].label: 
                    doStuff = False
            if (not doStuff) and (temp_g_score < g_score[neighbor[0].label]):
                doStuff = True

            if doStuff:
                came_from[neighbor[0].label] = current
                g_score[neighbor[0].label] = temp_g_score
                f_score[neighbor[0].label] = g_score[neighbor[0].label] + heuristic(graph, neighbor[0], is_goal)
                for open_state in openset:
                    if open_state.label == neighbor[0].label: 
                        doStuff = False
                if doStuff:
                    openset.append(neighbor[0])

# Used with a_star to reconstruct path to the goal node
def reconstruct_path(came_from, current):
    path = [current.label]
    while current.label in came_from.keys():
        current = came_from[current.label]
        path.insert(0,current.label)
    return path

# A simple admissible heuristic. Results in Dijkstra's algorithm
def bad_heuristic(graph, state_A, state_B):
    return 0

# Straight Line Distance between 2 points
def SLD(graph, node_A, node_B):
    return ((graph.verticies[node_A].x - graph.verticies[node_B].x)**2+(graph.verticies[node_A].y - graph.verticies[node_B].y)**2)**.5

# Finds all paths between start and dest nodes in a graph, returns list of paths
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

# Breadth First Search, returns path between start and end node
def bfs(graph, start, end):
    queue = []
    queue.append([start])
    while queue:
        #print queue
        path = queue.pop(0) # For dfs change to -1
        tail = path[-1]
        if tail == end:
            return path
        for edge in graph.edges_out(tail):
            if edge.dest not in path:
                newPath = list(path)
                newPath.append(edge.dest)
                queue.append(newPath)