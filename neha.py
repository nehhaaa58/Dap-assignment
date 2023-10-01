import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("nba_2022_2023.csv")
dataframe = pd.DataFrame(data)
dfh = dataframe.head(20)
dfh.plot(x="Player", y="PTS", kind="bar", title="Points of NBA players")
plt.show()