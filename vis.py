import cv2

fn = 'test2.png'
img = cv2.imread(fn)
img = img * 255
cv2.imwrite(fn, img)
