import pandas as pd
import requests
import ast
import re

PLAYER_DOBS = {
	"serenawilliams": "1981-09-26",
	"rafaelnadal": "1986-06-03"
}

def getPlayerData(name):
	formatted_name = _formatPlayerName(name)
	url = f"https://www.tennisabstract.com/jsmatches/{formatted_name}Career.js"

	raw_data = _getJS(url)
	if raw_data is None:
		raise ValueError(f"Error: {name} match data not found")

	key = formatted_name.lower()
	player_dob = PLAYER_DOBS.get(key)
	if not player_dob:
		raise ValueError(f"Error: DOB not found for {name}")
	
	return _cleanData(raw_data, player_dob = player_dob)

def _formatPlayerName(name):
	if " " in name:
		return name.title().replace(" ", "")
	return name


def _getJS(url):
	response = requests.get(url)
	if response.status_code != 200:
		return None

	match = re.search(r"=\s*(\[.*\]);?\s*$", response.text, re.DOTALL)
	if match:
		return ast.literal_eval(match.group(1))
	else:
		raise ValueError("Could not parse JavaScript array")


def _cleanData(match_data, player_dob):
	df = pd.DataFrame(_parseMatches(match_data))
	return _calculateAges(df, player_dob)


def _parseMatches(match_data):
	cleaned_rows = []
	for m in match_data:
		row = {
			"date": m[0],
			"tournament": m[1],
			"surface": m[2],
			"result": m[4],
			"opponent": m[11],
			"age_data": m[16]
		}
		cleaned_rows.append(row)

	return cleaned_rows


def _calculateAges(df, player_dob):
	df["date"] = pd.to_datetime(df["date"])
	df["player_age"] = (df["date"] - pd.to_datetime(player_dob)).dt.days / 365

	is_female = df["age_data"].astype(str).str.match(r"^\d{8}$")
	if is_female.any():
		df["age_data"] = pd.to_datetime(df["age_data"])
		df["opp_age"] = (df["date"] - df["age_data"]).dt.days / 365

	is_male = ~is_female
	if is_male.any():
		df["opp_age"] = df["age_data"].astype(float)

	df["age_diff"] = df["player_age"] - df["opp_age"]

	return df