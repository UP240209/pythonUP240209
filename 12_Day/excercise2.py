import random

#1
def list_of_hexa_colors(n):
    hex_colors = []
    for _ in range(n):
        hex_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        hex_colors.append(hex_color)
    return hex_colors

#2
def list_of_rgb_colors(n):
    rgb_colors = []
    for _ in range(n):
        rgb_color = f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'
        rgb_colors.append(rgb_color)
    return rgb_colors

#3
def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        raise ValueError("Invalid color type. Please choose 'hexa' or 'rgb'.")

  