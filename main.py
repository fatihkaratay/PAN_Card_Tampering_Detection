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

# changing the image size and format
original = original.resize((250, 160))
print(original.size)
original.save('venv/pan_card_tampering/image/original.png')

tampered = tampered.resize((250, 160))
print(tampered.size)
original.save('venv/pan_card_tampering/image/tampered.png')

# Change image type if required from png to jpg
tampered = Image.open('venv/pan_card_tampering/image/tampered.png')
tampered.save('venv/pan_card_tampering/image/tampered.png')

original.show()
tampered.show()

# load the two images to cv2
original = cv2.imread('venv/pan_card_tampering/image/original.png')
tampered = cv2.imread('venv/pan_card_tampering/image/tampered.png')

# convert these images to the grayscale format
original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
tampered_gray = cv2.cvtColor(tampered, cv2.COLOR_BGR2GRAY)

# computing the structural similarities
(score, diff) = structural_similarity(original_gray, tampered_gray, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))
