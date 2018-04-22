import cv2

cap=cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()
  frame = cv2.flip(frame,1)

  # Convert color space from BGR to Gray mode.
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  cv2.imshow('frame', frame)   # show original image
  # show image with gray mode cv2.imshow('frame', gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()