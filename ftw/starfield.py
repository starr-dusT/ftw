import numpy as np
from PIL import Image, ImageDraw
import random
import math

def create_star_field(image_size=(2560, 1440), num_stars=200, cluster_ratio_range=(0.2, 0.5), num_clusters_range=(3, 10), cluster_size_range=(20, 60), cluster_elongation_range=(1, 3)):
    # Randomize the cluster ratio and number of clusters within the given ranges
    cluster_ratio = random.uniform(*cluster_ratio_range)
    num_clusters = random.randint(*num_clusters_range)

    print(f"Cluster ratio: {cluster_ratio:.2f}, Number of clusters: {num_clusters}")
    
    # Create a transparent background
    image = Image.new("RGBA", image_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Number of stars that belong to clusters
    num_cluster_stars = int(num_stars * cluster_ratio)
    num_random_stars = num_stars - num_cluster_stars
    
    # Generate random cluster centers and assign a spread and elongation to each cluster
    cluster_centers = []
    cluster_sizes = []
    cluster_rotations = []
    
    for _ in range(num_clusters):
        center = (random.randint(50, image_size[0] - 50), random.randint(50, image_size[1] - 50))
        size_x = random.uniform(*cluster_size_range)  # Spread size in the x direction
        size_y = size_x / random.uniform(*cluster_elongation_range)  # Elongate the y-axis
        rotation_angle = random.uniform(0, 2 * math.pi)  # Random rotation angle for each cluster
        
        cluster_centers.append(center)
        cluster_sizes.append((size_x, size_y))  # Tuple for separate x and y sizes
        cluster_rotations.append(rotation_angle)  # Save the rotation for later use
    
    # Draw stars in clusters with misshapen forms
    for _ in range(num_cluster_stars):
        # Select a random cluster center and its corresponding spread size and rotation
        idx = random.randint(0, num_clusters - 1)
        cluster_x, cluster_y = cluster_centers[idx]
        size_x, size_y = cluster_sizes[idx]
        rotation_angle = cluster_rotations[idx]
        
        # Generate a random point in the elongated cluster space
        offset_x = random.gauss(0, size_x)
        offset_y = random.gauss(0, size_y)
        
        # Apply rotation to the offset to make the cluster randomly oriented
        rotated_x = offset_x * math.cos(rotation_angle) - offset_y * math.sin(rotation_angle)
        rotated_y = offset_x * math.sin(rotation_angle) + offset_y * math.cos(rotation_angle)
        
        x = int(cluster_x + rotated_x)
        y = int(cluster_y + rotated_y)
        
        # Make sure the star is within bounds
        if 0 <= x < image_size[0] and 0 <= y < image_size[1]:
            draw_star(draw, x, y)

    # Draw uniformly random stars
    for _ in range(num_random_stars):
        x = random.randint(0, image_size[0] - 1)
        y = random.randint(0, image_size[1] - 1)
        draw_star(draw, x, y)
    
    return image

def draw_star(draw, x, y):
    """Helper function to draw an irregular, misshaped star"""
    # Random brightness for the star (200-255 for white stars)
    brightness = random.randint(200, 255)

    # Generate random size for the star to create misshaping effect
    width = random.randint(1, 3)
    height = random.randint(1, 3)

    x_offset = random.randint(-1, 1)
    y_offset = random.randint(-1, 1)

    # Draw an irregular ellipse (misshapen star)
    draw.ellipse((x + x_offset, y + y_offset, x + width, y + height), fill=(brightness, brightness, brightness, 255))

# Create the star field image
star_field_image = create_star_field(num_stars=100, cluster_ratio_range=(0.4, 0.6), num_clusters_range=(3, 6), cluster_size_range=(5, 20), cluster_elongation_range=(1, 4))

# Save the image
star_field_image.save("star_field.png")

# Optionally, show the image
star_field_image.show()
