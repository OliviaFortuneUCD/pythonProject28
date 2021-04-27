import matplotlib.pyplot as plt
plt.style.use('classic')
import pandas as pd
import numpy as np
import seaborn as sns
import datatables

cereal = pd.read_csv("cereal.csv")
# get the hot cereals
hotcereals = cereal["sodium"][cereal["type"] == "H"]
# get the cold cereals
coldcereals = cereal["sodium"][cereal["type"] == "C"]


# plot cold cereals
plt.hist(coldcereals, alpha = 0.5, label = 'cold')
# plot hot cereals
plt.hist(hotcereals, label = 'hot')
# add legend
plt.legend(loc = "upper right")
# add a title
plt.title("sodiumn of 80 cereals by type")