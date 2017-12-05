import graphviz


class Edge:
    '''an Edge is defined by its name, length and the nodes it connects'''
    def __init__(self, name, node1, node2, length):
        self.name = name
        self.node1 = node1
        self.node2 = node2
        self.length = length

    '''String representation of an Edge : Edge 'name' from 'node1' to 'node2' with length 'length'''
    def __repr__(self):
        return 'Edge ' + self.name + \
               ' from ' + self.node1 + ' to ' + self.node2 + \
               ' with length ' + str(self.length)

class IGraph:
    '''
    init the edges, nodes and heuristics
    specify either edgesdict OR edges
    verify the Keyerror of the edgesdict
    heuristic is a dictionary where heuristic[G][S] is the heuristic distance from S to G
    call the validate to verify the parameters
    '''
    def __init__(self, nodes=None, edgesdict=None, heuristic=None, edges=None):
        '''specify EITHER edgesdict OR edges'''
        if edges:
            self.edges = edges
        elif edgesdict:
            try:
                self.edges = [Edge(e['NAME'], e['NODE1'], e['NODE2'], e['LENGTH']) for e in edgesdict]
            except KeyError:
                self.edges = [Edge(e['name'], e['node1'], e['node2'], e['length']) for e in edgesdict]
        else:
            self.edges = []
        self.nodes = nodes
        if not nodes:
            self.nodes = list(set([edge.node1 for edge in self.edges] +
                                  [edge.node2 for edge in self.edges]))
        '''heuristic is a dictionary where heuristic[G][S] is the heuristic distance from S to G'''
        self.heuristic = heuristic
        if not heuristic:
            self.heuristic = {}
        self.validate()

    '''test the none duplication and the validation of the edges and the nodes'''
    def validate(self):
        for name in self.nodes:
            assert isinstance(name, str), str(type(name)) + ": " + str(name)
        assert len(self.nodes) == len(set(self.nodes)), "no duplicate nodes"
        edgenames = [edge.name for edge in self.edges]
        assert len(edgenames) == len(set(edgenames)), "no duplicate edges"
        for edge in self.edges:
            assert isinstance(edge.name, str), type(edge.name)
            assert edge.node1 in self.nodes
            assert edge.node2 in self.nodes
            assert edge.length > 0, "positive edges only today"
        for start in self.nodes:
            for end in self.nodes:
                assert self.get_heuristic(start, end) >= 0

    """
    gets a list of all node id values connected to a given node.
    'node' should be a node name, not a dictionary.
    The return value is a list of node names.
    """
    def get_connected_nodes(self, node):
        assert node in self.nodes, "No node " + str(node) + " in graph " + str(self)
        result = [x.node2 for x in self.edges if x.node1 == node]
        # result += [x.node1 for x in self.edges if x.node2 == node]
        return sorted(result)

    """
    checks the list of edges and returns an edge if
    both connected nodes are part of the edge, or 'None' otherwise.
    'node1' and 'node2' are names of nodes, not 'NODE' dictionaries.
    """
    def get_edge(self, node1, node2):
        assert node1 in self.nodes, "No node " + str(node1) + " in graph " + str(self)
        assert node2 in self.nodes, "No node " + str(node2) + " in graph " + str(self)
        node_names = (node1, node2)
        for edge in self.edges:
            if ((edge.node1, edge.node2) == node_names or
                        (edge.node2, edge.node1) == node_names):
                return edge
        return None

    """
    checks if two edges are connected.
    'node1' and 'node2' are names of nodes, not 'NODE' dictionaries.
    """
    def are_connected(self, node1, node2):
        return bool(self.get_edge(node1, node2))

    """ Return the value of the heuristic from the start to the goal"""
    def get_heuristic(self, start, goal):
        assert start in self.nodes, "No node " + str(start) + " in graph " + str(self)
        assert goal in self.nodes, "No node " + str(goal) + " in graph " + str(self)
        if goal in self.heuristic:
            if start in self.heuristic[goal]:
                return self.heuristic[goal][start]
            else:
                return 0  # we have checked that everything is positive
        else:
            return 0  # we have checked that everything is positive

    def add_edge(self, node1, node2, length, name=None):
        if node1 not in self.nodes:
            self.nodes.append(node1)
        if node2 not in self.nodes:
            self.nodes.append(node2)
        if name == None:
            name = ("%s %s" % (node1, node2))
        self.edges.append(Edge(name, node1, node2, length))

    def set_heuristic(self, start, goal, value):
        if goal not in self.heuristic:
            self.heuristic[goal] = {}
        self.heuristic[goal][start] = value

    '''
    the string representation of the graph: 
    Graph:
    edges= "edges"
    heuristic= "heuristic
    '''
    def __str__(self):
        return "Graph: \n  edges=" + str(self.edges) + "\n  heuristic=" + str(self.heuristic)

class Graph(IGraph):
    '''
    call the init of the IGraph class to initilize the params(edges, nodes, heurisitics)
    create an empty graph as an image "test.png" (we used graphviz library)
    set the edges and the nodes on the graph
    '''
    def __init__(self, display,*args, **kwargs):
        super().__init__(*args, **kwargs)
        '''create an empty graph'''
        self.display_image = display
        self.g = graphviz.Digraph(filename="test",format="png")
        self.g.attr(size='10')
        self.g.attr(rankdir='LR')
        for v in self.nodes:
            self.g.node(v)
        for edge in self.edges:
            self.g.edge(edge.node1, edge.node2, label=str(edge.length))


    '''
    display the heuristic on the graph, you need just to specify the goal node
    '''
    def diplay_heuristique(self,goal):
        for node in self.nodes:
            self.g.node(node, label=node+' h*=('+str(self.get_heuristic(node,goal))+')')

    '''
    color of the nodes in : 
        fringe :lightblue2,
        explored : red,
        current : blue,
        start : pink,
        goal : green
    render the text.png image accrodingly and diplay it
    '''
    def display(self, fringe=[],cur=None,explored=[],start=None,goal=None):
        self.init()
        for vertex in fringe:
            self.g.node(vertex[-1], color='lightblue2', style='filled')
        for vertex in explored:
            self.g.node(vertex, color='red', style='filled')
        if cur!=None:
            self.g.node(cur, color='blue', style='filled')
        if start!=None:
            self.g.node(start, color='pink', style='filled')
        if goal!=None:
            self.g.node(cur, color='green', style='filled')
        self.g.render(filename="test")
        self.display_image("test.png")

    '''initilize the vertexes with a blank color'''
    def init(self):
        for vertex in self.nodes:
            self.g.node(vertex, color='', style='')


