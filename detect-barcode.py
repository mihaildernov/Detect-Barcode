import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

used_codes = []

camera = True

while camera == True:
    success, frame = cap.read()

    for code in decode(frame):
        if code.data.decode('utf-8') not in used_codes:
            print('Продукт найден')
            print(code.data.decode('utf-8'))
            used_codes.append(code.data.decode('utf-8'))

        elif code.data.decode('utf-8') in used_codes:
            print('Данный продукт уже был найден ранее')

        else:
            pass

    cv2.imshow('Testing-code-scan', frame)

    print(f"Распознаны следующие продукты: {used_codes}")
    print(f"Количество продуктов: {len(used_codes)}")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
