# for 1401. Circle and Rectangle Overlapping
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

radius = 1
xCenter = 5
yCenter = -2
x1 = 0; y1 = 0; x2 = 10; y2 = 2
# www.geeksforgeeks.org/how-to-draw-a-circle-using-matplotlib-in-python/
# https://www.codecamp.ru/blog/matplotlib-rectangle/
# https://www.geeksforgeeks.org/how-to-set-the-x-and-the-y-limit-in-matplotlib-with-python/

figure, axes = plt.subplots()
Drawing_uncolored_circle = plt.Circle((0.6, 0.6), 0.2,  fill = False)
plt.grid()
axes.add_patch (Rectangle((x1, y1), abs(x1-x2), abs(y1-y2),
                          edgecolor = 'darkgreen', facecolor = 'blue',fill= True ))
plt.xlim(min(x1,x2,xCenter)-5, max(x1,x2,xCenter)+5)
plt.ylim(min(y1,y2,yCenter)-5, max(y1,y2,xCenter)+5)
axes.set_aspect(1)
axes.add_artist(Drawing_uncolored_circle)
# plt.title('Colored Circle')
plt.show()