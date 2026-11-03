import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from src.gaussian import gaussian_filter, gaussian_kernel

def load_image():
    image = np.array(Image.open("images/cat.png").convert("RGB"))

    print("Image shape:", image.shape)
    print("Image data type:", image.dtype)
    print("Minimum intensity:", image.min())
    print("Maximum intensity:", image.max())

    import numpy as np




kernel = gaussian_kernel(3, 1.0)

print(kernel)
print("Kernel sum:", np.sum(kernel))