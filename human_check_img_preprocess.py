import sys, math
import cv2
import utils

# User input from sys.argv - START:
img_path = sys.argv[1] # argument 1 is img absolute path, please refer to your 'driving_log.csv'.
steering_angle = float(sys.argv[2]) # argument 1 is steering angle.
# User input from sys.argv - END

range_x = 100
range_y = 10

"""
def show_imgs(images):
    cols = 2
    rows = math.ceil(len(images) / 2)
    fig=plt.figure()
    for index, img in enumerate(images):
        fig.add_subplot(rows, cols, index + 1)
        plt.imshow(img)
    plt.show()
"""
def show_img(img, title = ''):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_imgs(images):
    for index, img in enumerate(images):
        show_img(img)

# Preprocess for model - START:
image = utils.load_image('data', img_path)
image_flip, steering_angle = utils.random_flip(image, steering_angle)
image_translate, steering_angle = utils.random_translate(image_flip, steering_angle, range_x, range_y)
# image_shadow = utils.random_shadow(image_translate)
# image_brightness = utils.random_brightness(image_shadow)
# image_crop = utils.crop(image_brightness)
image_crop = utils.crop(image_translate)
image_resize = utils.resize(image_crop)
image_rgb2yuv = utils.rgb2yuv(image_resize)
# Preprocess for model - END

images = [
    image,
    image_flip,
    image_translate,
#     image_shadow,
#     image_brightness,
    image_crop,
    image_resize,
    image_rgb2yuv,
]

show_imgs(images)
