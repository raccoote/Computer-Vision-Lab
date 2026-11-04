from common.image_loader import load_image
from common.visualization import show_image
from part1_image_processing.resampling import downsample, downsample_without_filter, upsample_nearest, upsample_bilinear
from common.metrics import calculate_psnr
import numpy as np
import matplotlib.pyplot as plt



def aliasing_experiment(image_name, sigma):
    img = load_image(f"data/images/{image_name}")

    no_filter = downsample_without_filter(img)
    filtered = downsample(img, sigma)

    # Display results
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    images = [img, no_filter, filtered]
    titles = [
        "Original image",
        "Downsampled without filtering",
        f"Downsampled with Gaussian filtering (σ={sigma})"
    ]

    for ax, image, title in zip(axes, images, titles):
        ax.imshow(image, cmap="gray" if image.ndim == 2 else None)
        ax.set_title(title)
        ax.axis("off")

    plt.tight_layout()
    plt.show()


def interpolation_experiment(image_name, sigma=1.0):

    # Load original image
    img = load_image(f"data/images/{image_name}")

    # Downsample by a factor of 2
    small = downsample(img, sigma=sigma)

    # Upsample using both interpolation methods
    nearest = upsample_nearest(small)
    bilinear = upsample_bilinear(small)

    # Handle odd image dimensions
    height, width = img.shape[:2]

    nearest = nearest[:height, :width]
    bilinear = bilinear[:height, :width]

    # Calculate PSNR
    psnr_nearest = calculate_psnr(img, nearest)
    psnr_bilinear = calculate_psnr(img, bilinear)

    print(f"Nearest-neighbour PSNR: {psnr_nearest:.2f} dB")
    print(f"Bilinear PSNR: {psnr_bilinear:.2f} dB")

    # Calculate pixel-wise error maps
    error_nearest = np.abs(
        img.astype(np.float64) - nearest.astype(np.float64)
    )

    error_bilinear = np.abs(
        img.astype(np.float64) - bilinear.astype(np.float64)
    )

    # Convert RGB error maps into grayscale error maps
    if error_nearest.ndim == 3:
        error_nearest = np.mean(error_nearest, axis=2)
        error_bilinear = np.mean(error_bilinear, axis=2)

    # Display results
    fig, axes = plt.subplots(2, 3, figsize=(15, 9))

    # First row: reconstructed images
    images = [img, nearest, bilinear]

    titles = [
        "Original image",
        f"Nearest-neighbour (PSNR: {psnr_nearest:.2f} dB)",
        f"Bilinear (PSNR: {psnr_bilinear:.2f} dB)"
    ]

    for ax, image, title in zip(axes[0], images, titles):
        ax.imshow(
            image,
            cmap="gray" if image.ndim == 2 else None,
            vmin=0,
            vmax=255
        )
        ax.set_title(title)
        ax.axis("off")

    # Second row: reconstruction error maps
    errors = [None, error_nearest, error_bilinear]

    error_titles = [
        "Original image",
        "Nearest-neighbour error",
        "Bilinear error"
    ]

    for ax, error, title in zip(axes[1], errors, error_titles):
        if error is None:
            ax.imshow(img, cmap="gray" if img.ndim == 2 else None)
        else:
            ax.imshow(error, cmap="hot", vmin=0)

        ax.set_title(title)
        ax.axis("off")

    plt.tight_layout()
    plt.show()
    
