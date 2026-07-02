from PIL import Image

img = Image.open('icon.png').convert('RGB')
width, height = img.size
pixels = img.load()

# Define what a "background" pixel looks like.
# Usually it's either white (255, 255, 255) or light grey (e.g. > 150, 150, 150) and r~=g~=b.
def is_bg(r, g, b):
    # Check if pixel is grey/white (r, g, b are close to each other)
    diff = max(r, g, b) - min(r, g, b)
    # Check if it's light enough
    return diff < 15 and max(r, g, b) > 150

min_x, min_y = width, height
max_x, max_y = 0, 0

for y in range(height):
    for x in range(width):
        if not is_bg(*pixels[x, y]):
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

print(f"Crop box: {min_x}, {min_y}, {max_x}, {max_y}")

cropped = img.crop((min_x, min_y, max_x + 1, max_y + 1))
cropped.save('icon.png')
