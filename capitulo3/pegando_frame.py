import cv2

capitura = cv2.VideoCapture('./Assets/vouembora.mp4')

while True:
  ret, frame = capitura.read()
  cv2.imshow("Frame", frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

capitura.release()
cv2.destroyAllWindows()
