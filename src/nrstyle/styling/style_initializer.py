# ================================================================
# 0. Section: Imports
# ================================================================
import matplotlib.font_manager as fm
import matplotlib.colors as mcolors

from matplotlib import colormaps
from pathlib import Path

from .colormaps import (
    nr_cmap,
    nr_bi_cmap,
    alpha_red_cmap_256,
    alpha_blue_cmap_256
)
from .colors import (
    NR_RED,
    NR_LIGHT_RED,
    NR_GREY,
    NR_DARK_BG,
    NR_BLUE,
    NR_DARK_BLUE
)

# ================================================================
# 1. Section: Font Initialization
# ================================================================
def init_font() -> None:
    BASE_DIR = Path(__file__).resolve().parents[0]
    fm.fontManager.addfont(BASE_DIR / Path("Diagramm/TTF/Diagramm-Light.ttf"))
    fm.fontManager.addfont(BASE_DIR / Path("Diagramm/TTF/Diagramm-Regular.ttf"))
    fm.fontManager.addfont(BASE_DIR / Path("Diagramm/TTF/Diagramm-Bold.ttf"))

    # Find the actual family name Matplotlib sees
    for f in fm.fontManager.ttflist:
        if "Diagramm" in f.name:
            pass
            # print(f"Font Loaded: {f.name}, {f.weight}")   # run once to inspect



# ================================================================
# 2. Section: Color Initialization
# ================================================================
def init_colors() -> None:
    NR_COLORS = {
        "NR_RED": NR_RED,
        "NR_LIGHT_RED": NR_LIGHT_RED,
        "NR_GREY": NR_GREY,
        "NR_DARK_BG": NR_DARK_BG,
        "NR_BLUE": NR_BLUE,
        "NR_DARK_BLUE": NR_DARK_BLUE,
    }
    mcolors.get_named_colors_mapping().update(NR_COLORS)


# ================================================================
# 3. Section: Colormaps Initialization
# ================================================================
def init_colormaps() -> None:
    colormaps.register(nr_cmap, name="nr_cmap")
    colormaps.register(alpha_red_cmap_256, name="nr_red_transparent")
    colormaps.register(alpha_blue_cmap_256, name="nr_blue_transparent")
    colormaps.register(nr_bi_cmap, name="nr_bi_cmap")


def init_style():
    init_font()
    init_colors()
    init_colormaps()
