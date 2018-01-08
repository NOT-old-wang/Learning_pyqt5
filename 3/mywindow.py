# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 15:50:14 2018

@author: laowang
"""

from PyQt5 import QtWidgets    
from ui import Ui_MainWindow   
import sys   
"""点击按钮，在控制台输出helloworld"""    
class MyWindow(QtWidgets.QWidget,Ui_MainWindow):    
    def __init__(self):    
        super(MyWindow,self).__init__()    
        self.setupUi(self)  
        self.Button1.clicked.connect(self.myPrint)   #槽函数不用加括号  
    def myPrint(self):                               #定义槽  
        print("hello dawang!")  
    
if __name__=="__main__":    
    app=QtWidgets.QApplication(sys.argv)    
    myshow=MyWindow()    
    myshow.show()    
    sys.exit(app.exec_())  