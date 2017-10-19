# AutoCleaning.py

import pandas as pd

def detect_variables(df):
	type_dict = {}
	for col in df.columns:
		if len(df[col].unique()) == 1:
			print("Needs multiple values to predict") 
		elif len(df[col].unique()) == 2:
			type_dict[col] = "binary"
		elif 5 >= len(df[col].unique()) > 2:  
			type_dict[col] = "categorical"
		else:
			type_dict[col] = "continuous"
	return type_dict


