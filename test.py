#!/usr/bin/python


import sys
#from mainwin import Ui_MainWindow

from PyQt4 import QtGui, uic

app = QtGui.QApplication(sys.argv)

class MyMain(QtGui.QMainWindow):
    def __init__(self):
        super(MyMain, self).__init__()
        uic.loadUi('./test/mainwindow.ui', self)
#        self.show()

def pyqtDemo():
#    w = Ui_MainWindow()
#    w.setupUi(w)
    w = MyMain()
    w.show()

if __name__ == "__main__":
    pyqtDemo()
    sys.exit(app.exec_())

    
    

