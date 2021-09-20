import numpy as np
import cv2

img = cv2.imread('./Assets/imagen.jpg')

cv2.imshow('Imagem',img)
cv2.waitKey(0)
cv2.destroyAllWindows()