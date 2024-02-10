import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('QueryResults.csv')
df.head()
df.columns=["Date","Tag","Post"]
df.head()
df.shape
df[['Date','Tag','Post']].count()
df.groupby('Tag').sum()
df.Date = pd.to_datetime(df.Date)
reshaped_df = df.pivot(index='Date', columns='Tag', values='Post')
reshaped_df.head()
reshaped_df.fillna(0, inplace=True)
reshaped_df.count()
reshaped_df.isna().values.any()
# plt.plot(reshaped_df.index, reshaped_df['python'], reshaped_df['java'])

# making visuals of data with matplotlib

# plt.plot(reshaped_df.index, reshaped_df['python'], reshaped_df['java'])

roll_df = reshaped_df.rolling(window=6).mean()


plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], 
             linewidth=3, label=roll_df[column].name)
plt.legend(fontsize=11) 
