import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('MLSlbData.csv', encoding = "ISO-8859-1")
df.head()
dfMinutes = df.query('MinutesPlayed >= 1000')
dfUnion = df.query('Team == "Philadelphia"')

plt.style.use('dark_background')
plt.figure()
#sns.scatterplot(x='AverageTacklesPerGame', y = 'TacklesWonPercent', data = df, ax=ax2).set_title('Tackles vs Success Rate')
plt.subplot(311)
plt.scatter(dfMinutes.AverageTacklesPerGame, dfMinutes.TacklesWonPercent, alpha = 0.5)
plt.scatter(dfUnion.AverageTacklesPerGame, dfUnion.TacklesWonPercent, alpha = 0.5, color='red')
for i in range(dfUnion.shape[0]):
    plt.annotate(dfUnion.Name.tolist()[i],(dfUnion.AverageTacklesPerGame.tolist()[i], dfUnion.TacklesWonPercent.tolist()[i]))
print(dfUnion.shape[0])
plt.tight_layout(pad=2.0)
plt.xlabel('Average Tackles Per Game', size=8)
plt.ylabel('Tackles Won Percentage',size=8)
plt.title('Average Tackles per game vs Tackles won %', size=8)
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.55,wspace=0.35)

#sns.scatterplot(x='Average Crosses Per Game', y = 'Accurate crosses, % (total)', data = df, ax=ax2).set_title('Crosses vs Success Rate')
plt.subplot(312)
plt.scatter(dfMinutes.AverageCrossesPerGame, dfMinutes.AccurateCrossesPercent, alpha = 0.5)
plt.scatter(dfUnion.AverageCrossesPerGame, dfUnion.AccurateCrossesPercent, alpha = 0.5, color='red')
for i in range(dfUnion.shape[0]):
    plt.annotate(dfUnion.Name.tolist()[i],(dfUnion.AverageCrossesPerGame.tolist()[i], dfUnion.AccurateCrossesPercent.tolist()[i]))
print(dfUnion.shape[0])
plt.tight_layout(pad=2.0)
plt.xlabel('Average Crosses Per Game', size=8)
plt.ylabel('Accurate Crosses Percentage',size=8)
plt.title('Average Crosses per game vs Successful Crosses %', size=8)
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.55,wspace=0.35)
#sns.scatterplot(x='Average Passes Per Game', y = 'Accurate passes, % (total)', data = df, ax=ax3).set_title('Average passes(per game) vs Pass Accuracy')
plt.subplot(313)
plt.scatter(dfMinutes.AveragePassesPerGame, dfMinutes.AccuratePassPercent, alpha = 0.5)
plt.scatter(dfUnion.AveragePassesPerGame, dfUnion.AccuratePassPercent, alpha = 0.5, color='red')
for i in range(dfUnion.shape[0]):
    plt.annotate(dfUnion.Name.tolist()[i],(dfUnion.AveragePassesPerGame.tolist()[i], dfUnion.AccuratePassPercent.tolist()[i]))
print(dfUnion.shape[0])
plt.tight_layout(pad=2.0)
plt.xlabel('Average Passes Per Game', size=8)
plt.ylabel('Accurate Passes Percentage',size=8)
plt.title('Average Passes per game vs Successful Pass %', size=8)
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.55, wspace=0.35)

plt.show()
