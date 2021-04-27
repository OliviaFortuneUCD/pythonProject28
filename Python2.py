import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats

#The coeffieient ranges from -1 to 1   ... .

cereal = pd.read_csv("cereal.csv")
#Does sugar give it a higher rating
sugar_df=cereal[['sugars','rating',]]

slope, intercept, r_value, p_value, std_err = stats.linregress(sugar_df['sugars'],sugar_df['rating'])

sns.regplot(sugar_df['sugars'],sugar_df['rating']).set_title("Ratings of Cereals against Sugar(g)")

print('The linear coefficient is',r_value)
 