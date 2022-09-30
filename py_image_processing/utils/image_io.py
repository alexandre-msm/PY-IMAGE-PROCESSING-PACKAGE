from skimage.io import imread, imsave


def read_image(path, is_gray=False):
    """
    This function reads an image of the specified path.
    :param path:
    :param is_gray:False
    :return: image
    """
    img = imread(path, as_gray=is_gray)
    return img


def save_image(img, path):
    """
    This function saves the image to the specified path.
    :param img:
    :param path:
    :return: None
    """
    imsave(path, img)

