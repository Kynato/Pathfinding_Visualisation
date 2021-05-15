from point import Point
from edge import Edge
from vert import Vert

# CONSTANTS
STRAIGHT_COST = 1
ANGLE_COST = STRAIGHT_COST*pow(2, 1/2)

class Graph:
    def __init__(self, height:int, width:int):

        # Grid size
        self.width = width
        self.height = height

        # Default path
        self.start = Point(0, 0)
        self.finish = Point(width-1, height-1)

        # Create grid of verts
        self.grid = create_grid(height, width)

        # Create a set of all the edges
        self.edges = create_edges(height, width, self)

        # Calculate the Euclidean Distances for each vert from finish vert
        self.recalculate_euclidean_distances()


    # Update whole grid with new euclidean distances
    # Use when changing finishing point
    def recalculate_euclidean_distances(self):
        for row in range(self.height):
            for col in range(self.width):
                self.grid[row][col].calculate_distance_from_point(self.finish)
        
    # Set point that begins our jurney
    def set_start(self, row:int, col:int):
        self.start = Point(col, row)

    # Set point that is searched, also updates the eucl_distances
    def set_finish(self, row:int, col:int):
        self.finish = Point(col, row)
        self.recalculate_euclidean_distances()

    # Returns ID of the vert  
    def get_vert_id(self, col:int, row:int):
        return self.grid[row][col].id  

    # Prints out helpful troubleshooting info
    def display(self):

        # Prints out a grid of VERT_IDs
        print('ID_GRID:')
        for row in range(self.height):
            for col in range(self.width):
                print(self.grid[row][col].id, end=' ')
            print('')

        # Prints out a list of edges and their costs
        if True:
            print('EDGES:')
            for edge in self.edges:
                edge.display()
        

        # Prints out the grade of the verticie
        print('EDGE_DENSITY:')
        for id in range(self.width*self.height):
            ctr = 0
            for edge in self.edges:
                if id in edge.verts:
                    ctr = ctr+1
            if id%self.width == self.width-1:
                print(ctr)
            else:
                print(ctr, end=' ')

        # Prints out the euclidean distance from each vert to finish
        print('EUCLIDEAN_DISTANCES:')
        for row in range(self.height):
            for col in range(self.width):
                print(round(self.grid[row][col].euclidean_cost, 1), end=' ')
            print('')

        


# ELEGANCY FUNCTIONS

# Creates a grid filled with Verts
def create_grid(h:int, w:int):
    ctr = 0
    grid = []
    for i in range(h):
        line = []
        for j in range(w):
            line.append(Vert(ctr, j, i))
            ctr = ctr+1
        grid.append(line)
    return grid
# Creates a set of edges
def create_edges(h:int, w:int, graph:Graph):
    stack = []
    for row in range(h):
        for col in range(w):
            current_vert = graph.get_vert_id(col, row)
            # Now create edge for every direction if possible
            # and add it to the stack
            #   NW  N   NE
            #   W   X   E
            #   SW  S   SE

            # N
            if row-1 >= 0:
                stack.append(Edge(current_vert, graph.get_vert_id(col, row-1), STRAIGHT_COST))
            # S
            if row+1 < h:
                stack.append(Edge(current_vert, graph.get_vert_id(col, row+1), STRAIGHT_COST))
            # W
            if col-1 >= 0:
                stack.append(Edge(current_vert, graph.get_vert_id(col-1, row), STRAIGHT_COST))
            # E
            if col+1 < w:
                stack.append(Edge(current_vert, graph.get_vert_id(col+1, row), STRAIGHT_COST))

            # NE
            if row-1 >= 0 and col+1 < w:
                stack.append(Edge(current_vert, graph.get_vert_id(col+1, row-1), ANGLE_COST))
            # SE
            if row+1 < h and col+1 < w:
                stack.append(Edge(current_vert, graph.get_vert_id(col+1, row+1), ANGLE_COST))
            # SW
            if col-1 >= 0 and row+1 < h:
                stack.append(Edge(current_vert, graph.get_vert_id(col-1, row+1), ANGLE_COST))
            # NW
            if col-1 >= 0 and row-1 >= 0:
                stack.append(Edge(current_vert, graph.get_vert_id(col-1, row-1), ANGLE_COST))

    # Clear duplicates from the stack
    # Now every edge is doubled but symetrically mirrored

    for org in stack:
        # Helper vars
        id_1 = org.verts[0]
        id_2 = org.verts[1]
        e_id = org.id

        # Search for duplicates
        for dupe in stack:
            # If not the same as org
            if dupe.id is not e_id:
                # And if the verts are the same
                if id_1 in dupe.verts and id_2 in dupe.verts:
                    stack.remove(dupe)  # Drop from stack
            
    # well it is not a stack really xd 

    return set(stack)
            





# INTERNAL / EXTERNAL LAUNCH
if __name__ == '__main__':
    
    print('================================')
    print('=== graph.py - DIRECT LAUNCH ===')
    print('================================')

    g = Graph(3, 3)
    g.display()

else:
    print('graph.py - EXTERNAL IMPORT')