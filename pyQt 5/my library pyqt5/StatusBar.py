####===============

###StatusBar


import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QMainWindow


class   F(QMainWindow):
 def __init__(self):
  super().__init__()
  self.setUI()

 def  setUI(self):
  self.setGeometry(10,10,300,300)
  self.setWindowTitle("Faradars") 
  
  btn = QPushButton("close",self)
  btn.move(100,100)
  btn.clicked.connect(self.click)
  
  self.statusBar().showMessage("first")
  self.show() 
  
 def   click(self):
  self.close()
  
   
if  __name__=="__main__":
 print(__name__)
 app = QApplication(sys.argv)
 ex=F()
 sys.exit(app.exec_())
