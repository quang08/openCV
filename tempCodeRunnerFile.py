cv2.imshow("Original Image", img)

# #Image saturation
# img_100 = np.ones(img.shape, dtype = 'uint8') * 100
# img2 = cv2.add(img, img_100) #brightened
# # img2 = cv2.subtract(img, img_100) #darkened


# #Image blending



# cv2.imshow("Brightened Image", img2)

# cv2.waitKey(0)
# cv2.destroyAllWindows()