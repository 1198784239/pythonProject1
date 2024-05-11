import cv2

raw_bag = cv2.imread('../12.jpg')
raw_huakuang =cv2.imread('../123.jpg')
#边缘图
canny_bag = cv2.Canny(raw_bag,70,200)
canny_huakuang = cv2.Canny(raw_huakuang,70,200)

res =cv2.matchTemplate(canny_bag,canny_huakuang,cv2.TM_CCOEFF_NORMED)
min_val,max_val,min_loc,max_loc =cv2.minMaxLoc(res)
x1,y1 = max_loc[0],max_loc[1]
x2,y2 = x1 +raw_huakuang.shape[1],x1 +raw_huakuang.shape[1]
cv2.rectangle(raw_bag,(x1,y1),(x2,y2),(0,0,255),2)
#展示滑块
cv2.imshow('bg',raw_bag)
#等待 防止秒
cv2.waitKey(0)