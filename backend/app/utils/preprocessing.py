import pandas as pd


def min_max_scale(series):

    min_val = series.min()
    max_val = series.max()

    scaled = (
        (series - min_val)
        /
        (max_val - min_val)
    ) * 100

    return scaled