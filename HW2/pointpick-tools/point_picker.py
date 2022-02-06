import os
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


def pointLoad(imgpath):
    if os.path.exists(imgpath):
        img = cv2.imread(imgpath)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img
        

    else:
        print("Invalid image path")
        return


# img1, img1pts = pointLoad("image1.jpg",4)

# img2, img2pts = pointLoad("image2.jpg",4)


# left=['3.jpeg','2.jpeg','2.jpeg','1.jpeg']
# right=['3.jpeg','4.jpeg','4.jpeg''5.jpeg']
# panoH={"images":[],"points":[]}
# # get points
# for image in left:
#     img1, img1pts = pointLoad(image,4)

# for image in right:
#     img1, img1pts = pointLoad(image,4)
    
# print(img1pts)
# print(img2pts)
# print(panoH)

# above is inferior to using coordaintes-checker so this program just loads in and shrinks images now =D
# image_paths=['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
# for image in image_paths:
#     img = pointLoad("../"+image)
#     cv2.resize(img, (0,0), fx=.1, fy=.1)
#     cv2.imwrite("small-"+image,img)

img = pointLoad("../1.jpg")

img = cv2.circle(img, (100,1500), radius=10, color=(0, 0, 255), thickness=-1)
img=cv2.resize(img, (0,0), fx=.25, fy=.25)
# img=cv2.resize(img, (0,0), fx=.5, fy=.5)
cv2.imshow('point',img)
cv2.waitKey(0)