NAME = "NAME"
NODE1 = "NODE1"
NODE2 = "NODE2"
VAL = "LENGTH"

class Node:
    def __init__(self, NAME, NODE1, NODE2, VAL,*args):
        self.NAME=NAME
        self.NODE1=NODE1
        self.NODE2=NODE2
        self.VAL=VAL

class DataFromFile:

    '''the data to be read from the file is the edges dictionary and the heuristic dictionary'''
    def __init__(self):
        self.edgesdata = {"edgesdict": []}
        self.heurisiticdata = {"heurisiticdict": []}

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
                    edgesdict = {}
                    line = ' '.join(line.replace("\"","\'").replace('{', "").replace('},', "").split())
                    params = line.replace('\'','').split(",")
                    name = params[0].split(": ")[1]
                    val = params[1].replace('\'','').split(": ")[1]
                    node1 = params[2].split(": ")[1]
                    node2 = params[3].split(": ")[1]
                    edgesdict[NAME] = name
                    edgesdict[VAL] = int(val)
                    edgesdict[NODE1] = node1
                    edgesdict[NODE2] = node2
                    self.edgesdata["edgesdict"].append(edgesdict)
                #get the heuristic dictionary
                else :
                    arguments = {}
                    line = ' '.join(line.replace("\"","\'").replace(' ', "").replace("},","}").split())
                    line = line.split(":{")
                    #endPoint indicates that this heuristic only works if the endPoint of the algo is that and that the start is 1
                    endPoint = line[0].replace("{","").replace("'","")
                    arguments = line[1].replace("}","").split(",")
                    heurisitics = {}
                    if(len(arguments)>0 and arguments[0]!=""):
                        for argument in arguments:
                            argument=argument.split(":")
                            #the heurisitic of each node must be an int
                            heurisitics[argument[0].replace("'","")] = int(argument[1])
                    heuristicdict={}
                    heuristicdict[endPoint] = heurisitics
                    self.heurisiticdata["heurisiticdict"].append(heuristicdict)
        print(self.edgesdata,self.heurisiticdata)
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
                foundit = True
                if(foundit):
                    for params in child:
                        for param in params:
                            if(param.tag=="endPoint"):
                                endPoint=param.attrib["node"]
                            else:
                                heurisitics[param.attrib["node"]] = int(param.attrib["value"])
                heuristicdict = {}
                heuristicdict[endPoint] = heurisitics
                self.heurisiticdata["heurisiticdict"].append(heuristicdict)
            if(child.tag=="edgesdict"):
                edgesdict = {}
                for edge in child:
                    edges = {}
                    edges[NAME] = edge.attrib['name']
                    edges[VAL] = int(edge.attrib['val'])
                    edges[NODE1] = edge.attrib['node1']
                    edges[NODE2] = edge.attrib['node2']
                    self.edgesdata["edgesdict"].append(edges)
        print(self.heurisiticdata["heurisiticdict"][0])
        print(self.edgesdata["edgesdict"])
        return (self.edgesdata,self.heurisiticdata)

d = DataFromFile()
d.getDataFromFileTXT("./DATA/graph8")