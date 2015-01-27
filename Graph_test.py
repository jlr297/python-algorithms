import Graph
import Graph_Algs as algs

'''
G = Graph.G
print G.toString()

print algs.find_paths(G,'A','F')
print algs.bfs(G,'A','F')
#print algs.dfs(G,'A','F')

print algs.eh_star(G, 'A', 'F', algs.shitty_heuristic)
'''

F = Graph.F
#print F.toString()

#print algs.find_paths(F,'A','D')
#print algs.bfs(F,'A','D')
#print algs.dfs(G,'A','F')

print algs.eh_star(F, 'A', 'D', algs.bad_heuristic)
print algs.eh_star(F, 'A', 'D', algs.SLD)
