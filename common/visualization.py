import matplotlib.pyplot as plt
import numpy as np


def show_image(image, title="Image", cmap=None):
    plt.figure()
    plt.title(title)
    plt.imshow(image, cmap=cmap)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def show_images(images, titles=None, cmap=None):
    n = len(images)
    titles = titles or [""] * n
    fig, axes = plt.subplots(1, n, figsize=(5 * n, 5))
    if n == 1:
        axes = [axes]
    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img, cmap=cmap)
        ax.set_title(title)
        ax.axis("off")
    plt.tight_layout()
    plt.show()
