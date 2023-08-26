import cv2
import numpy as np

img = cv2.imread("/Users/quangnguyenthe/Desktop/Academics/ImageProcessing/First/.openCVenv/imgs/simple.png", 0)

cv2.imshow("Original Image", img)


# *************************Image saturation*************************
#basic method:
img_100 = np.ones(img.shape, dtype = 'uint8') * 100 # create an image mask that will be added to the original image to adjust its saturation. By adding this mask, each pixel value in the original image will be increased by 100

img2 = cv2.add(img, img_100) #brightened
img2 = cv2.subtract(img, img_100) #darkened
#nested loop method: 
h,w = img.shape
i = 0
while i < h:
    j = 0
    while j < w:
        img[i, j] -= 50
        if img[i, j] < 0:
            img[i, j] = 0
        j += 1
    i += 1
cv2.imshow("Darkened Image", img)



# *************************Image blending: g(x)=(1−α)f0(x)+α.f1(x) or g(x)=α.f0(x)+β.f1(x)+γ *************************
# # image1 = cv2.imread('images/img1.jpg') 
# # image2 = cv2.imread('images/img2.jpg')

# weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0) #α = 0.5, β = 0.4, γ = 0
# cv2.imshow('Weighted Image', weightedSum)


# cv2.imshow("Brightened Image", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()