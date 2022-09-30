import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def find_diff_between_images(img1, img2):
    """
    This function finds the similarity
    between two images with same shape.

    :param img1:
    :param img2:
    :return: Normalized difference between images
    """
    try:
        img1_to_gray = rgb2gray(img1)
        img2_to_gray = rgb2gray(img2)
        (score, diff_between_images) = structural_similarity(img1_to_gray, img2_to_gray, full=True)
        print('Similarity between images:', score)
        normalized_diff_between_images = (diff_between_images + np.min(diff_between_images)) / (
                np.max(diff_between_images) + np.min(diff_between_images))
        return normalized_diff_between_images
    except ValueError:
        print(f'Image_1 shape: {img1.shape}\nImage_2 shape: {img2.shape}')
        print('Error: Images with different shapes!\nSpecify 2 images with the same shape.')


def hist_transfer(img1, img2):
    """
    This function returns the histogram
    of the correspondence between two images.
    :param img1:
    :param img2:
    :return: Matched histogram
    """
    matched_img_hist = match_histograms(img1, img2, channel_axis=-1)
    return matched_img_hist

