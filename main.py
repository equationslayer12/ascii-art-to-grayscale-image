from PIL import Image

ASCII_ART_FILE_NAME = "art.txt"
NEW_IMAGE_NAME = "new_image.png"

CHARACTER_REPRESENTATION_IN_GRAYSCALE = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
CHARACTER_REPRESENTATION_IN_GRAYSCALE_LENGTH = len(CHARACTER_REPRESENTATION_IN_GRAYSCALE)


def letter_to_rgb(letter):
    try:
        color = int(CHARACTER_REPRESENTATION_IN_GRAYSCALE.index(letter) / CHARACTER_REPRESENTATION_IN_GRAYSCALE_LENGTH * 255)
    except ValueError:
        color = 255

    return color, color, color


def get_longest_line_from_file(file):
    width = len(max(file, key=len))
    file.seek(0)
    return width


def count_file_newlines(file):
    height = len(file.readlines())
    file.seek(0)
    return height


def convert_ascii_art_to_image_data(ascii_art_file, image_width):
    image_data = []
    for line in ascii_art_file:
        for x in line:
            image_data.append(
                letter_to_rgb(x)
            )

        fill_rest_of_line_with_white(image_data, line, image_width)
    return image_data


def fill_rest_of_line_with_white(image_data, line, image_width):
    for x in range(image_width - len(line)):
        image_data.append((255, 255, 255))


def get_file_dimentions(ascii_art_file):
    image_width = get_longest_line_from_file(ascii_art_file)
    image_height = count_file_newlines(ascii_art_file)
    return image_width, image_height


def save_image(image):
    image.save(NEW_IMAGE_NAME)


def create_image_from_data(image_data, image_width, image_height):
    image = Image.new('RGB', (image_width, image_height))
    image.putdata(image_data)
    return image


def main():
    with open(ASCII_ART_FILE_NAME, "r") as ascii_art_file:
        new_image_width, new_image_height = get_file_dimentions(ascii_art_file)
        new_image_data = convert_ascii_art_to_image_data(ascii_art_file, new_image_width)
        new_image = create_image_from_data(new_image_data, new_image_width, new_image_height)
        save_image(new_image)


if __name__ == '__main__':
    main()
