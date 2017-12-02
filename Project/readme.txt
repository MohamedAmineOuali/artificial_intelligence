Algorithms:
    contains the implementations of the different algorithms:
        def bfs(graph, start, goal)
        def dfs(graph, start, goal)
        def uniform_cost(graph, start, goal)
        def a_star(graph, start, goal)
        def iterative_deepening(graph, start, goal)
Graph:
    class Edge:
        an edge is defined by this properties: name, node1, node2, length
    class IGraph:
        initilize the edges, nodes and the heuristics (heuristic is a dictionary where heuristic[G][S] is the heuristic distance from S to G)
        def validate(self): test the none duplication and the validation of the edges and the nodes.
        def get_connected_nodes(self, node): gets a list of all node id values connected to a given node name.
        def get_edge(self, node1, node2): returns an edge if both connected nodes are part of the edge, or 'None' otherwise.
        def are_connected(self, node1, node2): checks if two edges are connected.
        def get_heuristic(self, start, goal):Return the value of the heuristic from the start to the goal
        def add_edge(self, node1, node2, length, name=None): add an edge to the graph
        def set_heuristic(self, start, goal, value): set the heuristic value for a start - goal
    class Graph:
        initilize the params : edges, nodes , heurisitic by calling the IGraph methods; initilize the Graph and display it
        def diplay_heuristique(self,goal): display the heuristic on the graph
        def display(self, fringe=[],cur=None,explored=[],start=None,goal=None): sepcify the color of the graph
            (fringe :lightblue2, explored : red, current : blue, start : pink, goal : green) and update the graph image
AppGUI:
MyAppAction:
    class Thread:
        define the thread pause, stop and resume methods
    class MyAppAction:
        define the selection of the algos, delay, start and finish node
        specify the stop, play, pause , save button and define the methods corresponding to the clicks on the corresponding buttons
        def setAlgorithmList(self): define the algos list
        def setDelaiList(self): define the delays possibles list
        def display_image(self, img): display the updates of the graphs image according the delay sepecified
        def createGraph(self, name): create the graph and get the data from the files xml or txt
        def pause(self): specify the pause methods from the Thread
        def stop(self): specify the stop methods from the Thread
        def play(self): specify the play methods from the Thread : initilize the graph, and its params then start the algorithm
DataFromFile:
    read the data from the xml or txt file:

        def getDataFromFileTXT(self,filename):
            read the data from a text file : structure of the file should be:
            ______________________________________________
            |edgesdict=                                    |
            |{NAME: '!', VAL: ! , NODE1: '!', NODE2: '!'}, |
            |....                                          |
            |heuristic=                                    |
            |{'goal': { 'node': int, ... } }               |
            |______________________________________________|

        def getDataFromFileXML(self,filename):
            read the data from a xml file : structure of the file should be:
            _______________________________________________________
            |<graph>                                              |
            |   <edgesdict>                                       |
            |       <edge name="e1" val="5" node1="1" node2="2"/> |
            |           ...                                       |
            |   </edgesdict>                                      |
            |   <heuristic>                                       |
            |       <params>                                      |
            |           <endPoint node="14"></endPoint>           |
            |           <param node="4" value="17"></param>       |
            |_____________________________________________________|
