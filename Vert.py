from point import Point

class Vert:
    def __init__(self, id:int, x:int, y:int):
        
        # ID
        self.id = id

        # COORDINATES
        self.coords = Point(x, y)

        # COSTS
        self.euclidean_cost = 0
        self.current_cost = 0
        self.total_cost = 0

        # IS WALL
        self.active = True

        # Vert leading to THIS one
        self.prev_vert = None

    # Used to define the distance between 2 points
    def calculate_distance_from_point(self, p:Point):
        horizontal_edge = abs(self.coords.x - p.x)
        vertical_edge = abs(self.coords.y - p.y)
        
        euclidean_distance = pow( pow(horizontal_edge, 2)+pow(vertical_edge, 2), 1/2)
        self.euclidean_cost = euclidean_distance

    # Build/Destroy the wall
    def toggle_activity(self):
        self.active = not self.active

    # Set/Update vert leading to THIS one
    def set_previous_vert(self, prev_vert_id:int):
        self.prev_vert = prev_vert_id

    # Recalculate total cost
    def recalculate_total_cost(self):
        self.total_cost = self.current_cost + self.euclidean_cost



# INTERNAL / EXTERNAL LAUNCH
if __name__ == '__main__':
    
    print('===============================')
    print('=== vert.py - DIRECT LAUNCH ===')
    print('===============================')

    # CHECK THE EUC. CALCULATIONS
    p = Vert(0, 1, 1)
    p.calculate_distance_from_point(Point(4,5))
    if p.euclidean_cost != 5.0:
        print("ERROR. EUCLIDEAN DISTANCE MISCALCULATION.")
        exit
else:
    print('vert.py - EXTERNAL IMPORT')