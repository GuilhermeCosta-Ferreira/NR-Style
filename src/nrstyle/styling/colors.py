from .graphic_utils import tri_colormap, tri_alpha_colormap
from .graphic_classes import AlphaColor

NR_RED = "#E63946"
NR_LIGHT_RED = "#FE8E95"
NR_GREY = "#C0C2C3"
NR_DARK_BG = "#141414"
NR_BLUE = "#19D2C5"
NR_DARK_BLUE = "#12988E"

rwb_trimap = tri_colormap('red_white_blue', NR_RED, '#FFFFFF', NR_BLUE)
rbb_trimap = tri_colormap('red_black_blue', NR_RED, '#000000', NR_BLUE)
rgb_trimap = tri_colormap('red_grey_blue', NR_RED, NR_GREY, NR_BLUE)

ALPHA_NR_RED = AlphaColor(NR_RED, alpha=0.5)
ALPHA_NR_GREY = AlphaColor(NR_GREY, alpha=0)
ALPHA_NR_BLUE = AlphaColor(NR_BLUE, alpha=0.5)
t_rgb_map = tri_alpha_colormap(ALPHA_NR_RED, ALPHA_NR_GREY, ALPHA_NR_BLUE)
