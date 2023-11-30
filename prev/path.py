from segment import Segment

class Path:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.seg_list = []
        self.name = ""
        
    def get_num_of_segment(self):
        return len(self.seg_list)
    
    def need_transfer(self):
        return self.get_num_of_segment() > 1
    
    def set_total_in_vehicle_time(self, total_in_vehicle_time):
        self.total_in_vehicle_time = total_in_vehicle_time

    def set_total_in_vehicle_time_congested(self, t):
        self.total_in_vehicle_time_congested = t

    def add_segment(self, r, s, e):
        self.seg_list.append(Segment(r, s, e))

    def get_route_of_seg(self, i):
        return self.seg_list[i].route_id
    
    def get_route_and_end_of_seg(self, i):
        return str(self.seg_list[i].route_id) + str(self.seg_list[i].end_node)
    
    def set_name(self, s):
        self.name = s
    



