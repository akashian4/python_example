
##progressbar()

from PyQt5.QtWidgets import QWidget,QProgressBar,QPushButton,QApplication
import sys
import   time   as  tm



class F(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setUI()
        
        
    def setUI(self):      
     self.setGeometry(300, 300, 280, 170)
     self.setWindowTitle('progress')
     self.setFixedSize(300,300)

     self.prog = QProgressBar(self)
     self.prog.setGeometry(40,40,250,10)

     self.btn = QPushButton('download', self)
     self.btn.move(40,80)
     self.btn.clicked.connect(lambda : self.download())  
     self.list1=list(range(201))		
     self.show()
              
			  
    def  download(self):	
     for   i   in    self.list1:
      tm.sleep(.5)
      print(type(i))	 
      self.prog.setValue(i)
	
	
        
if __name__ == '__main__':   
    app = QApplication(sys.argv)
    ex = F()
    sys.exit(app.exec_()) 
