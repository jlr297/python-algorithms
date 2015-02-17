import Graph, Graph_Algs as Algs, Truck_Package as TP

truck_one = TP.Truck('Billy', 'F')
truck_two = TP.Truck('Joe', 'F')

package_one = TP.Package('important stuff', 'A', 'E')
package_two = TP.Package('special stuff', 'G', 'B')

nk_problem = TP.State("FFFalseFalse", 'F')

nk_problem.add_truck(truck_one)
nk_problem.add_truck(truck_two)

nk_problem.add_package(package_one)
nk_problem.add_package(package_two)

print "Using h = 0 heuristic:"
print Algs.eh_star(Graph.example, nk_problem, TP.is_goal, Algs.bad_heuristic, TP.transition_func)
print "Using better heuristic:"
print Algs.eh_star(Graph.example, nk_problem, TP.is_goal, Algs.truck_heuristic, TP.transition_func)

quit = input("Press enter to quit")