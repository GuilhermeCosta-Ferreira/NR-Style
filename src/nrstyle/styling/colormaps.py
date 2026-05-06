# ================================================================
# 0. Section: Imports
# ================================================================
from .graphic_utils import transparent_to_color_cmap, tri_colormap, bi_colormap
from .colors import NR_BLUE, NR_RED


# ================================================================
# 1. Section: Colormaps
# ================================================================
alpha_red_cmap_256 = transparent_to_color_cmap(NR_RED)
alpha_blue_cmap_256 = transparent_to_color_cmap(NR_BLUE)

alpha_black_red_cmap_256 = transparent_to_color_cmap(NR_RED, '#000000')
alpha_black_blue_cmap_256 = transparent_to_color_cmap(NR_BLUE, '#000000')

nr_cmap = tri_colormap('nr_cmap', NR_RED, "#000000", NR_BLUE)
nr_bi_cmap = bi_colormap('nr_bi_cmap', NR_RED, NR_BLUE)
