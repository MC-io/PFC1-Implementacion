from TNDP import TNDP

class RouteSet:

    def __init__(self):
        self.route_set = []
        self.d = [0, 0, 0]
        self.overall_constraint_violation = 0

    def read_from_string(st):
        rs = RouteSet()

    def size(self):
        return len(self.route_set)
    
    def get_route(self, i):
        return self.route_set[i]
    

    def generate_route_set(self, tndp):
        num_of_routes = tndp.get_number_of_routes()
        feasible = True
        while True:
            self.route_set.clear()
            self.overall_constraint_violation = 0
        
