NAME = "NAME"
NODE1 = "NODE1"
NODE2 = "NODE2"
VAL = "LENGTH"
import ast
class Node:
    def __init__(self, NAME, NODE1, NODE2, VAL,*args):
        self.NAME=NAME
        self.NODE1=NODE1
        self.NODE2=NODE2
        self.VAL=VAL

class DataFromFile:

    '''the data to be read from the file is the edges dictionary and the heuristic dictionary'''
    def __init__(self):
        self.edgesdata = []
        self.heurisiticdata = []

    ''' 
    read the data from a text file : structure of the file should be:
        ______________________________________________
        |edgesdict=                                    |
        |{NAME: '!', VAL: ! , NODE1: '!', NODE2: '!'}, |
        |....                                          |
        |heuristic=                                    | 
        |{'goal': { 'node': int, ... } }               |
        |______________________________________________|
    
    '''
    def getDataFromFileTXT(self,filename):
        self.filename = filename
        with open(self.filename,'r') as file:
            foundit = False
            heuristic=''
            for line in file:
                #skip the line that indicates it is the start of the edges dictionary
                if "edgesdict" in line:
                    continue
                #skip the line that indicates it is the start of the heuristic dictionary
                #foundit is to indicate that we are treating the heurisitic part of the file
                if "heuristic" in line:
                    foundit = True
                    continue
                #get the edges dictinary
                if (foundit == False) :
                    edgesdict=ast.literal_eval(line )
                    self.edgesdata.append(edgesdict)
                #get the heuristic dictionary
                else :
                    heuristic+=line

            if(foundit):
                self.heurisiticdata = ast.literal_eval(heuristic)

        return (self.edgesdata,self.heurisiticdata)

    ''' 
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

    '''
    def getDataFromFileXML(self,filename):
        self.filename = filename
        foundit=False
        import xml.etree.ElementTree as ET
        tree = ET.parse(filename)
        root = tree.getroot()
        for child in root:
            if(child.tag == "heuristic"):
                heurisitics = {}
                heuristicdict = {}
                foundit = True
                if(foundit):
                    for params in child:
                        for param in params:
                            endPoint = param.attrib["node"]
                            for i in param:
                                heurisitics[i.attrib["node"]] = int(i.attrib["value"])
                            heuristicdict[endPoint] = heurisitics
                self.heurisiticdata=heuristicdict
            if(child.tag=="edgesdict"):
                edgesdict = {}
                for edge in child:
                    edges = {}
                    edges[NAME] = edge.attrib['name']
                    edges[VAL] = int(edge.attrib['val'])
                    edges[NODE1] = edge.attrib['node1']
                    edges[NODE2] = edge.attrib['node2']
                    self.edgesdata.append(edges)

        return (self.edgesdata,self.heurisiticdata)
