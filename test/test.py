from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('./123.png')
#img1=img.crop((729,118,1241,374))
img = np.array(img)
img = img.transpose(1,0)#行列互换
#print(img.shape)

init_1 = np.zeros([1242,375])
init_2 = np.zeros([1242,375])
#print(init.shape)

x1 = [0,364,729,0,364,729]
y1 = [0,0,0,118,118,118]
x2 = [511,876,1241,511,876,1241]
y2 = [255,255,255,374,374,374]

length = len(x1)
for c in range(0,length):
    for x in range(x1[c],x2[c]+1):
        for y in range(y1[c],y2[c]+1):
            init_1[x][y] += 1
            init_2[x][y] = img[x][y]



print(init_1.min())
img = init_2.transpose(1,0)#行列互换
img = img/255
img = Image.fromarray(img)
img.show()
#img.save("./result_.png")
'''
for x in range(0,512):
    for y in range(0,255):
        #print('x:',x,'y:',y)
        init[x][y] = img[x][y]
'''
        


#img = img/255
#img = Image.fromarray(img)
#img_2 = numpy.array(img)



#img.show()


#plt.figure("test")
#plt.imshow(img)
#plt.show()
