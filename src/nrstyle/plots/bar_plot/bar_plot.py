# ================================================================
# 0. Section: IMPORTS
# ================================================================
import numpy as np
from matplotlib import pyplot as plt

from matplotlib.axes import Axes
from matplotlib.figure import Figure

from ..features import nice_legend
from ..PlotSettings import PlotSettings
from .bar_helpers import add_bars, get_y_axis, assert_same_keys



# ================================================================
# 1. Section: Functions
# ================================================================
def two_group_bar_plot(
    group_1_dict: dict,
    group_2_dict: dict,
    group_names: list[str] | np.ndarray,
    plt_settings: PlotSettings = PlotSettings(),
) -> tuple[Figure, Axes]:
    # 1. Make sure both groups have the same keys, if not just print a warning
    assert_same_keys(group_1_dict, group_2_dict)

    # 2. Builds a dict better suited for this
    sub_groups = sorted(group_1_dict.keys() | group_2_dict.keys())
    data_dict = build_data_dict(group_names, group_1_dict, group_2_dict, sub_groups)

    # 3. Define the group positioning
    x = np.arange(len(sub_groups))

    # 4. Initialize and fill the plot
    fig, ax = plt.subplots(layout='constrained', figsize=plt_settings.fig_size)

    # 5. Get sub-group bar positions and parameters
    add_bars(data_dict, ax, x, plt_settings)

    # 6. Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_title(plt_settings.title)
    ax.set_aspect("auto")

    # 7. Define the Y lim and its ticks
    ax = get_y_axis(ax, data_dict, plt_settings)

    # 8. Define the X lim and its ticks
    ax.set_xticks(x + (plt_settings.width + plt_settings.gap)/2, sub_groups)
    ax.set_xlim(-plt_settings.width, len(sub_groups) - 1 + plt_settings.width * 2 + plt_settings.gap)
    ax.tick_params(axis='x', length=0)
    ax.spines["bottom"].set_visible(False)

    # 9. Builds the legend for better visualization
    if plt_settings.show_legend:
        ax = nice_legend(ax, plt_settings.colors, group_names)

    return fig, ax



# ──────────────────────────────────────────────────────
# 1.1 Subsection: Helper Functions
# ──────────────────────────────────────────────────────
def build_data_dict(
    group_names: list[str] | np.ndarray | tuple,
    dict_1: dict,
    dict_2: dict,
    sub_groups: list[str]
) -> dict:
    return {
            group_names[0]: [dict_1.get(sub_group, np.nan) for sub_group in sub_groups],
            group_names[1]: [dict_2.get(sub_group, np.nan) for sub_group in sub_groups],
        }
