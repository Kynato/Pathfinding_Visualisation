from typing import Counter


class Edge:
    count = 0
    def __init__(self, id_a:int, id_b:int, cost):
        self.verts = [id_a, id_b]
        self.cost = cost
        self.visited = False

        self.id = Edge.count
        Edge.count += 1

    # Prints the id_1 - id_2 - cost
    def display(self):
        print(self.verts[0], ' - ', self.verts[1], ' : ', round(self.cost, 2), ' | id: ', self.id)

    






# INTERNAL / EXTERNAL LAUNCH
if __name__ == '__main__':
    
    print('===============================')
    print('=== edge.py - DIRECT LAUNCH ===')
    print('===============================')

else:
    print('edge.py - EXTERNAL IMPORT')