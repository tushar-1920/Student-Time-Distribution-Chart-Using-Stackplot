import matplotlib.pyplot as plt

# Days of the week
days = [1, 2, 3, 4, 5, 6, 7]

# Hours spent on different activities
studying = [3, 4, 3, 5, 4, 3, 4]
playing = [2, 2, 1, 1, 2, 3, 2]
watching_tv = [2, 1, 2, 2, 1, 1, 1]
sleeping = [5, 5, 6, 5, 6, 5, 5]

# Labels and colors
labels = ['Studying', 'Playing', 'Watching TV', 'Sleeping']
colors = ['blue', 'red', 'yellow', 'pink']

# Create the stackplot
plt.figure(figsize=(6, 6))
plt.stackplot(days, studying, playing, watching_tv, sleeping, labels=labels, colors=colors, alpha=0.4)

# Add legend, labels, and title
plt.legend(loc='upper left')
plt.xlabel('Days')
plt.ylabel('Hours')
plt.title('Student Time Distribution')
plt.grid(True)

# Show the plot
plt.show()
