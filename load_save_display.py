#!/usr/bin/env python3

import argparse
import cv2

# Handling arguments and help message for arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image from the argument and load it with cv2
# The function cv2.imread will return a numpy array that represents the image

image = cv2.imread(args["image"])

# Printing the image properties
print("height: {} pizels".format(image.shape[0]))
print("width: {} pixels".format(image.shape[1]))
print("channels: {}".format(image.shape[2]))

# Displays the image
cv2.imshow("image", image)
# Waits for any key press to unpause execution
cv2.waitKey(0)
# Save the image as jpg
cv2.imwrite("newimage.jpg", image)

