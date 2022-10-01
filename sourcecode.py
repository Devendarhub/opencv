import cv2

#read image
#img=('')
img_path= cv2.imread('nosingimage.jpg')
#display image 
bilateral = cv2.bilateralFilter(img_path,15,75,75)

cv2.imshow('newimage',bilateral)
cv2.waitKey(8000)
cv2.destroyAllWindows()