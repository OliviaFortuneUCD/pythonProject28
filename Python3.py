import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats

#The coeffieient ranges from -1 to 1   ... .

cereal = pd.read_csv("cereal.csv")


nutrition_df=cereal[['protein','fat','sodium','fiber','carbo','sugars','potass','vitamins','rating']]
corr = nutrition_df.corr()
ax = sns.heatmap(
    corr,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);
