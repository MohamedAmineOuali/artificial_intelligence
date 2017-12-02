from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Algorithms
import time
import threading
from DataFromFile import *
from Graph import *
NAME = "NAME"
NODE1 = "NODE1"
NODE2 = "NODE2"
VAL = "LENGTH"

class MyThread(threading.Thread):
    def __init__(self, target, *args):
        self.target = target
        self.args = args
        self.pause = False
        self.kill = False
        self.ev = threading.Event()
        super().__init__(target=self.execute)

    '''pause the thread'''
    def pausef(self):
        if (self.pause):
            self.ev.set()
        self.pause = not self.pause

    '''stop the thread'''
    def killf(self):
        self.kill = True

    '''run the thread : resume if paused'''
    def execute(self):
        for i in self.target(*self.args):
            if (self.pause):
                self.ev.wait()
            if (self.kill):
                return

class MyAppAction:
    algo = ["DFS", "BFS", "iterative_deepening", "uniform cost", "Astar"]
    algorithms = [Algorithms.dfs, Algorithms.bfs, Algorithms.iterative_deepening, Algorithms.uniform_cost,
                  Algorithms.a_star]

    '''
    define the selction of the algos, delay, start and finish node
    specify the stop, play, pause , save button and define the methods corresponding to the clicks on the corresponding buttons
    '''
    def __init__(self, algoSelect: QComboBox, delaySelect: QtWidgets.QDoubleSpinBox, startSelect: QComboBox,
                 endSelect: QComboBox, textarea, playbt: QToolButton, stopbt: QToolButton, pausebt: QToolButton,
                 view, saveBt: QAction):
        self.algoSelect = algoSelect
        self.delaySelect = delaySelect
        self.startSelect = startSelect
        self.endSelect = endSelect
        self.textarea = textarea
        self.playbt = playbt
        self.stopbt = stopbt
        self.pausebt = pausebt
        self.view = view
        self.saveBt = saveBt
        self.setAlgorithmList()
        self.setDelaiList()
        self.playbt.clicked.connect(self.play)
        self.pausebt.clicked.connect(self.pause)
        self.stopbt.clicked.connect(self.stop)

    '''define the algos list'''
    def setAlgorithmList(self):
        self.algoSelect.addItems(MyAppAction.algo)

    '''define the delays possibles list'''
    def setDelaiList(self):
        self.delaySelect.setValue(1)

    '''display the updates of the graphs image according the delay sepecified'''
    def display_image(self, img):
        self.view.setPixmap(QtGui.QPixmap(img))
        self.view.show()
        QCoreApplication.processEvents()  # let Qt do his work
        if hasattr(self, 'delay'):
            time.sleep(self.delay)

    '''create the graph and get the data from the files xml or txt'''
    def createGraph(self, name):
        edgesdata=[]
        heurisiticdata=[]
        d = DataFromFile()
        if("txt" in name[1]):
            (edgesdata, heurisiticdata) = d.getDataFromFileTXT(name[0])
        if("xml" in name[1]):
            (edgesdata, heurisiticdata) = d.getDataFromFileXML(name[0])
        self.graph = Graph(display=self.display_image, edgesdict= edgesdata["edgesdict"],
                           heuristic= heurisiticdata["heurisiticdict"][0])
        def cmp_to_key():
            'Convert a cmp= function into a key= function'
            class K(object):
                def __init__(self, obj, *args):
                    self.obj = obj
                def __lt__(self, other):
                    return int(self.obj) < int(other.obj)
            return K
        self.graph.nodes.sort(key=cmp_to_key())
        self.startSelect.addItems(self.graph.nodes)
        self.endSelect.addItems(self.graph.nodes)
        self.endSelect.setCurrentIndex(0)
        self.startSelect.setCurrentIndex(0)
        self.graph.display()
    '''specify the pause methods from the Thread'''
    def pause(self):
        self.t.pausef()

    '''specify the stop methods from the Thread'''
    def stop(self):
        self.t.killf()

    '''specify the play methods from the Thread : initilize the graph, and its params then start the algorithm '''
    def play(self):
        self.graph.init()
        self.curAlgo = MyAppAction.algorithms[self.algoSelect.currentIndex()]
        a = self.startSelect.currentIndex()
        b = self.endSelect.currentIndex()
        self.startNode = self.startSelect.currentText()
        self.goleNode = self.endSelect.currentText()
        self.delay = self.delaySelect.value()
        self.t = MyThread(self.curAlgo, self.graph, self.startNode, self.goleNode)
        self.t.start()
