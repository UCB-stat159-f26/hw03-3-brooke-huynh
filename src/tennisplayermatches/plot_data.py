import os
import matplotlib.pyplot as plt
import seaborn as sns

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

	_configurePlot()
	_cleanLegend()

	if output_path:
		os.makedirs(os.path.dirname(output_path), exist_ok=True)
		plt.savefig(output_path)


def _configurePlot():
	plt.title("Player's Professional Career Matches", fontweight = "bold", loc = "left")
	plt.xlabel("Player's Age", color = "gray", size = 7)
	plt.ylabel("")
	plt.axhline(0, color = "black", linewidth = 0.7, alpha = 0.6)
	plt.grid(True, which = "both", axis = "both", color = "gray", alpha = 0.3)


def _cleanLegend():
	handles, labels = plt.gca().get_legend_handles_labels()
	if handles and labels:
		unique_labels = dict(zip(labels, handles))
		plt.legend(unique_labels.values(), unique_labels.keys(), title="", frameon=True)