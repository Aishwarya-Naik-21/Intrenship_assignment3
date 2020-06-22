import numpy as np
import cv2

n = int(input("Enter canvas size in pixel ( multiple of 8 ): "))
b = int(n/8)
print(b)

checkerboard = np.zeros([n,n],dtype = 'uint8')
s = b
k = b* 2

for j in range(s,n,k):
        for i in range(s,n,k):
                checkerboard[j-s:j,i-s:i] = 255
                checkerboard[j:j+s,i:i+s] = 255
        
cv2.imshow('Checkboard 8*8',checkerboard)
cv2.waitKey(0)
cv2.destroyAllWindows()
