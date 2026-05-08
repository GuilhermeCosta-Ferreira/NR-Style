# ================================================================
# 0. Section: IMPORTS
# ================================================================
import numpy as np
from matplotlib import pyplot as plt

from matplotlib.figure import Figure
from matplotlib.axes import Axes



# ================================================================
# 1. Section: Functions
# ================================================================
def plot_imshow_with_labels(
    img: np.ndarray,
    points: list | np.ndarray,
    point_labels: list | np.ndarray | None = None,
    fig_size: tuple = (12,8),
    title: str = "Image with Points",
    img_cmap: str = "gray"
) -> tuple[Figure, Axes]:

    # 1. Initializes the img plot
    fig, ax = plt.subplots(layout='constrained', figsize=fig_size)
    ax.imshow(img, cmap=img_cmap)

    # 2. Adds the Lables
    for idx, point in enumerate(points):
        if point_labels is not None:
            ax.scatter(point[0], point[1], label=point_labels[idx])
        else:
            ax.scatter(point[0], point[1])

    # 3. Shows labels if applicable
    if point_labels is not None:
        ax.legend(loc='upper right', ncols=1)

    # 4. Format and add title
    plt.axis('off')
    ax.set_title(title)

    return fig, ax
