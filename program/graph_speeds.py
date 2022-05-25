# This file builds the graphs for the average % of CPU time

import matplotlib.pyplot as plt
import numpy as np

labels = ['Simple patch', 'Simple offbeat hihats', 'Simple with bass']
vcv = [17.010, 19.614, 34.081]
proj = [1.550, 1.563, 1.869]

x = np.arange(len(labels)) # Label locations
width = 0.35 # Width of bars

# Plot data
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, vcv, width, label="VCV Rack")
rects2 = ax.bar(x + width/2, proj, width, label="Project")

# Add labels, titles, and custom x axis
ax.set_ylabel('% of Avg. CPU time')
ax.set_title('VCV Rack vs Project CPU time')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Show plot
plt.show()