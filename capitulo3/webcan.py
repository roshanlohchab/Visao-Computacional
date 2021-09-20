import cv2

capitura = cv2.VideoCapture(0)

while True:
  ft, frame = capitura.read()
  cv2.imshow("Cam", frame)
  if cv2.waitKey(1) & 0xff == ord('q'):
    break
capitura.release()
cv2.destroyAllWindows()