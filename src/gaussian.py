from scipy.signal import convolve2d
import numpy as np


def gaussian_kernel(kernel_size, sigma):
    center = kernel_size // 2

    # Create coordinate values
    x = np.arange(-center, center + 1)
    y = np.arange(-center, center + 1)

    # Create coordinate grid
    X, Y = np.meshgrid(x, y)

    # Calculate Gaussian values
    gaussian = (1 / (2 * np.pi * sigma**2)) * np.exp(
        -(X**2 + Y**2) / (2 * sigma**2)
    )

    # Normalize the kernel
    kernel = gaussian / np.sum(gaussian)

    return kernel


def gaussian_filter(image, kernel):
    pass

