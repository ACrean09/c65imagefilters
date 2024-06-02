# Importing Library
import numpy as np
import cv2

# Define the input and output paths
imputpath = "converted/lion.png"

# Load the color image
originalimage = cv2.imread(imputpath)

# ------------Convert image to Grayscale --------------

# Convert the color image to grayscale image
#greyscaleimage = cv2.cvtColor(originalimage, cv2.COLOR_BGR2GRAY)
oilImg = cv2.xphoto.oilPainting(originalimage, size = 7, dynRatio = 1)
# Save the color image to disk
# Uncomment the below lines
outputpath = "converted/oilpainting.png"
cv2.imwrite(outputpath, oilImg)
# outputPath = 'converted/grayScale.png'
# cv2.imwrite(outputPath, grayscaleImage)


# Display the converted image
cv2.imshow("oilpainting", oilImg)
cv2.waitKey(0)

# Display a message indicating that the image has been saved
# Uncomment the below lines
print('Converted Grayscale image saved to disk : ' + outputpath)
