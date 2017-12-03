# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MyAppAction import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.graphicsView = QtWidgets.QLabel(self.splitter)
        self.graphicsView.setObjectName("graphicsView")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(10, 10, 20, 10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(4, 4, 4, 4)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.algoSelect = QtWidgets.QComboBox(self.widget)
        self.algoSelect.setObjectName("algoSelect")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.algoSelect)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.delaySelect = QtWidgets.QDoubleSpinBox(self.widget)
        self.delaySelect.setObjectName("delaySelect")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.delaySelect)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.startSelect = QtWidgets.QComboBox(self.widget)
        self.startSelect.setObjectName("startSelect")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.startSelect)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.endSelect = QtWidgets.QComboBox(self.widget)
        self.endSelect.setObjectName("endSelect")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.endSelect)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.textarea = QtWidgets.QTextBrowser(self.widget)
        self.textarea.setObjectName("textarea")
        self.verticalLayout_4.addWidget(self.textarea)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stopbt = QtWidgets.QToolButton(self.widget)
        self.stopbt.setObjectName("stopbt")
        self.horizontalLayout.addWidget(self.stopbt)
        self.playbt = QtWidgets.QToolButton(self.widget)
        self.playbt.setObjectName("playbt")
        self.horizontalLayout.addWidget(self.playbt)
        self.pausebt = QtWidgets.QToolButton(self.widget)
        self.pausebt.setObjectName("pausebt")
        self.horizontalLayout.addWidget(self.pausebt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 34))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        self.about = QtWidgets.QMenu(self.menubar)
        self.about.setObjectName("about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openBt = QtWidgets.QAction(MainWindow)
        self.openBt.setObjectName("openBt")
        self.saveBt = QtWidgets.QAction(MainWindow)
        self.saveBt.setObjectName("saveBt")
        self.menuFiles.addAction(self.openBt)
        self.menuFiles.addAction(self.saveBt)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.about.menuAction())

        self.retranslateUi(MainWindow)
        # Action definition
        self.openBt.triggered.connect(self.getFile)
        self.saveBt.triggered.connect(self.saveFile)
        self.myAction = MyAppAction(self.algoSelect, self.delaySelect, self.startSelect, self.endSelect,
                               self.textarea, self.playbt, self.stopbt, self.pausebt, self.graphicsView)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getFile(self):
        fname = QFileDialog.getOpenFileName(self.widget, 'Open file','', "Text files (*.txt);;XML files (*.xml)")
        self.myAction.createGraph(fname)

    def saveFile(self):
        fname = QFileDialog.getSaveFileName(self.widget, 'Save file','', "Text files (*.txt)")
        self.myAction.saveTrace(fname)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Algorithm"))
        self.label_2.setText(_translate("MainWindow", "Delay"))
        self.label_3.setText(_translate("MainWindow", "Start Node:"))
        self.label_4.setText(_translate("MainWindow", "End Node:  "))
        self.stopbt.setText(_translate("MainWindow", "stop"))
        self.playbt.setText(_translate("MainWindow", "play"))
        self.pausebt.setText(_translate("MainWindow", "pause"))
        self.menuFiles.setTitle(_translate("MainWindow", "Fi&le"))
        self.about.setTitle(_translate("MainWindow", "Abo&ut"))
        self.openBt.setText(_translate("MainWindow", "Open"))
        self.saveBt.setText(_translate("MainWindow", "save trace"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

