from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import random
import math

def create_star_field(image_size=(2560, 1440), num_stars=200, cluster_ratio_range=(0.2, 0.5), num_clusters_range=(3, 10), cluster_size_range=(20, 60), cluster_elongation_range=(1, 3)):
    # Randomize the cluster ratio and number of clusters within the given ranges
    cluster_ratio = random.uniform(*cluster_ratio_range)
    num_clusters = random.randint(*num_clusters_range)

    print(f"Cluster ratio: {cluster_ratio:.2f}, Number of clusters: {num_clusters}")
    
    # Create a transparent background
    image = Image(width=image_size[0], height=image_size[1], background=Color("transparent"))
    draw = Drawing()

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

    # Apply the drawing to the image
    draw(image)
    
    # Clean up the draw object
    draw.clear()
    
    return image

def draw_star(draw, x, y):
    """Helper function to draw an irregular, misshaped star"""
    # Random brightness for the star (200-255 for white stars)
    brightness = random.randint(200, 255)
    star_color = Color(f'rgba({brightness}, {brightness}, {brightness}, 1.0)')

    # Generate random size for the star to create misshaping effect
    radius_x = random.random()*2  # Horizontal radius
    radius_y = random.random()*2  # Vertical radius

    x_offset = random.random()*.5
    y_offset = random.random()*.5

    # Set the fill color for the star
    draw.fill_color = star_color

    # Draw the ellipse with the center at (x + x_offset, y + y_offset) and radii (radius_x, radius_y)
    draw.ellipse((x + x_offset, y + y_offset), (radius_x, radius_y))
