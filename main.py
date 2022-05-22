# import all the necessary packages
from skimage.metrics import structural_similarity   # finding the similarities
import imutils                                      # drawing the contours
import cv2                                          # computer vision
from PIL import Image                               # downloading, visualizing the image
import requests                                     # getting requests from URLs. We use this to get images from user.


# loading/downloading the images from the internet. using requests
original = Image.open(requests.get('https://www.thestatesman.com/wp-content/uploads/2019/07/pan-card.jpg', stream=True).raw)
tampered = Image.open(requests.get('https://assets1.cleartax-cdn.com/s/img/20170526124335/Pan4.png', stream=True).raw)

# displaying some information to make sure the images are properly downloaded.
print("original image size:", original.size)
print("tampered image size:", tampered.size)

print("original image format:", original.format)
print("tampered image format:", tampered.format)