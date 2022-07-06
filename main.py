from PIL import Image

gray_scale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
length = len(gray_scale)


def letter_to_rgb(letter):
    try:
        value = int(gray_scale.index(letter) / length * 255)
    except ValueError:
        value = 255

    return value, value, value


with open("art.txt", "r") as file:
    WIDTH = len(max(file, key=len))
    file.seek(0)
    HEIGHT = 0

    pixels = []
    for line in file:
        for x in line:
            pixels.append(
                letter_to_rgb(x)
            )

        for x in range(WIDTH - len(line)):
            pixels.append((255, 255, 255))

        HEIGHT += 1

    image = Image.new('RGB', (WIDTH, HEIGHT))
    image.putdata(pixels)
    image.save('new_image.png')
