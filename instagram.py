import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('comments.csv')
df.columns = df.columns.str.strip().str.lower().str.replace('_', ' ')
df.dropna(inplace=True)

time_col = [c for c in df.columns if 'time' in c or 'date' in c][0]
user_col = [c for c in df.columns if 'user' in c][0]
comment_col = [c for c in df.columns if 'comment' in c][0]
hashtag_col = [c for c in df.columns if 'hashtag' in c][0]

df['time'] = pd.to_datetime(df[time_col], errors='coerce', dayfirst=True)
df['hour'] = df['time'].dt.hour
df['comment_length'] = df[comment_col].astype(str).str.len()

top_users = df[user_col].value_counts().head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_users.index.astype(str), top_users.values, color='green')
plt.title('Top 10 Most Active Users')
plt.xlabel('User ID')
plt.ylabel('Total Interactions')
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df[hashtag_col], df['comment_length'], alpha=0.4, color='orange')
plt.title('Hashtag Count vs Comment Length')
plt.xlabel('Number of Hashtags Used')
plt.ylabel('Length of Comment (Characters)')
plt.show()

print(df.shape)