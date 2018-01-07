#from PyQt5 import QtWidgets  
#import test  
#import sys
 
#class mywindow(QtWidgets.QWidget):  
#     def __init__(self):  
#         super(mywindow,self).__init__()  
#         self.new=test.Ui_MainWindow()  
#         self.new.setupUi(self)  
#  
#if __name__=="__main__":  
#     app=QtWidgets.QApplication(sys.argv)  
#     myshow=mywindow()  
#     myshow.show()  
#     sys.exit(app.exec_())  
     
import sys      
from PyQt5 import QtWidgets  
from test import Ui_MainWindow  
  
class mywindow(QtWidgets.QWidget,Ui_MainWindow):  
    def __init__(self):  
        super(mywindow,self).__init__()  
        self.setupUi(self)  
  
if __name__=="__main__":  
  
    app=QtWidgets.QApplication(sys.argv)  
    myshow=mywindow()  
    myshow.show()  
    sys.exit(app.exec_())  