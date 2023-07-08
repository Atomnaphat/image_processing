import numpy as np
import cv2 as cv


image_width = 32
image_height = 32
line_color = (255, 255, 255)
image = np.zeros((image_height, image_width, 3), dtype=np.uint8)


start_point = (0, 10)
end_point = (20, 30)
line_thickness = 1


cv.line(image, start_point, end_point, line_color, line_thickness)


cv.imwrite("picture_line.png", image)


image_path = "kanti.jpg"
original_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)


line_filter_image = cv.imread("picture_line.png", cv.IMREAD_GRAYSCALE)


line_filter_sum = line_filter_image.sum()
line_filter_image = line_filter_image / line_filter_sum


output_image = cv.filter2D(src=original_image, ddepth=-1, kernel=line_filter_image)


cv.imwrite("output_image.png", output_image)
cv.destroyAllWindows()
