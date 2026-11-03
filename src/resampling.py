from src.gaussian import gaussian_filter, gaussian_kernel

def upsample_nearest(image):
    pass

def upsample_bilinear(image):
    pass

def downsample(image, sigma=1.0):
    kernel = gaussian_kernel(sigma)
    blurred = gaussian_filter(image, kernel)
    return blurred[::2, ::2]