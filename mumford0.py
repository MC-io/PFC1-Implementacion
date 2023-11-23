class Edge:
    def __init__(self, value, to):
        self.value = value
        self.to = to
        
class Graph:
    def __init__(self, size):
        self.nodes = []
        for _ in range(size):
            self.nodes.append([])


if __name__ == "__main__":

    mandl_network = Graph(15)
    mandl_network.nodes[0] = [Edge(8,1)]
    mandl_network.nodes[1] = [Edge(8,0), Edge(2,2), Edge(3,3), Edge(6,4)]
    mandl_network.nodes[2] = [Edge(2,1), Edge(3,5)]
    mandl_network.nodes[3] = [Edge(3,1), Edge(4,4), Edge(4,5), Edge(10,11)]
    mandl_network.nodes[4] = [Edge(6,1), Edge(4,3)]
    mandl_network.nodes[5] = [Edge(3,2), Edge(4,3), Edge(2,7), Edge(3,14)]
    mandl_network.nodes[6] = [Edge(7,9), Edge(2,14)]
    mandl_network.nodes[7] = [Edge(2,5), Edge(8,9), Edge(2,14)]
    mandl_network.nodes[8] = [Edge(8,14)]
    mandl_network.nodes[9] = [Edge(7,6), Edge(8,7), Edge(5,10), Edge(10,12), Edge(8,13)]
    mandl_network.nodes[10] = [Edge(5,9), Edge(10,11), Edge(5,12)]
    mandl_network.nodes[11] = [Edge(10,3), Edge(10,10)]
    mandl_network.nodes[12] = [Edge(10,9), Edge(5,10), Edge(2,13)]
    mandl_network.nodes[13] = [Edge(8,9), Edge(2,12)]
    mandl_network.nodes[14] = [Edge(3,5), Edge(2,6), Edge(2,7), Edge(8,8)]

    mandl_demand_matrix = [[  0,400,200, 60, 80,150, 75, 75, 30,160, 30, 25, 35,  0,  0],
                           [400,  0, 50,120, 20,180, 90, 90, 15,130, 20, 10, 10,  5,  0],
                           [200, 50,  0, 40, 60,180, 90, 90, 15, 45, 20, 10, 10,  5,  0],
                           [ 60,120, 40,  0, 50,100, 50, 50, 15,240, 40, 25, 10,  5,  0],
                           [ 80, 20, 60, 50,  0, 50, 25, 25, 10,120, 20, 15,  5,  0,  0],
                           [150,180,180,100, 50,  0,100,100, 30,880, 60, 15, 15, 10,  0]
                           [ 75, 90, 90, 50, 25,100,  0, 50, 15,440, 35, 10, 10,  5,  0],
                           [ 75, 90, 90, 50, 25,100, 50,  0, 15,440, 35, 10, 10,  5,  0],
                           [ 30, 15, 15, 15, 10, 30, 15, 15,  0,140, 20,  5,  0,  0,  0],
                           [160,130, 45,240,120,880,440,440,140,  0,600,250,500,200,  0],
                           [ 30, 20, 20, 40, 20, 60, 35, 35, 20,600,  0, 75, 95, 15,  0],
                           [ 25, 10, 10, 25, 15, 15, 10, 10,  5,250, 75,  0, 70,  0,  0],
                           [ 35, 10, 10, 10,  5, 15, 10, 10,  0,500, 95, 70,  0, 45,  0],
                           [  0,  5,  5,  5,  0, 10,  5,  5,  0,200, 15,  0, 45,  0,  0],
                           [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]













