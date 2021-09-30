####===============

###PushButton

import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton

class   F(QWidget):
 def __init__(self):
  super().__init__()
  self.setUI()

 def  setUI(self):
  self.setGeometry(10,10,300,300)
  self.setWindowTitle("Faradars")
  btn = QPushButton("close",self)
  btn.move(100,100)
  #btn.clicked.connect(self.click)
  btn.clicked.connect(self.exit)
  self.show() 
  
 def   click(self):
   print("python is simple")
   
 def    print2(self):
  print("pyqt is  simple")
  
  
 def  exit(self):
  self.close()
   
 
if  __name__=="__main__":
 print(__name__)
 app = QApplication(sys.argv)
 ex=F()
 sys.exit(app.exec_())
