from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image_path = 'monke.jpg'
image = Image.open(image_path)

# Calculate the size of the boxes 
dpi = 300
box_size = 1 * dpi  

# Create a new image 
bg_image = Image.new('RGB', (11 * dpi, 14 * dpi), 'white')
bg_w, bg_h = bg_image.size

# Paste the uploaded image 
img_w, img_h = image.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
bg_image.paste(image, offset)

# Draw the grid
draw = ImageDraw.Draw(bg_image)
for x in range(0, bg_w, int(box_size)):
    line = ((x, 0), (x, bg_h))
    draw.line(line, fill='white')

for y in range(0, bg_h, int(box_size)):
    line = ((0, y), (bg_w, y))
    draw.line(line, fill='white')


# Convert to numpy array for matplotlib
np_image = np.array(bg_image)

# Plot the image with grid
plt.figure(figsize=(11, 14))
plt.imshow(np_image)
plt.axis('off')  # Hide axis
plt.show()

# Save the new image with the grid as a JPEG file
output_path = 'monke_with_grid_white.jpg'
bg_image.save(output_path, 'JPEG')


# Return the path to the new image file
output_path