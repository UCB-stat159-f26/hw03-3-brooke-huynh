import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def createPlot(df, output_path=None):
	sns.scatterplot(
		data = df,
		x = "player_age",
		y = "age_diff",
		hue = "result",
		palette = {"W": "deepskyblue", "L": "purple"},
		alpha = 0.7,
		edgecolor = None,
		s = 15
	)

	plt.title("Player's Professional Career Matches", fontweight = "bold", loc = "left")
	plt.xlabel("Player's Age:", color = "gray", size = 7)
	plt.ylabel("")
	plt.axhline(0, color = "black", linewidth = 0.7, alpha = 0.6)
	plt.grid(True, which = "both", axis = "both", color = "gray", alpha = 0.3)
	plt.legend(title = "")

	if output_path:
		os.makedirs(os.path.dirname(output_path), exist_ok=True)
		plt.savefig(output_path)