# -*-coding: utf-8 -*-

from ReQLineEdit import Edit
from PyQt4 import QtGui,QtCore
import os,subprocess,time,re,sys
from Functions import *
reload(sys)
sys.setdefaultencoding( "utf-8" )
class TF(QFunction):
    def __init__(self):
        super(TF,self).__init__()
        self.initUI()
    def initUI(self):
        #刷新按钮
        btn_re2 = QtGui.QPushButton(self)
        btn_re2.setStyleSheet("QPushButton{background-image:url(1.png);width:20px;height:20px;padding-top:0px;}")
        btn_re2.clicked.connect(self.devices_list)
        btn_re2.move(440,10)
        #手机列表下拉框
        self.lab_devices = QtGui.QLabel(u"当前设备:",self)
        self.lab_devices.resize(100,20)
        self.lab_devices.move(280,10)
        string_list = [u'无设备']
        self.combo = QtGui.QComboBox(self)
        self.combo.addItems(string_list)
        self.combo.resize(80, 20)
        self.combo.move(350,10)
        #输入框
        self.lab_textpath = QtGui.QLabel(u"文本：",self)
        self.lab_textpath.resize(100,20)
        self.lab_textpath.move(15,50)
        self.inputtext =  QtGui.QLineEdit(self)
        self.inputtext.setGeometry(QtCore.QRect(60, 40, 280, 30))
        self.inputtext.setText("")
        #输入按钮
        btn_inp = QtGui.QPushButton(u'输入',self)
        btn_inp.clicked.connect(self.InputText)
        btn_inp.move(380,40)

        #手机地址输入框
        self.sj_lab = QtGui.QLabel(u"手机路径：",self)
        self.sj_lab.resize(100,20)
        self.sj_lab.move(15,110)
        self.sj_path =Edit(self)
        self.sj_path.setGeometry(QtCore.QRect(85, 100, 280, 30))
        self.sj_path.setText("")

        #导入手机按钮
        btn_sj = QtGui.QPushButton(u'导入手机',self)
        btn_sj.clicked.connect(self.Push_file)
        btn_sj.move(380,100)
        #导入pc按钮
        btn_pc = QtGui.QPushButton(u'导入pc',self)
        btn_pc.clicked.connect(self.Pull_file)
        btn_pc.move(380,140)
        #pc地址输入框
        self.pc_lab = QtGui.QLabel(u"pc路径：",self)
        self.pc_lab.resize(100,20)
        self.pc_lab.move(15,150)
        self.pc_path =Edit(self)
        self.pc_path.setGeometry(QtCore.QRect(85, 140, 280, 30))
        self.pc_path.setText("")
        self.show()