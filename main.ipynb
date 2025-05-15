import cv2
import numpy as np


image = cv2.imread('reference.jpg')
image = cv2.resize(image, (640, 480))  


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

_, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)


contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


for contour in contours:
    area = cv2.contourArea(contour)
    if area > 500: 
        x, y, w, h = cv2.boundingRect(contour)
     
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
      
        cv2.putText(image, "Product", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


cv2.imshow("Detected Shelf Products", image)
cv2.imshow("Thresholded Image", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
