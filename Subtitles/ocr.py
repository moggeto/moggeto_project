import pytesseract
import cv2
import os
from os import listdir
from PIL import Image
import re


def count_sorting(a):
    nums = re.findall(r'\d+', a)
    nums = [int(i) for i in nums]
    return nums


files = listdir("/Users/nahshon/PycharmProjects/Subtitles/cropped_data/")

jpg_filter = filter(lambda x: x.endswith('.jpg'), files)

itog = []
# re.sub("^\s+|\n|\r|\s+$", '', itog)
for i in sorted(jpg_filter, key=count_sorting):
    img = Image.open('/Users/nahshon/PycharmProjects/Subtitles/cropped_data/' + i)
    string = pytesseract.image_to_string(img, lang='rus')
    itog.append(string)
itog_1 = set(itog)
with open('text.txt', 'w') as txt:
    for _ in itog_1:
        txt.write(_)

