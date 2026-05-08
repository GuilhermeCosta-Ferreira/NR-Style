# ================================================================
# 0. Section: IMPORTS
# ================================================================
import numpy as np

from typing import cast
from matplotlib.axes import Axes
from scipy.stats import ttest_ind

from ..PlotSettings import PlotSettings
from ..features import convert_rect_to_grad
from ...logger import logger
from ...styling import change_lighness
from ...stats import p_to_stars



# ================================================================
# 1. Section: Generate Bars
# ================================================================
def add_bars(
    data_dict: dict,
    ax: Axes,
    x: np.ndarray,
    plt_settings: PlotSettings
) -> Axes:
    multiplier = 0
    for attribute, measurement in data_dict.items():
        # 1. Computes the offset for bar placing on the x axis
        offset = (plt_settings.width + plt_settings.gap) * multiplier

        # 2. Computes the rects as fading gradients
        rects = ax.bar(x + offset, measurement, plt_settings.width, label=attribute, color="none")
        rects = convert_rect_to_grad(rects, ax, measurement, plt_settings.colors[multiplier])

        # 3. To show or not the measurement value at the top
        if plt_settings.show_rects:
            ax.bar_label(rects, padding=3, label_type="center")
        multiplier += 1

    return ax

def add_points(
    data_dict: dict,
    ax: Axes,
    x: np.ndarray,
    plt_settings: PlotSettings
) -> Axes:
    multiplier = 0
    for attribute, measurement in data_dict.items():
        # 1. Computes the offset for bar placing on the x axis
        offset = (plt_settings.width + plt_settings.gap) * multiplier

        # 2. Computes the rects as fading gradients
        for idx, msr in enumerate(measurement):
            color = plt_settings.colors[multiplier]
            soft_color = change_lighness(color, factor=plt_settings.lightness_factor)

            jitter = np.random.uniform(-0.015, 0.015, size=len(msr))

            ax.scatter(
                x=np.array([int(x[idx])] * len(msr)) + offset + jitter,
                y=msr,
                s=plt_settings.scatter_size,
                label=attribute,
                color=soft_color,
                zorder=5,
                alpha=plt_settings.scatter_alpha,
                edgecolor="none"
            )

        multiplier += 1

    return ax

def add_errorbar(
    mean_dict: dict,
    std_dict: dict,
    ax: Axes,
    x: np.ndarray,
    plt_settings: PlotSettings
    ) -> Axes:

    multiplier = 0
    for attribute, measurement in mean_dict.items():
        # 1. Computes the offset for bar placing on the x axis
        offset = (plt_settings.width + plt_settings.gap) * multiplier

        cap_half_width = 0.04

        # 2. Computes the rects as fading gradients
        ax.vlines(
            x + offset,
            measurement,
            np.array(measurement) + np.array(std_dict[attribute]),
            color="black",
            linewidth=2,
            zorder=6
        )
        ax.hlines(
            np.array(measurement) + np.array(std_dict[attribute]),
            x + offset - cap_half_width,
            x + offset + cap_half_width,
            color="black",
            linewidth=2,
            zorder=6
        )

        multiplier += 1

    return ax

def add_pvalue(
    data_dict: dict,
    ax: Axes,
    x: np.ndarray,
    plt_settings: PlotSettings
    ) -> Axes:

    # 0. Extract the data as lists for better handling
    first_key_values = list(data_dict.values())[0]
    second_key_values = list(data_dict.values())[1]

    # 1. Build the p-value list
    for tp_idx in range(len(first_key_values)):
        first = first_key_values[tp_idx]
        second = second_key_values[tp_idx]

        t_stat, p_value = ttest_ind(first, second, equal_var=False)
        p_value = cast(float, p_value)
        print(p_value)

        if p_to_stars(p_value) == 'ns':
            continue

        # 1. Computes the offset for bar placing on the x axis
        end_offset = (plt_settings.width + plt_settings.gap)
        x_start = x[tp_idx]
        x_end = x[tp_idx] + end_offset

        # 2. Computes the rects as fading gradients
        first_bar = np.mean(first_key_values[tp_idx]) + plt_settings.pvalue_dist_to_bar
        second_bar = np.mean(second_key_values[tp_idx]) + plt_settings.pvalue_dist_to_bar

        tallest = np.max([first_bar, second_bar])

        ax.vlines(
            x_start,
            first_bar,
            tallest + plt_settings.pvalue_height,
            zorder=7,
            linewidth=2,
            color="black"
        )
        ax.vlines(
            x_end,
            second_bar,
            tallest + plt_settings.pvalue_height,
            zorder=7,
            linewidth=2,
            color="black"
        )
        ax.hlines(
            tallest + 7.0,
            x_start - 0.005,
            x_end + 0.0035,
            zorder=7,
            linewidth=2,
            color="black"
        )
        ax.text(
            (x_start + x_end) / 2,
            tallest + 7.0 + 2.0,
            p_to_stars(p_value),
            ha="center",
            fontsize=20,
            fontweight="bold",
        )


    return ax



# ================================================================
# 2. Section: Axis Management
# ================================================================
def get_y_axis(
    ax: Axes,
    data_dict: dict,
    plt_settings: PlotSettings
) -> Axes:
    ax.set_ylabel(plt_settings.ylabel)
    if plt_settings.vertical_offset == 0 and plt_settings.ylim is not None:
        ax.set_ylim(plt_settings.ylim)
        ax.set_yticks([0,
            int(plt_settings.ylim[1])])
    else:
        valid_maxes = [
            np.nanmax(arr)
            for arr in data_dict.values()
            if len(arr) > 0 and not np.isnan(arr).all()
        ]

        max_value = max(valid_maxes) if valid_maxes else np.nan
        ymax = max_value + plt_settings.vertical_offset
        ax.set_ylim((0, int(ymax)))
        ax.set_yticks([0, int(ymax)])

    return ax



# ================================================================
# 3. Section: Assertions
# ================================================================
def assert_same_keys(dict_1: dict, dict_2: dict) -> None:
    if(dict_1.keys != dict_2.keys):
        logger.warning("Both groups have different sub-group labels, some bars migh be empty\n"
            f"Group 1 Keys: {dict_1.keys()}"
            f"Group 2 Keys: {dict_2.keys()}"
        )
