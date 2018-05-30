from PIL import Image
import numpy as np

def convertToArray(pixels):
    return np.array(pixels, dtype = np.uint8)

def writeToBMP(pixels, size, filename):
    array  = convertToArray(pixels)
    image = Image.Image()
    image = Image.fromarray(array)

    image.save(filename, 'BMP')

    return None
