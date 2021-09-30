import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])


# plt.plot(x, y)
# plt.plot(x, y, 'o')    # without line
# plt.plot(y)    # default x point is 0 1 2 3 ...


#markers
# plt.plot(y, marker = 'o')
# plt.plot(y, marker = '*')
# plt.plot(y, marker = '3')
# plt.plot(y, marker = 'H')


#'marker line color'
# plt.plot(y, 'o:r')     'marker line color'
# plt.plot(y, 'o--')
# plt.plot(y, '*-.')


# ms ==> markerSize  ,  mec ==> markerColor  ,  mf ==> markerFaceColor
# plt.plot(y, marker = 'o', ms = 20, mec = 'r')
# plt.plot(y, marker = 'o', ms = 20, mfc = 'r')
# plt.plot(y, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
# plt.plot(y, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
# plt.plot(y, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')


#Linestyle or ls
# plt.plot(y, linestyle = 'dotted')
# plt.plot(y, ls = 'dashed')
# plt.plot(y, ls = ':')


#line color  ,  line width
# plt.plot(y, color = 'r', linewidth = '20.5')



# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(y1)
# plt.plot(y2)

# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(x1, y1, x2, y2)


#title and lable
# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}
# plt.title("Sports Watch Data", fontdict = font1, loc = 'left')
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)


#grid
# plt.grid()
# plt.grid(axis = 'x')
# plt.grid(axis = 'y')
# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)



##subplot
#plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title("SALES")
# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.title("INCOME")
# plt.suptitle("MY SHOP")



#scatter
# plt.scatter(x, y)
# plt.scatter(x, y, color = 'hotpink')
# colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
# plt.scatter(x, y, c=colors)  #coloer for each dot
# plt.colorbar()
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
# plt.scatter(x, y, s=sizes)
# plt.scatter(x, y, s=sizes,alpha=0.2)
# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')


#bar
# plt.bar(x,y)
# plt.barh(x, y)
# plt.bar(x, y, color = "red",width=0.5)
# plt.barh(x, y, color = "red", height = 0.1)


#hist
# x = np.random.normal(170, 10, 250)
# plt.hist(x)


#pie
# plt.pie(y)
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y, labels = mylabels)
# plt.pie(y, labels = mylabels, startangle = 90)
# myexplode = [0.2, 0, 0, 0]
# plt.pie(y, labels = mylabels, explode = myexplode)
# plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# mycolors = ["black", "hotpink", "b", "#4CAF50"]
# plt.pie(y, labels = mylabels, colors = mycolors)
# plt.legend()
# plt.legend(title = "Four Fruits:")





plt.show()

