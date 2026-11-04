import numpy as np
from PIL import Image
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


def load_image(path):
    """Load an image from a path relative to the project root."""
    return np.array(Image.open(BASE_DIR / path).convert("RGB"))
