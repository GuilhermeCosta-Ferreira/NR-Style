# ================================================================
# 0. Section: IMPORTS
# ================================================================
from dataclasses import dataclass, field



# ================================================================
# 1. Section: Functions
# ================================================================
@dataclass
class PlotSettings:
    ylabel: str = "Metric"
    title: str = "Title of the Plot"
    fig_size: tuple = (8, 8)
    ylim: tuple | None = None
    show_rects: bool = True
    colors: list[str] = field(default_factory=lambda: ["NR_GREY", "NR_RED"])
    width: float = 0.25
    gap: float = 0.0
    vertical_offset: float = 0.0
    show_legend: bool = True
    scatter_size: int = 75
    lightness_factor: float = 0.1
    scatter_alpha: float = 0.8
    show_points: bool = False
    label_points: bool = False
    show_errorbar: bool = False
    show_pvalue: bool = False
    pvalue_dist_to_bar: float = 5.0
    pvalue_height: float = 7.0
