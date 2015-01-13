import pandas as pd

data = pd.read_csv("WDI_Data.csv")

usa_data = data.loc[data["Country Code"] == "USA"]
usa_data.to_csv("usa_data.csv")