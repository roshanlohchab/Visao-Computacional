import cv2

imagem = cv2.imread('./Assets/imagen1.png')
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(imagem)

cv2.imshow("Hue", hue)
cv2.imshow("Saturation", saturation)
cv2.imshow("Value", value)

imagem = cv2.merge((hue, saturation, value))
imagem = cv2.cvtColor(imagem, cv2.COLOR_HSV2BGR)

cv2.imshow("Original", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()