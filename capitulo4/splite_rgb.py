import cv2

imagem = cv2.imread('./Assets/imagen1.png')

#separa as imagens em cores
blue, green, red =  cv2.split(imagem)

cv2.imshow("red", red)
cv2.imshow("green", green)
cv2.imshow("blue", blue)

#salva as imagens em disco
cv2.imwrite('./Assets/ImagesCapitulo4/imagenRed.png', red)
cv2.imwrite('./Assets/ImagesCapitulo4/imagenBlue.png', blue)
cv2.imwrite('./Assets/ImagesCapitulo4/imagenGreen.png', green)

#junta as cores novamente
imagemMerge = cv2.merge((blue,green,red))

cv2.imshow("Original", imagemMerge)

#convetendo em tons de cinza
cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

cv2.imshow("Cinza", cinza)

cv2.waitKey(0)
cv2.destroyAllWindows()