from PIL import Image

from os import listdir

area = (1, 920, 1920, 1070)  # область, которую нужно вырезать

files = listdir("/Users/nahshon/PycharmProjects/Subtitles/data/")

mytxt = filter(lambda x: x.endswith('.jpg'), files)

for i in mytxt:
    counter = 0
    new_filename = '/Users/nahshon/PycharmProjects/Subtitles/cropped_data/' + i
    image_name = '/Users/nahshon/PycharmProjects/Subtitles/data/' + i
    img = Image.open(image_name)
    cropped_image = img.crop(area)
    cropped_image.save(new_filename)
    counter += 1
    print(i)
