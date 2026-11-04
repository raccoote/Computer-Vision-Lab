from scipy.signal import convolve2d
import numpy as np


def gaussian_kernel(sigma, kernel_size=None):

    # calculate kernel size if not specified by t
    if kernel_size is None:
        kernel_size = 2 * int(np.ceil(3 * sigma)) + 1

    center = kernel_size // 2
    x = np.arange(-center, center + 1)
    y = np.arange(-center, center + 1)

    X, Y = np.meshgrid(x, y)
    gaussian = (1 / (2 * np.pi * sigma**2)) * np.exp(
        -(X**2 + Y**2) / (2 * sigma**2)
    )

    # Normalize
    kernel = gaussian / np.sum(gaussian)

    return kernel


def gaussian_filter(image, kernel):
    image = image.astype(np.float64)
    channels = []

    for c in range(image.shape[2]):
        filtered_channel = convolve2d(
            image[:, :, c],
            kernel,
            mode="same",
            boundary="symm"
        )
        channels.append(filtered_channel)

    return np.stack(channels, axis=2)
