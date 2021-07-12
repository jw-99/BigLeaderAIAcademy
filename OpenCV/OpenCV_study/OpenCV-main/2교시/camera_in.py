import sys
import cv2

# (4)
# 카메라로부터 cv2.VideoCapture 객체(클래스) 생성
# VideoCapture('파일명')
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 프레임 해상도 출력
print('Frame width:', round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 매 프레임 처리 및 화면 출력
while True:
    ret, frame = cap.read()

    if not ret:
        break

    edge = cv2.Canny(frame, 50, 150)

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)

# escape
    if cv2.waitKey(10) == 27:
        break

# 자원 해제

cap.release()
cv2.destroyAllWindows()
