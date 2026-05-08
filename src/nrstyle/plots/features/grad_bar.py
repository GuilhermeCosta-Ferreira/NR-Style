# ================================================================
# 0. Section: IMPORTS
# ================================================================
import numpy as np
from matplotlib import pyplot as plt

from matplotlib.axes import Axes
from matplotlib.container import BarContainer
from matplotlib.patches import Rectangle
from matplotlib.colors import to_rgba



# ================================================================
# 1. Section: Functions
# ================================================================
def convert_rect_to_grad(rects: BarContainer, ax: Axes, measurement: list, color: str) -> BarContainer:
    for rect, h in zip(rects, measurement):
        if np.isnan(h) or h <= 0:
            continue

        add_vertical_gradient_to_bar(
            ax=ax,
            rect=rect,
            color=color,
            alpha_bottom=0.0,
            alpha_top=1.0
        )

    return rects


# ──────────────────────────────────────────────────────
# 1.1 Subsection: Helper Functions
# ──────────────────────────────────────────────────────
def add_vertical_gradient_to_bar(
    ax: Axes,
    rect: Rectangle,
    color: str,
    alpha_bottom: float = 0.0,
    alpha_top: float = 1.0
) -> None:
    # 1. Get the rect parameters
    x = rect.get_x()
    y = rect.get_y()
    w = rect.get_width()
    h = rect.get_height()

    rgba = np.array(to_rgba(color))
    gradient = np.ones((256, 1, 4))
    gradient[..., :3] = rgba[:3]

    t = np.linspace(0, 1, 256).reshape(256, 1)
    gradient[..., 3] = alpha_bottom + (alpha_top - alpha_bottom) * (t ** 0.5)

    im = ax.imshow(
        gradient,
        extent=(x, x + w, y, y + h),
        origin="lower",
        aspect="auto",
        interpolation="bicubic",
        zorder=2
    )

    im.set_clip_path(rect)
