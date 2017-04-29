import cv2

for filename in "negatives_images/":
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(filename, img)
