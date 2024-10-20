from wand.image import Image
from wand.color import Color

def create_blank(image_size, hex_color):
    width, height = image_size
    # Create a blank image with the specified size and color
    return Image(width=width, height=height, background=Color(hex_color))
