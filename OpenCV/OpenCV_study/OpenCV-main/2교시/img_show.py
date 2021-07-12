import sys
import cv2
# (2)
# 영상 불러오기
img = cv2.imread('cat.bmp')
if img is None:
    print('Image load failed!')
    sys.exit()

# 영상 화면 출력
cv2.namedWindow('image')
cv2.imshow('image', img)

# cv2.resizeWindow('image',100,100)
# cv2.moveWindow('image',15,15)

print(img)
print(type(img))
print(img.shape)
print(img.dtype)
# 다음 key 기다림
cv2.waitKey()

# 창 닫기
cv2.destroyAllWindows()
