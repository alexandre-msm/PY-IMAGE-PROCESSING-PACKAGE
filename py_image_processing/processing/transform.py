from skimage.transform import resize


def resize_img(img, proportion):
    """
    This function returns the resized image
    through a proportionality factor (0 <= proportion <= 1)
    :param img:
    :param proportion:
    :return: resized image
    """
    try:
        assert 0 <= proportion <= 1
        height = round(img.shape[0] * proportion)
        width = round(img.shape[1] * proportion)
        resized_img = resize(img, (height, width), anti_aliasing=True)
        return resized_img
    except AssertionError:
        print('Error: Specify a valid proportion between 0 and 1.')
