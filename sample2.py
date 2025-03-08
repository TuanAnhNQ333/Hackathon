import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'data' DataFrame is already loaded

plt.figure(figsize=(12, 6))
sns.countplot(x='Final Grade', hue='Learning Style', data=data, order=sorted(data['Final Grade'].unique()))
plt.title('Learning Style vs. Final Grade', fontsize=16)
plt.xlabel('Final Grade', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.xticks(rotation=0, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(title='Learning Style', title_fontsize=12, fontsize=10)
plt.tight_layout()
plt.show()
