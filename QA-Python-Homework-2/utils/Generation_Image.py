import numpy
from PIL import Image

def Generation_Image():
        return Image.fromarray((numpy.random.rand(400,240,3) * 255).astype('uint8')).convert('RGBA')