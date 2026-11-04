from part1_image_processing.gaussian import gaussian_filter, gaussian_kernel
import numpy as np


def upsample_nearest(image):
    height, width = image.shape[:2]

    new_height = height * 2
    new_width = width * 2

    upsampled = np.zeros(
        (new_height, new_width) + image.shape[2:],
        dtype=image.dtype
    )

    for y in range(new_height):
        for x in range(new_width):
            original_y = y // 2
            original_x = x // 2
            upsampled[y, x] = image[original_y, original_x]

    return upsampled


def upsample_bilinear(image):
    height, width = image.shape[:2]

    new_height = height * 2
    new_width = width * 2

    image_float = image.astype(np.float64)

    upsampled = np.zeros(
        (new_height, new_width) + image.shape[2:],
        dtype=np.float64
    )

    for y in range(new_height):
        for x in range(new_width):
            original_y = y / 2.0
            original_x = x / 2.0

            y1 = int(np.floor(original_y))
            x1 = int(np.floor(original_x))

            y2 = min(y1 + 1, height - 1)
            x2 = min(x1 + 1, width - 1)

            dy = original_y - y1
            dx = original_x - x1

            top_left = image_float[y1, x1]
            top_right = image_float[y1, x2]
            bottom_left = image_float[y2, x1]
            bottom_right = image_float[y2, x2]

            top = top_left * (1 - dx) + top_right * dx
            bottom = bottom_left * (1 - dx) + bottom_right * dx

            upsampled[y, x] = top * (1 - dy) + bottom * dy

    return np.clip(upsampled, 0, 255).astype(image.dtype)


def downsample(image, sigma=1.0, kernel_size=3):
    kernel = gaussian_kernel(sigma, kernel_size)
    blurred = gaussian_filter(image, kernel)
    # gaussian_filter works in float64; restore original dtype so matplotlib
    # displays colours correctly (float arrays must be in [0.0, 1.0])
    blurred = np.clip(blurred, 0, 255).astype(image.dtype)
    return blurred[::2, ::2]

def downsample_without_filter(image):
    return image[::2, ::2]