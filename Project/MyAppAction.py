from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import Algorithms
import time
import timeit
import threading
from DataFromFile import *
from Graph import *
NAME = "NAME"
NODE1 = "NODE1"
NODE2 = "NODE2"
VAL = "LENGTH"

class MyThread(QThread):
    displayFun = pyqtSignal(str)
    def __init__(self, dispalyFun,target ,*args):
        super().__init__()
        self.displayFun.connect(dispalyFun)
        self.target=target
        self.args=args
        self.pause=False
        self.kill=False
        self.ev=threading.Event()

    def pausef(self):
        if(self.pause):
            self.ev.set()
        self.pause=not self.pause

    def killf(self):
        self.kill=True

    def run(self):
        gen=self.target(*self.args)
        start_time=timeit.default_timer()
        while 1:
            try:
                next(gen)
                if (self.pause):
                    self.ev.wait()
                    self.ev.clear()
                if (self.kill):
                    return
            except StopIteration as ex:
                time=timeit.default_timer() - start_time
                if(len(ex.value[0])==0):
                    text="But non atteint "+"\nPath: " + ex.value[1].__str__() +"\nexecution time: "+str(time)
                else:
                    text="Solution path: " + ex.value[0].__str__() +"\nPath: " + ex.value[1].__str__() +"\nPath legth: " + str(ex.value[2])+"\nexecution time: "+str(time)
                self.displayFun.emit(text)
                return


class MyAppAction:
    algo = ["DFS", "BFS", "iterative_deepening", "uniform cost","best_first", "Astar","iterative_a_star"]
    algorithms = [Algorithms.dfs, Algorithms.bfs, Algorithms.iterative_deepening,
                  Algorithms.uniform_cost, Algorithms.best_first, Algorithms.a_star,
                  Algorithms.iterative_a_star]

    '''
    define the selction of the algos, delay, start and finish node
    specify the stop, play, pause , save button and define the methods corresponding to the clicks on the corresponding buttons
    '''
    def __init__(self, algoSelect: QComboBox, delaySelect: QtWidgets.QDoubleSpinBox, startSelect: QComboBox,
                 endSelect: QComboBox, textarea:QTextBrowser, playbt: QToolButton, stopbt: QToolButton, pausebt: QToolButton,
                 view):
        self.algoSelect = algoSelect
        self.delaySelect = delaySelect
        self.startSelect = startSelect
        self.startSelect.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.endSelect = endSelect
        self.endSelect.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.textarea = textarea
        self.playbt = playbt
        self.stopbt = stopbt
        self.pausebt = pausebt
        self.view = view
        self.setAlgorithmList()
        self.setDelaiList()
        self.playbt.clicked.connect(self.play)
        self.pausebt.clicked.connect(self.pause)
        self.stopbt.clicked.connect(self.stop)
        self.result=False

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

        self.graph = Graph(display=self.display_image, edgesdict= edgesdata,
                           heuristic= heurisiticdata)
        def cmp_to_key():
            'Convert a cmp= function into a key= function'

            class K(object):
                def __init__(self, obj, *args):
                    self.obj = obj

                def __lt__(self, other):
                    try:
                        return int(self.obj) < int(other.obj)
                    except ValueError:
                        return self.obj<other.obj


            return K

        self.graph.nodes.sort(key=cmp_to_key())
        self.startSelect.clear()
        self.endSelect.clear()
        self.startSelect.addItems(self.graph.nodes)
        self.endSelect.addItems(self.graph.nodes)
        self.endSelect.setCurrentIndex(0)
        self.startSelect.setCurrentIndex(0)
        self.graph.display()
        self.textarea.setText(self.graph.__str__())

    def display_result(self,text):
        self.textarea.setText(self.textarea.toPlainText()+"\n"+text)
        self.result=True

    def saveTrace(self,name):
        if(self.result):
            with open(name[0],'w') as f:
                f.write(self.textarea.toPlainText())
            self.textarea.setText(self.textarea.toPlainText()+"\ntrace saved (y)")
        else:
            self.textarea.setText("no trace found")

    def pause(self):
        self.t.pausef()

    def stop(self):
        self.t.killf()
        self.result=False
        self.graph.display()
        self.textarea.setText(self.graph.__str__())
        self.disable_enable(True)


    def play(self):
        self.result=False
        self.disable_enable(False)
        self.textarea.setText(self.textarea.toPlainText()+"\n"+MyAppAction.algo[self.algoSelect.currentIndex()]+":")
        self.graph.init()
        self.curAlgo = MyAppAction.algorithms[self.algoSelect.currentIndex()]
        a = self.startSelect.currentIndex()
        b = self.endSelect.currentIndex()
        self.startNode = self.startSelect.currentText()
        self.goleNode = self.endSelect.currentText()
        self.delay = self.delaySelect.value()
        self.t = MyThread(self.display_result,self.curAlgo, self.graph, self.startNode, self.goleNode)
        self.t.start()

    def disable_enable(self,state):
        self.playbt.setEnabled(state)
        self.algoSelect.setEnabled(state)
        self.startSelect.setEnabled(state)
        self.endSelect.setEnabled(state)
        self.delaySelect.setEnabled(state)



