##label-pixmap

import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton
from  PyQt5.QtGui    import   QPixmap



class   F(QWidget):
 def __init__(self):
  super().__init__()
  self.setUI()

 def  setUI(self):
  self.setGeometry(10,10,300,300)
  self.setWindowTitle("Faradars")
 
 
 
 
  lb=QLabel(self)
  pix=QPixmap('C:/Users/RF/Desktop/faradars/image.jpg')
  
  x=pix.width()
  y=pix.height()
  
  lb.setPixmap(pix)
  lb.move(10,10)
  
  
  bt=QPushButton("faradars.ir",self)
  bt.move(x+10,10)
  bt.resize(60,55)
  
  
  self.show()

  
  
if  __name__=="__main__":
 print(__name__)
 app = QApplication(sys.argv)
 ex=F()
 sys.exit(app.exec_())

  
  
  
  

 
 

