"""This module holds all the visualization functions"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def target_distribution_in_keywords(df):
    """This function plots a horizontal bar graph that plots the count of the targets for each keyword"""
    df_copy = df.copy()
    df_copy['target_mean'] = df_copy.groupby('keyword')['target'].transform('mean')
    fig = plt.figure(figsize=(6, 72))

    sns.countplot(y=df_copy.sort_values(by='target_mean', ascending=False)['keyword'],
              hue=df_copy.sort_values(by='target_mean', ascending=False)['target'])

    plt.tick_params(axis='x', labelsize=15)
    plt.tick_params(axis='y', labelsize=12)
    plt.legend(loc=1)
    plt.title('Target Distribution in Keywords')

    plt.show()
