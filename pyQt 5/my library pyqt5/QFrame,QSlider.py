
###==============
##QFrame,QSlider
##===================================================================================
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QPushButton,QFrame,QSlider
from  PyQt5.QtGui    import   QColor
from PyQt5.QtCore    import Qt
import    random    as    rn

 
class F(QWidget):
 
    def __init__(self):
        super().__init__()
        self.setUI()
 
    def setUI(self):
     self.setWindowTitle("slider_color")
     self.setGeometry(10,10,500,500)
     self.setFixedSize(500,500)
	
     self.qf=QFrame(self)
     self.qf.setGeometry(100,10,300,300)	 
	 
     self.slider = QSlider(Qt.Horizontal,self)
     self.slider.setGeometry(100, 320, 480, 15)
     self.slider.valueChanged.connect(lambda  :   self.change_slider())

####=====================================setColor
     self.palette=self.qf.palette()
     role=self.qf.backgroundRole()	 
     self.palette.setColor(role,QColor(250,255,250))
     self.qf.setPalette(self.palette)
     self.qf.setAutoFillBackground(True) 
####=========================================
	
     self.show()
	 
    def   change_slider(self):
	
     ##RGB=(2(bit)^8)*(2(bit)^8)*(2(bit)^8)=256*256*256=16777216
     ##R=[a,b,c,d,....]#0-255===>>len(R)=100
     ##G=[a2,b2,c2,d2,...]#0-255===>>len(G)=100
     ##B=[a3,b3,c3,d3,]#0-255===>>len(B)=100
     ##LIST_COLOR=[[R[0] G[0] B[0]],[[R[1] G[1] B[1]],[.....],.........]=[[a,a2,a3],[b,b2,b3],[.....],.........]
	

     color_change=self.slider.value()
     ###0-99=100

     Red=[]
     Green=[]
     Blue=[]

     for    i   in   list(range(100)):
       Red.append(rn.randint(0,255))
       Green.append(rn.randint(0,255))
       Blue.append(rn.randint(0,255))
	 
     loop=list(range(100))
     LIST_COLOR=[]
     
     self.palette=self.qf.palette()
     role=self.qf.backgroundRole()
	  
     for    i  in  loop:
       arg=[Red[i],Green[i],Blue[i]]
       LIST_COLOR.append(arg)
	 
     print(LIST_COLOR)
      
     if   color_change==0:
      self.x=255
      self.y=255
      self.z=200
      self.palette.setColor(role,QColor(self.x,self.y,self.z))
      self.qf.setPalette(self.palette)
      self.qf.setAutoFillBackground(True) 
     else:
      self.x,self.y,self.z = LIST_COLOR[color_change]###R,G,B
      self.palette.setColor(role,QColor(self.x,self.y,self.z))
      self.qf.setPalette(self.palette)
      self.qf.setAutoFillBackground(True) 
####=========================================

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = F()
    sys.exit(app.exec_())  
        
    

            


	   

