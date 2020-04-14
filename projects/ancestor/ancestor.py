from util import Stack, Queue

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("ERROR: vertex does not exist")

    def add_undirected_edge(self, v1, v2):
        """
        Add a undirected edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            print("ERROR: vertex does not exist")        

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print("ERROR: vertex does not exist")   

def earliest_ancestor(ancestors, starting_node):
    
    graph = Graph()

    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_vertex(9)
    graph.add_vertex(10)
    graph.add_vertex(11)
    graph.add_edge(6, 3)
    graph.add_edge(6, 5)
    graph.add_edge(3, 1)
    graph.add_edge(3, 2)
    graph.add_edge(1, 10)
    graph.add_edge(7, 5)
    graph.add_edge(9, 8)
    graph.add_edge(5, 4)
    graph.add_edge(8, 4)
    graph.add_edge(8, 11)
    
    # Create a queue
    q = Queue()
    # Enqueue the starting vertex
    q.enqueue(starting_node)
    # Create a set to store visited vertices
    visited = set()
    # While the queue is not empty
    while q.size() > 0:
        # Dequeue the first vertex
        v = q.dequeue()
        # Check if it's been visited
        # If it hasn't been visted
        if v not in visited:
            # Mark it as visited
            visited.add(v)
            
            # Enqueue all it's neighbors
            for neighbor in graph.get_neighbors(v):
                q.enqueue(neighbor)
            if neighbor not in graph.get_neighbors(v):  
                print(v)   
                
earliest_ancestor(None,6)               