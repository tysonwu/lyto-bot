import pyautogui
from collections import Counter
import time
import PIL.ImageGrab as ImageGrab

pyautogui.FAILSAFE = True

# specify game window, the square cropping out the main game area------
# do not leave too many margin outside the colored circles
AREA = (132, 977, 868, 1713)
#----------------------------------------------------------------------

def click(coord): # input a coord tuple (x,y)
    pyautogui.moveTo(coord[0], coord[1], duration=0.01)
#     screen_size = pyautogui.size()
    pyautogui.click(button='left')


def locate():
    box = ImageGrab.grab(AREA)
    h, w = box.size
#     print(h,w)
    pixel = list(box.getdata())
    counter = Counter(pixel)
    common = counter.most_common(3)
    pick = common[-1][0]

    location = None
    for i, pixel in enumerate(pixel):
        if pixel == pick:
            location = i

    coord_x = location % w
    coord_y = location // w

    click_x = AREA[0] + coord_x
    click_y = AREA[1] + coord_y
    print(location % w, location // w)
    return (click_x/2, click_y/2)


def main():
    while True:
        try:
            coord = locate() # returns the tuple of pixel to click
            click(coord)
            print('clicked')
            i += 1
        except:
            print('fail')
        time.sleep(0.1)

if __name__ == "__main__":
    main()
