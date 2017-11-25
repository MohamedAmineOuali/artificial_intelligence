from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import Image
from PIL.ImageQt import ImageQt
import Algorithms
import time
import threading

NAME="NAME"
NODE1="NODE1"
NODE2="NODE2"
VAL="LENGTH"
from Graph import  *


class MyThread(threading.Thread):
    def __init__(self, target ,*args):
        self.target=target
        self.args=args
        self.pause=False
        self.kill=False
        self.ev=threading.Event()
        super().__init__(target=self.execute )

    def pausef(self):
        if(self.pause):
            self.ev.set()
        self.pause=not self.pause

    def killf(self):
        self.kill=True

    def execute(self):
        for i in self.target(*self.args):
            if(self.pause):
                self.ev.wait()
            if(self.kill):
                return




class MyAppAction:
    algo = ["DFS", "BFS", "uniform cost", "Astar"]
    algorithms=[Algorithms.dfs,Algorithms.bfs,Algorithms.uniform_cost,Algorithms.a_star]
    def __init__(self, algoSelect:QComboBox, delaySelect:QtWidgets.QDoubleSpinBox, startSelect:QComboBox, endSelect:QComboBox, textarea, playbt:QToolButton, stopbt:QToolButton, pausebt:QToolButton,
                 view, saveBt:QAction):
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




    def setAlgorithmList(self):
        self.algoSelect.addItems(MyAppAction.algo)

    def setDelaiList(self):
        self.delaySelect.setValue(1)

    def display_image(self, img):
        self.view.setPixmap(QtGui.QPixmap(img))
        self.view.show()
        QCoreApplication.processEvents()  # let Qt do his work
        if hasattr(self, 'delay'):
            time.sleep(self.delay)

    def createGraph(self,name):
        self.graph = Graph(display=self.display_image,edgesdict= \
                           [{NAME: 'e1', VAL: 5, NODE1: '1', NODE2: '2'},
                            {NAME: 'e2', VAL: 15, NODE1: '3', NODE2: '4'},
                            {NAME: 'e3', VAL: 7, NODE1: '5', NODE2: '4'},
                            {NAME: 'e4', VAL: 25, NODE1: '6', NODE2: '9'},
                            {NAME: 'e5', VAL: 5, NODE1: '8', NODE2: '10'},
                            {NAME: 'e6', VAL: 3, NODE1: '11', NODE2: '13'},
                            {NAME: 'e7', VAL: 1, NODE1: '7', NODE2: '3'},
                            {NAME: 'e8', VAL: 4, NODE1: '14', NODE2: '6'},
                            {NAME: 'e9', VAL: 2, NODE1: '2', NODE2: '7'},
                            {NAME: 'e10', VAL: 9, NODE1: '13', NODE2: '2'},
                            {NAME: 'e11', VAL: 6, NODE1: '3', NODE2: '6'},
                            {NAME: 'e12', VAL: 4, NODE1: '8', NODE2: '2'},
                            {NAME: 'e13', VAL: 10, NODE1: '5', NODE2: '3'},
                            {NAME: 'e14', VAL: 5, NODE1: '10', NODE2: '2'},
                            {NAME: 'e15', VAL: 8, NODE1: '2', NODE2: '11'},
                            {NAME: 'e16', VAL: 3, NODE1: '3', NODE2: '2'},
                            {NAME: 'e17', VAL: 8, NODE1: '12', NODE2: '1'}
                            ],
                       heuristic= \
                           {'14':
                                {'4': 17,
                                 '5': 10,
                                 '3': 7,
                                 '6': 13,
                                 '14': 15,
                                 '9': 14,
                                 '8': 8,
                                 '10': 6,
                                 '2': 4,
                                 '7': 6,
                                 '1': 0,
                                 '13': 12,
                                 '11': 1000,
                                 '12': 6}})
        def cmp_to_key():
            'Convert a cmp= function into a key= function'

            class K(object):
                def __init__(self, obj, *args):
                    self.obj = obj

                def __lt__(self, other):
                    return int(self.obj)<int(other.obj)
            return K

        self.graph.nodes.sort(key=cmp_to_key())

        self.startSelect.addItems(self.graph.nodes)
        self.endSelect.addItems(self.graph.nodes)
        self.endSelect.setCurrentIndex(0)
        self.startSelect.setCurrentIndex(0)
        self.graph.display()

    def pause(self):
        self.t.pausef()

    def stop(self):
        self.t.killf()

    def play(self):
        self.graph.init()
        self.curAlgo = MyAppAction.algorithms[self.algoSelect.currentIndex()]
        a=self.startSelect.currentIndex()
        b=self.endSelect.currentIndex()
        self.startNode = self.startSelect.currentText()
        self.goleNode = self.endSelect.currentText()
        self.delay=self.delaySelect.value()
        self.t = MyThread(self.curAlgo,self.graph,self.startNode,self.goleNode)
        self.t.start()




