class Edge:
    def __init__(self, id_a:int, id_b:int, cost):
        self.verts = [id_a, id_b]
        self.cost = cost

    def display(self):
        print(self.verts[0], ' - ', self.verts[1], ' : ', self.cost)

    






# INTERNAL / EXTERNAL LAUNCH
if __name__ == '__main__':
    
    print('===============================')
    print('=== edge.py - DIRECT LAUNCH ===')
    print('===============================')

else:
    print('edge.py - EXTERNAL IMPORT')