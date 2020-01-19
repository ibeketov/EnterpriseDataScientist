import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def colcheck(df):
    """
    Prints short infor about columns
    :param df: takes into a dataframe
    :return:
    """
    columns = df.columns.tolist()
    for col in columns:
        print(df[col].head())
        print('Missing (%):', df[col].isnull().mean())
        print(10*'-')