#from starfield import create_star_field
#
## Create the star field image
#star_field_image = create_star_field(num_stars=100, cluster_ratio_range=(0.7, 0.8), num_clusters_range=(3, 8), cluster_size_range=(5, 10), cluster_elongation_range=(1, 4))
#
## Save the image
#star_field_image.save("star_field.png")
#
## Optionally, show the image
#star_field_image.show()

#from wand.image import Image
#from wand.color import Color
#
## Load the three images
#with Image(filename='blank.png') as img1, \
#     Image(filename='star_field.png') as img2, \
#     Image(filename='kestrel.png') as img3:
#
#    # Find the max dimensions among the three images for the canvas size
#    max_width = max(img1.width, img2.width, img3.width)
#    max_height = max(img1.height, img2.height, img3.height)
#    
#    # Create an empty canvas with a transparent background, large enough to fit all images
#    with Image(width=max_width, height=max_height, background=Color('transparent')) as canvas:
#        
#        # Composite the first image at the center of the canvas
#        canvas.composite(img1, left=(max_width - img1.width) // 2, top=(max_height - img1.height) // 2)
#        
#        # Composite the second image at the center of the canvas
#        canvas.composite(img2, left=(max_width - img2.width) // 2, top=(max_height - img2.height) // 2)
#        
#        # Composite the third image at the center of the canvas
#        canvas.composite(img3, left=(max_width - img3.width) // 2, top=(max_height - img3.height) // 2)
#        
#        # Save the final result
#        canvas.save(filename='output_image.png')

def main():
    print("test")
