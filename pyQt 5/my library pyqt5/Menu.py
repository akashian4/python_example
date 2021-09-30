
##Menu
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QLabel,QMainWindow,QAction

class   F(QMainWindow):
 def __init__(self):
  super().__init__()
  self.setUI()

 def  setUI(self):
  self.setGeometry(10,10,300,300)
  self.setWindowTitle("Faradars")
  btn = QPushButton("copy",self)
  btn.move(100,100)
  btn.clicked.connect(self.exit) 
##==================================
  self.textbox1=QLineEdit(self) 
  self.textbox1.move(10,30)
  self.textbox1.resize(200,20)
  
  self.textbox2=QLineEdit(self) 
  self.textbox2.move(10,55)
  self.textbox2.resize(200,20)
   
  label1 = QLabel("input",self)
  label2 = QLabel("output",self)
  label1.move(215,35)
  label2.move(215,60)
####=====================================menu
  mainM = self.menuBar()
  fileM = mainM.addMenu("File")
  editM = mainM.addMenu("Edit")
  searchM = mainM.addMenu("Search")
  viewM = mainM.addMenu("View")
  encodingM = mainM.addMenu("Encoding")
  languageM = mainM.addMenu("Language")
  settingM = mainM.addMenu("Setting")
  toolsM = mainM.addMenu("Tools")
  macroM = mainM.addMenu("Macro")
  runM = mainM.addMenu("Run")
  pluginsM = mainM.addMenu("Plugins")
  windowM = mainM.addMenu("Window")
  helpM = mainM.addMenu("?")
  
###=========================================QAction
  NewB = QAction("New",self)
  editB = QAction("Edit",self)
  saveB = QAction("Save as",self)
  exitB = QAction("Exit",self)
  
  fileM.addAction(NewB)
  fileM.addAction(editB)
  fileM.addAction(saveB)
  fileM.addAction(exitB)
  
  
  exitB.triggered.connect(self.print2)
   
  #widget.signal.connect(funtion)
###===================================================================
  self.show() 
  
 def   print2(self):
   print("close")
   self.close()

 def   exit(self):
  T1=self.textbox1.text()
  self.textbox2.setText(T1)
  
if  __name__=="__main__":
 print(__name__)
 app = QApplication(sys.argv)
 ex=F()
 sys.exit(app.exec_())
 

 
