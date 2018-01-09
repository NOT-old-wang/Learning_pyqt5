from PyQt5 import QtWidgets  
from ui import Ui_MainWindow  
from PyQt5.QtWidgets import QFileDialog  
  
class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):  
    def __init__(self):  
        super(MyWindow,self).__init__()  
        self.setupUi(self)  
        self.fileOpen.triggered.connect(self.openMsg)      #菜单的点击事件是triggered  
        self.fileClose.triggered.connect(self.openMsg)      #菜单的点击事件是triggered  
  
    def openMsg(self):  
        file,ok=QFileDialog.getOpenFileName(self,"打开","C:/","All Files (*);;Text Files (*.txt)")  
        self.statusbar.showMessage(file)                   #在状态栏显示文件地址  
  
if __name__=="__main__":  
    import sys  
  
    app=QtWidgets.QApplication(sys.argv)  
    myshow=MyWindow()  
    myshow.show()  
    sys.exit(app.exec_())  