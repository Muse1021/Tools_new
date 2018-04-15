# -*- coding: utf-8 -*-
import time
import os,subprocess,time,re,sys
from Utils import *
reload(sys)
sys.setdefaultencoding( "utf-8" )
class Test1(QtGui.QWidget):
    def __init__(self):
        super(Test1,self).__init__()
        self.t_ui()
    def t_ui(self):
        btn = QtGui.QPushButton(u'安装',self)
        btn.clicked.connect(self.btn_devices)
        btn.resize(btn.sizeHint())
        btn.move(400,100)
        self.show()
    def btn_devices(self):
        shell = "adb shell"
        a = cmd(self,shell)
        print a
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ic = Test1()
    sys.exit(app.exec_())


def test():
    screenshot = "adb shell /system/bin/screencap -p /sdcard/screenshot.png"
    pic_name = str(int(time.time()))+".png"
    screenshot_pull = "adb pull /sdcard/screenshot.png E:/screenshot/%s"%pic_name
    subprocess.Popen(screenshot,shell=True, stdout=subprocess.PIPE).stdout
    if  os.path.exists("E:/screenshot"):
        pass
    else:
        os.mkdir("E:/screenshot")
    Poplog = subprocess.Popen(screenshot_pull, shell=True, stdout=subprocess.PIPE).stdout
    Poplog.readlines()
a = "sssss"
b = "bbbbb"
print "%s1%s2"%(a,b)

def test():
    screenshot = "adb shell /system/bin/screencap -p /sdcard/screenshot.png"
    pic_name = str(int(time.time()))+".png"
    screenshot_pull = "adb pull /sdcard/screenshot.png E:/screenshot/%s"%pic_name
    subprocess.Popen(screenshot,shell=True, stdout=subprocess.PIPE).stdout
    if  os.path.exists("E:/screenshot"):
        pass
    else:
        os.mkdir("E:/screenshot")
    Poplog = subprocess.Popen(screenshot_pull, shell=True, stdout=subprocess.PIPE).stdout
    Poplog.readlines()
#a = "sssss"
#b = "bbbbb"
#print "%s1%s2"%(a,b)
def find():
	P = "adb devices"
	Poplog =subprocess.Popen(P,shell = True,stdout = subprocess.PIPE, stderr = subprocess.PIPE).stdout
	devices = Poplog.readlines()
	print devices
	devices_list = []
	model_list ={}
	for i in devices:
		#if not any(s in i for s in ("devices","daemon")) and len(i.split()) > 0:
		if not re.search('devices|daemon',i) and len(i.split()) > 0:
			devices_list.append(i.split()[0])
	device_number = len(devices_list)
	print(devices_list)	
find()
