#import sys  
#from PyQt5 import QtWidgets  
#  
#  
##pyqt窗口必须在QApplication方法中使用  
#app=QtWidgets.QApplication(sys.argv)  
#  
##qt支持html标签，强大吧   
#label=QtWidgets.QLabel("<p style='color: red; margin-left: 20px'><b>hell world</b></p>") 
##有了实例，就需要用show()让他显示  
#label.show()  
#  
# #消息结束的时候，进程结束，并返回0，接着调用sys.exit(0)退出程序    
#sys.exit(app.exec_())     


import sys 
from PyQt5 import QtWidgets  
#从PyQt库导入QtWidget通用窗口类  
class mywindow(QtWidgets.QWidget):  
#自己建一个mywindows类，以class开头，mywindows是自己的类名，  
#（QtWidgets.QWidget）是继承QtWidgets.QWidget类方法，  
    def __init__(self):  
        super(mywindow,self).__init__()  
  
app = QtWidgets.QApplication(sys.argv)  
windows = mywindow()  
label=QtWidgets.QLabel(windows)     #在窗口中绑定label  
label.setText("hello world")  
  
windows.show()  
sys.exit(app.exec_())  