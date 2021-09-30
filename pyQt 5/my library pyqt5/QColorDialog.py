
###==============
##QColorDialog
##QColor
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QColorDialog,QPushButton
from  PyQt5.QtGui    import   QColor

 
class F(QWidget):
 
    def __init__(self):
        super().__init__()
        self.setUI()
 
    def setUI(self):
     self.setWindowTitle("photo_color")
     self.setGeometry(10,10,500,500)
     self.setFixedSize(500,500)
     
     p1=QPushButton("color1",self)
     p1.move(50,10)
     p1.resize(200,200)
     p1.clicked.connect(lambda : self.dialcolor(p1))
	 
	 
     p2=QPushButton("color2",self)
     p2.move(250,10)
     p2.resize(200,200)
     p2.clicked.connect(lambda : self.dialcolor(p2))
	 
	 
     p3=QPushButton("color3",self)
     p3.move(50,250)
     p3.resize(200,200)
     p3.clicked.connect(lambda : self.dialcolor(p3))
	 
     p4=QPushButton("color4",self)
     p4.move(250,250)
     p4.resize(200,200)
     p4.clicked.connect(lambda : self.dialcolor(p4))
	 
	 
     self.show()
	 
    def     dialcolor(self,push):
     QC=QColorDialog()
     C=QC.getColor()
     C1=C.name()
####=========================setting  color  widget 
     palette = push.palette()
     role = push.foregroundRole()
     role1 = push.backgroundRole()
     palette.setColor(role, QColor(C1))
     palette.setColor(role1,QColor(C1))
     push.setPalette(palette)
     push.setAutoFillBackground(True)
###==================================== 
     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = F()
    sys.exit(app.exec_())  
	   
	   

