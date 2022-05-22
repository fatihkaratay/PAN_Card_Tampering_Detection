# import all the necessary packages
from skimage.metrics import structural_similarity   # finding the similarities
import imutils                                      # drawing the contours
import cv2                                          # computer vision
from PIL import Image                               # downloading, visualizing the image
import requests                                     # getting requests from URLs. We use this to get images from user.


print("module detections")