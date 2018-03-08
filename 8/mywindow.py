from PyQt5 import QtWidgets  
from ui import Ui_MainWindow  
from Children import Ui_Form  
from PyQt5.QtWidgets import QFileDialog  


class ChildrenForm(QtWidgets.QWidget,Ui_Form):  
    def __init__(self):  
        super(ChildrenForm,self).__init__()  
        self.setupUi(self)  
  
class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):  
    def __init__(self):  
        super(MyWindow,self).__init__()  
        self.setupUi(self) 

        self.child=ChildrenForm()                          #self.child = children()生成子窗口实例 

        self.fileOpen.triggered.connect(self.openMsg)      #菜单的点击事件是triggered  
        self.fileClose.triggered.connect(self.childShow)      
        
    def childShow(self):  
        self.gridLayout_2.addWidget(self.child)          #添加子窗口  
        self.child.show()  

    def openMsg(self):  
        file,ok=QFileDialog.getOpenFileName(self,"打开","C:/","All Files (*);;Text Files (*.txt)")  
        self.statusbar.showMessage(file)                   #在状态栏显示文件地址  



if __name__=="__main__":  
    import sys  
  
    app=QtWidgets.QApplication(sys.argv)  
    myshow=MyWindow()  
    myshow.show()  
    sys.exit(app.exec_())  

