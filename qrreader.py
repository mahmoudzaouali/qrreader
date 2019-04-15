import cv2
import numpy as np
from pyzbar import pyzbar
from firebase import firebase

cap = cv2.VideoCapture(0)
img=cv2.imread("big-number.png")

firebase = firebase.FirebaseApplication('https://empedded-system-vise-project.firebaseio.com/')
result = firebase.get('/users', None)
print(result)
b = 0
while True:
    _, frame=cap.read()
    dobject=pyzbar.decode(frame)

    cv2.imshow("frame", frame)




    for barcode in dobject:

        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)


        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        if barcodeData in result:
            print('true')
            b=1
            break
        else:
            print('wrong')



    cv2.imshow("frame", frame)
    if b ==1:
        break
    key = cv2.waitKey(1)
    if key==27:
        break

print('yahooo')
cv2.destroyAllWindows()
