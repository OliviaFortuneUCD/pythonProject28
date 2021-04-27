import matplotlib.pyplot as plt
plt.style.use('classic')
import pandas as pd
import numpy as np
import seaborn as sns
import datatables

cereal = pd.read_csv("cereal.csv")
sodium = cereal["sodium"]
#plot a histogram
plt.hist(sodium)
plt.title("sodium in 80 cereals products")