import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")

df = pd.read_csv("user_metrics.csv", names=['time', 'online', 'offline', 'idle']) #assign column names
df['total'] = df['online'] + df['offline'] + df['idle']
df.drop("time", 1, inplace = True) #remove date time column

print(df.head())

df['online'].plot()
plt.legend()
plt.show()
plt.savefig("graph_user_metrics.png")