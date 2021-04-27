import pandas as pd
import numpy as np
import seaborn as sns



cereal = pd.read_csv("cereal.csv")
#Does sugar give it a higher rating
sugar_df=cereal[['sugars','rating',]]


print(sugar_df.to_string())
sns.regplot(sugar_df['sugars'],sugar_df['rating']).set_title("Ratings of Cereals against Sugar(g)")