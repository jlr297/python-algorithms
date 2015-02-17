class Truck():
    def __init__(self, label, location):
        self.label = label
        self.package = None
        self.location = location

    def set_location(self, location):
        self.location = location

    def get_neighbors(self, graph):
        return graph.edges_out(self.location)

    def has_package(self):
        if(self.package):
            return True
        else:
            return False

class Package():
    def __init__(self, label, location, dest):
        self.label = label
        self.location = location
        self.dest = dest

    def delivered(self):
        return location == dest

class State():
    def __init__(self, label, garage):
        self.label = label
        self.garage = garage
        self.trucks = []
        self.packages = []

    def add_package(self, package):
        self.packages.append(package)

    def get_packages(self, packages):
        return self.packages

    def add_truck(self, truck):
        self.trucks.append(truck)

    def get_trucks(self,trucks):
        return self.trucks

# Transition function, finds all neighbor States for each truck
def transition_func(graph, state):
    states = []
    for neighbor1 in state.trucks[0].get_neighbors(graph):
        for neighbor2 in state.trucks[1].get_neighbors(graph):
            temp = State("", state.garage)
            for index in range(0, len(state.packages)):
                temp.add_package(Package(state.packages[index].label, state.packages[index].location, state.packages[index].dest))
            for index in range(0, len(state.trucks)):
                temp.add_truck(Truck(state.trucks[index].label, state.trucks[index].location))

            if temp.packages[0].location == temp.trucks[0].location:
                if temp.packages[0].location != temp.packages[0].dest:
                    temp.trucks[0].package = temp.packages[0]
                else:
                    temp.trucks[0].package = None
            if temp.trucks[0].has_package():
                temp.trucks[0].location = neighbor1.dest
                temp.packages[0].location = neighbor1.dest
            else:
                if not(temp.packages[0].location == temp.packages[0].dest and temp.trucks[0].location == temp.garage):
                    temp.trucks[0].location = neighbor1.dest

            if temp.packages[1].location == temp.trucks[1].location:
                if temp.packages[1].location != temp.packages[1].dest:
                    temp.trucks[1].package = temp.packages[1]
                else:
                    temp.trucks[1].package = None
            if temp.trucks[1].has_package():
                temp.trucks[1].location = neighbor2.dest
                temp.packages[1].location = neighbor2.dest
            else:
                if not(temp.packages[1].location == temp.packages[1].dest and temp.trucks[1].location == temp.garage):
                    temp.trucks[1].location = neighbor2.dest

            temp.label = temp.trucks[0].location + temp.trucks[1].location
            temp.label+= str(temp.packages[0].location == temp.packages[0].dest)
            temp.label+= str(temp.packages[1].location == temp.packages[1].dest)
            
            states.append((temp, neighbor1.weight + neighbor2.weight))
    return states

# Simple function to check if the problem is solved
def is_goal(state):
    for package in state.packages:
        if package.location != package.dest:
            return False
    for truck in state.trucks:
        if truck.location != state.garage:
            return False
    return True