###QComboBox
import   sys
from PyQt5.QtWidgets import   QWidget,QLabel,QApplication,QComboBox

class F(QWidget):    
    def __init__(self):
        super().__init__()
        self.setUI()
        
    def setUI(self):      
     self.lbl = QLabel(" ", self)
     self.lbl.resize(50,20)
     self.lbl.move(50, 150)		
     self.setGeometry(300, 300, 300, 200)
     self.setWindowTitle('faradars')
	 
     self.com1=QComboBox(self)
     self.com1.addItem("python",self)
     self.com1.addItem("java",self)
     self.com1.addItem("C++",self)
     self.com1.addItem("PyQt5",self)

     self.com1.move(100,100)
     self.com1.resize(200,20)

     self.com1.activated.connect(lambda  : self.combItem())
     self.show()
     
    def    combItem(self):
     text=self.com1.currentText()
     index=self.com1.currentIndex()
     print(text,' ',index)
     self.lbl.setText(text)
     
     
         
	
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = F()
    sys.exit(app.exec_())
    
