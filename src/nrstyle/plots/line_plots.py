# ================================================================
# 0. Section: IMPORTS
# ================================================================
import numpy as np

from typing import cast
from matplotlib import pyplot as plt

from matplotlib.figure import Figure
from matplotlib.axes import Axes



# ================================================================
# 1. Section: Functions
# ================================================================
def plot_lines(
    lines_data: list | np.ndarray,
    line_labels: list | np.ndarray | None = None,
    title: str = "Lines on a Frame",
    fig_size: tuple = (8,8),
    ax: Axes | None = None,
) -> tuple[Figure, Axes]:
    # 1. Initializes the plot
    if ax is None:
        fig, ax = plt.subplots(layout='constrained', figsize=fig_size)
    else:
        fig = cast(Figure, ax.figure)

    # 2. Plot all lines
    for idx, line in enumerate(lines_data):
        if line_labels is not None:
            ax.plot(line, label=line_labels[idx])
        else:
            ax.plot(line)

    # 3. Shows labels if applicable
    if line_labels is not None:
        ax.legend(loc='upper right', ncols=1)

    # 4. Format and add title
    ax.set_title(title)

    return fig, ax
