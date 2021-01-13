import cv2
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('photo.jpg')
grayscaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_cordinates = trained_face_data.detectMultiScale(grayscaled_img)
for (x,y,w,h) in face_cordinates:
    #(x,y,w,h) = face_cordinates[0]
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),10)
cv2.imshow('clever program',img)
cv2.waitKey()
print("code completed")


