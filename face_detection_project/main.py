import cv2
print("Введите путь для файла")
photo_path=input()
model_path=cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_detector=cv2.CascadeClassifier(model_path)
image=cv2.imread(photo_path)
if image is None:
    print("файл не найден")
    exit()
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
face=face_detector.detectMultiScale(image, scaleFactor=1.2, minNeighbors=5)
#print (face)
if face is None:
    print('лицо не найдено')
    exit()
x,y,w,h=face[0]
image=cv2.rectangle(image,(x,y), (x+w,y+h), (255,0,0), 2)
cv2.imshow('image',image)
cv2.waitKey(0)