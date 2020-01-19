import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def colcheck(df):
    """
    Prints short info about columns
    :param df: takes into a dataframe
    :return:
    """
    columns = df.columns.tolist()
    for col in columns:
        print(df[col].head())
        print('Missing (%):', df[col].isnull().mean())
        print(10*'-')

def showmissing(df, lower_thresh=0.0):
    """
    Shows a barplot of the missing values of all columns.
    :param df: takes into a pandas dataframe.
    :param lower_thresh: Allows to threshold the count of missing columns to gain greater insight
    :return:
    """
    plt.figure(figsize=(16,10))
    na_count = df.isna().sum()/df.shape[0]
    na_count = na_count[na_count >= lower_thresh]
    plot = sns.barplot(na_count.index.values, na_count)
    plot.set_xticklabels(plot.get_xticklabels(), rotation=90)