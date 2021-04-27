import matplotlib.pyplot as plt
plt.style.use('classic')
import pandas as pd
import numpy as np
import seaborn as sns
import datatables

cereal = pd.read_csv("cereal.csv")
fig = plt.figure()

plt.rcParams['figure.figsize'] = [10,10]
plt.rcParams["font.weight"] = "bold"

fontdict={'fontsize': 25,
          'weight' : 'bold'}

fontdicty={'fontsize': 18,
          'weight' : 'bold',
          'verticalalignment': 'baseline',
          'horizontalalignment': 'center'}

fontdictx={'fontsize': 18,
          'weight' : 'bold',
          'horizontalalignment': 'center'}

plt.subplots_adjust(wspace=0.2, hspace=0.2)

fig.suptitle('Can calories and macronutrients affect cereal rating?', fontsize=25,fontweight="bold", color="black",
             position=(0.5,1.01))

ax1 = fig.add_subplot(221)
ax1.scatter('calories', 'rating', data=cereal, c="green")
ax1.set_title('Calories', fontdict=fontdict, color="green")


ax2 = fig.add_subplot(222)
ax2.scatter('fat', 'rating', data=cereal, c="orange")
ax2.set_title('Fat', fontdict=fontdict, color="orange")


ax3 = fig.add_subplot(223)
ax3.scatter('protein', 'rating', data=cereal, c="brown")
ax3.set_title('Protein', fontdict=fontdict, color="brown")

ax4 = fig.add_subplot(224)
ax4.scatter('carbo', 'rating', data=cereal, c="blue")
ax4.set_title("Carbs", fontdict=fontdict, color="blue")