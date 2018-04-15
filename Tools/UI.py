# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys
from main import Exemple
from TF_ui import TF
class TabWidget(QtGui.QTabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)
        self.resize(500,500)
        self.center()
        self.setWindowTitle(u'工具')
        self.setWindowIcon(QtGui.QIcon("icon.jpg"))
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif',10))
        self.mContent = Exemple()
        self.mIndex = TF()
        self.addTab(self.mContent, u"常用")
        self.addTab(self.mIndex, u"文本文件")
        self.show()
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
def main():
    app = QtGui.QApplication(sys.argv)
    ex = TabWidget()
    sys.exit(app.exec_())
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    t = TabWidget()
    app.exec_()

