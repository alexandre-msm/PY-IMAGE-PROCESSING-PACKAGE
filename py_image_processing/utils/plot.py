import matplotlib.pyplot as plt
import numpy as np


def plot_image(img):
    """
    This function plots the image
    using the pyplot module of the matplotlib package.
    :param img:
    :return: None
    """
    plt.figure(figsize=(12, 4))
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()


def plot_gray_image(img):
    """
    This function plots the grayscale image
    using the plot_image() function.
    :param img:
    :return: None
    """
    grey_vals = np.array([0.2126, 0.7152, 0.0722])
    s_rgb_array = img / 255
    img_gray = s_rgb_array @ grey_vals
    plot_image(img_gray)


def plot_multi_images(*args):
    """
    This function plots multiple images in the same window.
    :param args: (e.g. img1, img2, img3)
    :return: None
    """
    num_of_img = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=num_of_img, figsize=(12, 4))
    for ax, img in zip(axis, args):
        ax.imshow(img, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()


def plot_hist(img):
    """
    This function plots the histogram of the image.
    :param img:
    :return: None
    """
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex='all', sharey='all')
    color_lst = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title(f'{color.title()} histogram')
        ax.hist(img[:, :, index].ravel(), bins=256, color=color, alpha=0.8)
    fig.tight_layout()
    plt.show()
