import cv2
import os

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

    # if not created then raise error
except OSError:
    print('Error: Creating directory of data')

cam = cv2.VideoCapture('/Users/nahshon/Downloads/data/1.mp4')
total_frames = cam.get(cv2.CAP_PROP_FRAME_COUNT)
abra = int(total_frames)
print(abra)

currentframe = 1
while True:
    cam.set(cv2.CAP_PROP_POS_MSEC, (currentframe * 2200))
    rat, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if rat:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images

        cv2.imwrite(name, gray)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

cam.release()
cv2.destroyAllWindows()
