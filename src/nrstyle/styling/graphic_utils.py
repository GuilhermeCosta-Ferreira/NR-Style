# ================================================================
# 0. Section: Imports
# ================================================================
import cv2
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.colors import LinearSegmentedColormap

from .graphic_classes import AlphaColor
from .color_converter import hex2rgb



# ================================================================
# 1. Section: Background Removal
# ================================================================
def remove_color_for_background(image_path: str, output_path: str, color_threshold: int = 240):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # If the image doesn't have an alpha channel, add one
    if img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

    # Make white pixels transparent
    # Define white color threshold (accounting for near-white pixels)
    mask = np.all(img[:, :, :3] >= color_threshold, axis=2)
    img[mask, 3] = 0  # Set alpha channel to 0 (transparent) for white pixels

    # Save the image with transparency
    cv2.imwrite(output_path, img)



# ================================================================
# 2. Section: Color Manager
# ================================================================
def pick_colors(color_map: LinearSegmentedColormap, N: int) -> np.ndarray:
    return color_map(np.linspace(0, 1, N))

def transparent_to_color_cmap(ending_color: str, starting_color: str = '#FFFFFF', n_bins: int = 256) -> LinearSegmentedColormap:
    """Create a colormap transitioning from transparent to a specified color.

    Generates a `LinearSegmentedColormap` that starts with a fully transparent
    version of `starting_color` and linearly interpolates to a solid `ending_color`.

    Parameters
    ----------
    ending_color : str
        Hexadecimal color string (e.g., '#FF0000') for the solid end of the colormap.
    starting_color : str, optional
        Hexadecimal color string (e.g., '#FFFFFF') whose RGB values are used for
        the transparent start of the colormap. Defaults to '#FFFFFF' (white).
    n_bins : int, optional
        The number of discrete color steps in the colormap. Defaults to 255.

    Returns
    -------
    matplotlib.colors.LinearSegmentedColormap
        The generated colormap object.

    Notes
    -----
    The function relies on `matplotlib` for colormap creation. The starting
    point of the colormap will have the RGB values of `starting_color` but
    with an alpha value of 0, making it fully transparent.

    Examples
    --------
    >>> from matplotlib.colors import to_hex
    >>> cmap_red = transparent_to_color_cmap('#FF0000', n_bins=3)
    >>> # The colormap will have 3 colors: transparent white, a mix, and solid red.
    >>> print([to_hex(c, keep_alpha=True) for c in cmap_red.colors])
    ['#ffffff00', '#ff7f7fff', '#ff0000ff']
    >>> cmap_blue = transparent_to_color_cmap(ending_color='#0000FF')
    >>> # By default, creates a 2-step map from transparent white to the ending color.
    >>> print([to_hex(c, keep_alpha=True) for c in cmap_blue.colors])
    ['#ffffff00', '#0000ffff']
    """

    rgb_ending_color = hex2rgb(ending_color)
    rgb_starting_color = hex2rgb(starting_color)

    rgb_starting_color = (rgb_starting_color[0], rgb_starting_color[1], rgb_starting_color[2], 0)

    colors = [rgb_starting_color, rgb_ending_color]
    personal_cmap = LinearSegmentedColormap.from_list('transparent_to_red', colors, N=n_bins)

    return personal_cmap

def tri_colormap(cmap_name: str, color_1: str, color_2: str, color_3: str, n_bins: int = 256) -> LinearSegmentedColormap:

    color_1 = hex2rgb(color_1)
    color_2 = hex2rgb(color_2)
    color_3 = hex2rgb(color_3)

    colors = [color_1, color_2, color_3]
    cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

    return cmap

def bi_colormap(cmap_name: str, color_1: str, color_2: str, n_bins: int = 256) -> LinearSegmentedColormap:

    color_1 = hex2rgb(color_1)
    color_2 = hex2rgb(color_2)

    colors = [color_1, color_2]
    cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

    return cmap

def tri_alpha_colormap(color_1: AlphaColor, color_2: AlphaColor, color_3: AlphaColor, **kwargs) -> LinearSegmentedColormap:
    n_bins = kwargs.get('n_bins', 256)

    colors = [
        (color_1.r, color_1.g, color_1.b, color_1.a),
        (color_2.r, color_2.g, color_2.b, color_2.a),
        (color_3.r, color_3.g, color_3.b, color_3.a)
    ]
    cmap = LinearSegmentedColormap.from_list('tri_alpha_cmap', colors, N=n_bins)

    return cmap

def show_colormap(cmap, n=256):
    gradient = np.linspace(0, 1, n).reshape(1, -1)

    plt.figure(figsize=(6, 1.2))
    plt.imshow(gradient, aspect="auto", cmap=cmap)
    plt.axis("off")
    plt.show()
