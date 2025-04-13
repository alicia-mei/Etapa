import cv2 #openCV lib

camera = cv2.VideoCapture(0) #opens camera

while cv2.waitKey(1) == -1: #loop finishes when a key is pressed
    status, imagem = camera.read() #captures image
    cv2.imshow("image", imagem) #shows captured image 
    print(status)
camera.release() #frees camera
cv2.destroyAllWindows() #closes the window
