###--------------
##QMessageBox.Cancel	
##QMessageBox.Open	
##QMessageBox.Discard	
##QMessageBox.Reset	
##QMessageBox.No	
##QMessageBox.NoToAll	
##QMessageBox.NoButton
##QMessageBox.RestoreDefaults	
##QMessageBox.Abort	
##QMessageBox.Retry
##QMessageBox.Ignore
##QMessageBox.Ok	
##QMessageBox.Help
##QMessageBox.Save
##QMessageBox.SaveAll 
##QMessageBox.Close
##QMessageBox.Apply 
##QMessageBox.Yes
##QMessageBox.YesToAll 
######====================

##QMessageBox
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QMessageBox
class   F(QWidget):
 def __init__(self):
  super().__init__()
  self.setUI()

 def  setUI(self):
  self.setGeometry(10,10,300,300)
  self.setWindowTitle("Faradars")
  btn = QPushButton("close",self)
  btn.move(100,100)
  btn.clicked.connect(self.exit) 
  self.show() 

 def   exit(self):
   qms = QMessageBox.question(self,"Message","do you want close it?",QMessageBox.Yes | QMessageBox.No | QMessageBox.Help)
   if   qms ==  QMessageBox.Yes:
    self.close()
   elif  qms == QMessageBox.No:
    pass
   elif  qms == QMessageBox.Help :
    print("python.org") 
   

 
if  __name__=="__main__":
 print(__name__)
 app = QApplication(sys.argv)
 ex=F()
 sys.exit(app.exec_())
 

 
