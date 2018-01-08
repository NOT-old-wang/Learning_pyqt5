# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 19:25:30 2018

@author: laowang
"""
'''
     QMessageBox.information 信息框
     QMessageBox.question 问答框
     QMessageBox.warning 警告
     QMessageBox.ctitical危险
     QMessageBox.about 关于
'''

from PyQt5 import QtWidgets,QtCore  
from ui import Ui_Form  
from PyQt5.QtWidgets import QMessageBox   #使用QMessageBox
import time  
import sys  
    
class MyWindow(QtWidgets.QWidget,Ui_Form):  
    _signal=QtCore.pyqtSignal(str)        #定义信号,定义参数为str类型  
    def __init__(self):    
        super(MyWindow,self).__init__()  
        self.setupUi(self)  
        '''一个按钮接连了两个'''
        self.Button_print.clicked.connect(self.msg) 
        self.Button_print.clicked.connect(self.myPrint)  
        self._signal.connect(self.mySignal)  #将信号连接到函数mySignal  

    def msg(self):  
        reply = QMessageBox.warning(self,                         #使用infomation信息框  
                                    "警告",                              
                                    "正在打印",  
                                    QMessageBox.Yes | QMessageBox.No)  
  
    def myPrint(self):  
        self.textEdit.setText("come on")  
        self.textEdit.append("正在打印，请稍候")  
        self._signal.emit("你妹，打印结束了吗，快回答！")  
    def mySignal(self,string):  
        print(string) 
        time.sleep(2)
        self.textEdit.append("打印结束")    
  
if __name__=="__main__":      
    
    app=QtWidgets.QApplication(sys.argv)    
    myshow=MyWindow()  
    myshow.show()    
    sys.exit(app.exec_())   
