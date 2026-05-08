# ================================================================
# 0. Section: Imports
# ================================================================
from .graphic_utils import (
    transparent_to_color_cmap,
    tri_colormap,
    bi_colormap,
    tri_alpha_colormap
)
from .color import (
    NR_BLUE,
    NR_RED,
    NR_GREY,
    ALPHA_NR_RED,
    ALPHA_NR_GREY,
    ALPHA_NR_BLUE
)


# ================================================================
# 1. Section: Colormaps
# ================================================================
alpha_red_cmap_256 = transparent_to_color_cmap(NR_RED)
alpha_blue_cmap_256 = transparent_to_color_cmap(NR_BLUE)

alpha_black_red_cmap_256 = transparent_to_color_cmap(NR_RED, '#000000')
alpha_black_blue_cmap_256 = transparent_to_color_cmap(NR_BLUE, '#000000')

nr_cmap = tri_colormap('nr_cmap', NR_RED, "#000000", NR_BLUE)
nr_bi_cmap = bi_colormap('nr_bi_cmap', NR_RED, NR_BLUE)

rwb_trimap = tri_colormap('red_white_blue', NR_RED, '#FFFFFF', NR_BLUE)
rbb_trimap = tri_colormap('red_black_blue', NR_RED, '#000000', NR_BLUE)
rgb_trimap = tri_colormap('red_grey_blue', NR_RED, NR_GREY, NR_BLUE)

t_rgb_map = tri_alpha_colormap(ALPHA_NR_RED, ALPHA_NR_GREY, ALPHA_NR_BLUE)
