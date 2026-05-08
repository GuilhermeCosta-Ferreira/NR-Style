# ================================================================
# 0. Section: IMPORTS
# ================================================================
import numpy as np

from matplotlib.lines import Line2D
from matplotlib.axes import Axes



# ================================================================
# 1. Section: Functions
# ================================================================
def nice_legend(ax: Axes, colors: list, group_names: list | np.ndarray) -> Axes:
    # A. Assert both have the same shape
    if(len(colors) != len(group_names)):
        raise ValueError(
            "There are a different number of colors than groups"
            f"Colors ({len(colors)}) {colors}"
            f"Groups ({len(group_names)}) {group_names}"
        )

    # 1. Build the handles
    legend_handles = build_handels(colors, group_names)

    # 2. Builds the legend box and places it
    ax.legend(
        handles=legend_handles,
        loc='upper center',
        bbox_to_anchor=(0.5, -0.10),
        ncol=2,
        frameon=False,
        handlelength=0.8,
        handletextpad=0.5,
        columnspacing=1.5,
        fontsize=16
    )

    return ax


# ──────────────────────────────────────────────────────
# 1.1 Subsection: Helper Functions
# ──────────────────────────────────────────────────────
def build_handels(colors: list, group_names: list | np.ndarray) -> list:
    handles = []
    for idx, color in enumerate(colors):
        label_name = 'Control' if idx == 0 else f"{group_names[idx]}"
        handles.append(Line2D([0], [0], marker='o', linestyle='None',
                    markerfacecolor=color, markeredgecolor=color,
                    markersize=14, label=label_name)
        )

    return handles
