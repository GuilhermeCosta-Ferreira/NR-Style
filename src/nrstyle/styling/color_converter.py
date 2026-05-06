# ================================================================
# 0. Section: IMPORTS
# ================================================================
import colorsys

import matplotlib.colors as mcolors



# ================================================================
# 1. Section: Functions
# ================================================================
def hex2rgb(hex_color: str) -> tuple:
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16)/255.0 for i in (0, 2, 4))

def change_lighness(color: str | tuple, factor: float = 0.1) -> tuple[float, float, float]:
    r, g, b = mcolors.to_rgb(color)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    l = min(1.0, l + factor)
    return colorsys.hls_to_rgb(h, l, s)
