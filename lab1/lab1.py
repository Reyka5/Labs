import cv2

# set paths
BW_IMG_PATH = "mnist.jpeg"
BGR_IMG_PATH = "Lenna_(test_image).png"
OUTPUT_PATH = "saved_roi.png"

# read images
bw_img = cv2.imread(BW_IMG_PATH, 0)  # 0-flag means "read greyscale"
bgr_img = cv2.imread(BGR_IMG_PATH)

# show images
cv2.imshow("Black-and-white image", bw_img)
cv2.imshow("Color image", bgr_img)

# BGR --> HSV
hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV image", hsv_img)

# show separate channels of rgb and hsv images
cv2.imshow("B", bgr_img[:, :, 0])
cv2.imshow("G", bgr_img[:, :, 1])
cv2.imshow("R", bgr_img[:, :, 2])
cv2.imshow("H", hsv_img[:, :, 0])
cv2.imshow("S", hsv_img[:, :, 1])
cv2.imshow("V", hsv_img[:, :, 2])

# press any key to stop showing images
cv2.waitKey(0)

# copy a region of interest of bw image
roi_bw = bw_img[:bw_img.shape[0]//2, :bw_img.shape[1]//2].copy()

# save roi copy
cv2.imwrite(OUTPUT_PATH, roi_bw)
