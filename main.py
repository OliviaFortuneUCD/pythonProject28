import pandas as pd
cereal = pd.read_csv("cereal.csv")
print(cereal.head())
print(cereal.info())

# Lowest rating cereal
print(cereal.loc[cereal['rating'] == min(cereal.rating)])

# Best rating cereal
print(cereal.loc[cereal['rating'] == max(cereal.rating)])