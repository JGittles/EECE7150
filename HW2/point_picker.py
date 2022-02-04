import os
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt



def pointLoad(imgpath,pts):
    if os.path.exists(imgpath):
        img = cv2.imread(imgpath)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ptMatrix = plt.ginput(pts)
        plt.close()
        return img, np.array(ptMatrix).astype(int)
        

    else:
        print("Invalid image path")
        return


img1, img1pts = pointLoad("image1.jpg",4)

img2, img2pts = pointLoad("image2.jpg",4)


left=['s1.jpeg','s4.jpeg']
right=['s1.jpeg','s5.jpeg']
panoH={"images":[],"points":[]}
# get points
for image in left:
    img1, img1pts = pointLoad(image,4)

for image in right:
    img1, img1pts = pointLoad(image,4)
    
print(img1pts)
print(img2pts)
print(panoH)
