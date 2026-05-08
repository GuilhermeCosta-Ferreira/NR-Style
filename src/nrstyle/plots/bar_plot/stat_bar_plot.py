# ================================================================
# 0. Section: IMPORTS
# ================================================================
import numpy as np
from matplotlib import pyplot as plt

from matplotlib.axes import Axes
from matplotlib.figure import Figure

from ..features import nice_legend
from ..PlotSettings import PlotSettings
from .bar_helpers import add_bars, add_points, add_errorbar, get_y_axis, add_pvalue, assert_same_keys



# ================================================================
# 1. Section: Functions
# ================================================================
def two_group_stat_bar_plot(
    group_1_dict: dict[str, dict[str, list[float]]],
    group_2_dict: dict[str, dict[str, list[float]]],
    group_names: list[str] | np.ndarray,
    plt_settings: PlotSettings = PlotSettings(),
) -> tuple[Figure, Axes, dict]:
    # 1. Make sure both groups have the same keys, if not just print a warning
    assert_same_keys(group_1_dict, group_2_dict)

    # 2. Builds a dict better suited for this
    sub_groups = sorted(group_1_dict.keys() | group_2_dict.keys())
    data_dict = build_data_dict(group_names, group_1_dict, group_2_dict, sub_groups)
    g1_point_names = {k: list(v.keys()) for k, v in group_1_dict.items()}
    #g1_point_names = list(next(iter(g1_point_names.values())).keys())
    g2_point_names = {k: list(v.keys()) for k, v in group_2_dict.items()}
    #g2_point_names = list(next(iter(g1_point_names.values())).keys())
    mean_dict = build_mean_data_dict(data_dict)
    std_dict = build_std_data_dict(data_dict)

    print(group_1_dict)
    print(data_dict)
    print()
    print(g1_point_names)
    print(g2_point_names)


    # 3. Define the group positioning
    x = np.arange(len(sub_groups))

    # 4. Initialize and fill the plot
    fig, ax = plt.subplots(layout='constrained', figsize=plt_settings.fig_size)

    # 5. Get sub-group bar positions and parameters
    ax = add_bars(mean_dict, ax, x, plt_settings)
    if plt_settings.show_points:
        ax = add_points(data_dict, ax, x, plt_settings)
    if plt_settings.show_errorbar:
        ax = add_errorbar(mean_dict, std_dict, ax, x, plt_settings)
    if plt_settings.show_pvalue:
        ax = add_pvalue(data_dict, ax, x, plt_settings)

    # 6. Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_title(plt_settings.title)
    ax.set_aspect("auto")

    # 7. Define the Y lim and its ticks
    ax = get_y_axis(ax, mean_dict, plt_settings)

    # 8. Define the X lim and its ticks
    ax.set_xticks(x + (plt_settings.width + plt_settings.gap)/2, sub_groups)
    ax.set_xlim(-plt_settings.width, len(sub_groups) - 1 + plt_settings.width * 2 + plt_settings.gap)
    ax.tick_params(axis='x', length=0)
    ax.spines["bottom"].set_visible(False)

    # 9. Builds the legend for better visualization
    if plt_settings.show_legend:
        ax = nice_legend(ax, plt_settings.colors, group_names)

    return fig, ax, data_dict


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
            group_names[0]: [list(dict_1.get(sub_group, {}).values()) for sub_group in sub_groups],
            group_names[1]: [list(dict_2.get(sub_group, {}).values()) for sub_group in sub_groups],
        }

def build_mean_data_dict(data_dict: dict) -> dict:
    return {
        group_name: [float(np.nanmean(values)) for values in sub_dict]
        for group_name, sub_dict in data_dict.items()
    }

def build_std_data_dict(data_dict: dict) -> dict:
    return {
        group_name: [float(np.nanstd(values)) for values in sub_dict]
        for group_name, sub_dict in data_dict.items()
    }
