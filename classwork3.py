import cv2 as cv
import random

img = cv.imread('atom.png', cv.IMREAD_GRAYSCALE)

density_salt = 0.1
density_pepper = 0.1

# Set number of white pixels (salt)
number_of_white_pixel = int(density_salt * (img.shape[0] * img.shape[1]))

# Add salt to the image
for i in range(number_of_white_pixel):
    y_coord = random.randint(0, img.shape[0] - 1)
    x_coord = random.randint(0, img.shape[1] - 1)
    img[y_coord][x_coord] = 255

# Set number of black pixels (pepper)
number_of_black_pixel = int(density_pepper * (img.shape[0] * img.shape[1]))

# Add pepper to the image
for i in range(number_of_black_pixel):
    y_coord = random.randint(0, img.shape[0] - 1)
    x_coord = random.randint(0, img.shape[1] - 1)
    img[y_coord][x_coord] = 0

# Apply median filter to reduce noise
filtered_img = cv.medianBlur(img, 5)
cv.imwrite('atom clean.png',filtered_img)

# check picture
noise_not_remove = filtered_img - img
cv.imwrite('check_picture.png',noise_not_remove)
