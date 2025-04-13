import cv2

camera = cv2.VideoCapture(0)

while cv2.waitKey(1) == -1:
    status, imagem = camera.read()
    cv2.imshow("alguma coisa ai", imagem)
    print(status)
camera.release()
cv2.destroyAllWindows()
