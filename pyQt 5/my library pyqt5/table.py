
##========================
##|    | pr1    | pr2    |    
##========================
##| p1 |  ...   | ....   |    
##========================
##| p2 |  ...   | ....   |    
##========================
##| p3 |  ...   | ....   |    
##========================

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QTableWidget,QTableWidgetItem,QVBoxLayout


class   F(QWidget):
 def __init__(self):
  super().__init__()
  self.setUI()

 def  setUI(self):
  self.setGeometry(10,10,300,300)
  self.setWindowTitle("Faradars") 
  self.table()  
  
  
  self.lay = QVBoxLayout()
  self.lay.addWidget(self.tw)
  self.setLayout(self.lay)
  self.show()
  
  
 def    table(self):
  self.tw = QTableWidget()
  self.tw.setRowCount(4)
  self.tw.setColumnCount(3)
  self.tw.setItem(0,1,QTableWidgetItem("pr1"))
  self.tw.setItem(0,2,QTableWidgetItem("pr2"))
  self.tw.setItem(1,0,QTableWidgetItem("p1"))
  self.tw.setItem(2,0,QTableWidgetItem("p2"))
  self.tw.setItem(3,0,QTableWidgetItem("p3"))
  
  self.tw.clicked.connect(self.print_twcell)
  
 def   print_twcell(self):
   for  cell   in   self.tw.selectedItems(): 
    print(cell.text())
  
 
if  __name__=="__main__":
 print(__name__)
 app = QApplication(sys.argv)
 ex=F()
 sys.exit(app.exec_())
