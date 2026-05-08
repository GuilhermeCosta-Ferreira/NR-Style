# ================================================================
# 0. Section: IMPORTS
# ================================================================
from .AlphaColor import AlphaColor



# ================================================================
# 1. Section: Colors
# ================================================================
NR_RED = "#E63946"
NR_LIGHT_RED = "#FE8E95"
NR_GREY = "#C0C2C3"
NR_DARK_BG = "#141414"
NR_BLUE = "#19D2C5"
NR_DARK_BLUE = "#12988E"


# ──────────────────────────────────────────────────────
# 1.1 Subsection: Alpha Versions
# ──────────────────────────────────────────────────────
ALPHA_NR_RED = AlphaColor(NR_RED, alpha=0.5)
ALPHA_NR_GREY = AlphaColor(NR_GREY, alpha=0)
ALPHA_NR_BLUE = AlphaColor(NR_BLUE, alpha=0.5)
