# ================================================================
# 0. Section: IMPORTS
# ================================================================
import numpy as np
from matplotlib import pyplot as plt

from nrstyle import init_style
from nrstyle.plots import PlotSettings, two_group_stat_bar_plot


# ================================================================
# 1. Section: INPUTS
# ================================================================



# ================================================================
# 2. Section: FUNCTIONS
# ================================================================



# ================================================================
# 3. Section: MAIN
# ================================================================
if __name__ == '__main__':
    init_style()
    np.random.seed(2000)

    # Example Data
    group_1 = {
        "Baseline": {
            "1A": list(np.random.normal(loc=10, size=1)),
            "2A": list(np.random.normal(loc=10, size=1)),
            "3A": list(np.random.normal(loc=10, size=1)),
            "1B": list(np.random.normal(loc=10, size=1)),
            "2B": list(np.random.normal(loc=10, size=1)),
        },

        "Week 1": {
            "1A": list(np.random.normal(loc=2, size=1)),
            "2A": list(np.random.normal(loc=2, size=1)),
            "3A": list(np.random.normal(loc=2, size=1)),
            "1B": list(np.random.normal(loc=2, size=1)),
            "2B": list(np.random.normal(loc=2, size=1)),
        },
        "Week 4": {
            "1A": list(np.random.normal(loc=4, size=1)),
            "2A": list(np.random.normal(loc=4, size=1)),
            "3A": list(np.random.normal(loc=4, size=1)),
            "1B": list(np.random.normal(loc=4, size=1)),
            "2B": list(np.random.normal(loc=4, size=1)),
        },
        "Week 8": {
            "1A": list(np.random.normal(loc=6, size=1)),
            "2A": list(np.random.normal(loc=6, size=1)),
            "3A": list(np.random.normal(loc=6, size=1)),
            "1B": list(np.random.normal(loc=6, size=1)),
            "2B": list(np.random.normal(loc=6, size=1)),
        }
    }
    group_2 = {
        "Baseline": {
            "1A": list(np.random.normal(loc=10, size=1)),
            "2A": list(np.random.normal(loc=10, size=1)),
            "3A": list(np.random.normal(loc=10, size=1)),
            "1B": list(np.random.normal(loc=10, size=1)),
            "2B": list(np.random.normal(loc=10, size=1)),
        },
        "Week 1": {
            "1A": list(np.random.normal(loc=2, size=1)),
            "2A": list(np.random.normal(loc=2, size=1)),
            "3A": list(np.random.normal(loc=2, size=1)),
            "1B": list(np.random.normal(loc=2, size=1)),
            "2B": list(np.random.normal(loc=2, size=1)),
        },
        "Week 4": {
            "1A": list(np.random.normal(loc=2, size=1)),
            "2A": list(np.random.normal(loc=2, size=1)),
            "3A": list(np.random.normal(loc=2, size=1)),
            "1B": list(np.random.normal(loc=2, size=1)),
            "2B": list(np.random.normal(loc=2, size=1)),
        },
        "Week 8": {
            "1A": list(np.random.normal(loc=3, size=1)),
            "2A": list(np.random.normal(loc=3, size=1)),
            "3A": list(np.random.normal(loc=3, size=1)),
            "1B": list(np.random.normal(loc=3, size=1)),
            "2B": list(np.random.normal(loc=3, size=1)),
        }
    }

    config = PlotSettings(
        show_rects = False,
        show_pvalue=True,
        vertical_offset=5,
        pvalue_dist_to_bar = 3.0,
        pvalue_height = 3.0,
        fig_size=(10,8),
        width = 0.35
    )

    two_group_stat_bar_plot(group_2, group_1, ["Control", "Treated"], config)
    plt.show()
