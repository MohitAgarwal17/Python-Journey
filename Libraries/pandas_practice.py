# import pandas as pd
# print(pd.__version__)

#Series

# Series= A Pandas 1-Dimensional labeled array that can hold any data type
#         Think of it like a single column in a spreadsheet (1-Dimensional)s

# data = [100, 102, 104]
# data = ["A", "B","C"] # objects

# series = pd.Series(data)
# series1 = pd.Series(data, index = ['a', 'b', 'c'])
# print(series1)
# print(series1.loc["a"])
# series1.loc["a"] = 200
# print(series1)
# print(series1.iloc[0])

# data = [100, 102, 104, 200, 202]
# series = pd.Series(data, index = ['a', 'b', 'c', 'd', 'e'])

# print(series[series >= 200])

# calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

# series = pd.Series(calories)
# print(series.loc["Day 1"])
# series.loc["Day 3"] += 500
# print(series)
# print(series[series >= 2000])
# print(series[series < 2000])

# Data Frames

# DataFrame = A tabular data structure with rows AND columns. (2 Dimensional)
#             Similar to an Excel spreadsheet

# data ={"Name": ["Oggy", "Olivia", "Jack"],
#        "Age": [25, 23, 29]}

# df = pd.DataFrame(data)
# print(df)
# df = pd.DataFrame(data, index = ["Contestant 1", "Contestant 2", "Contestant 3"])
# print(df)
# print(df.loc["Contestant 1"])
# print(df.iloc[0])

# Add a new column
# df["Position"] = ["Third", "Second", "First"]
# print(df)

# Add a new row
# new_row = pd.DataFrame([{"Name": "Bob", "Age": 35, "Position": "Fourth"}])
# df = pd.concat([df, new_row])
# df = pd.concat([new_row, df]) # concatenates at 0 index
# new_row = pd.DataFrame([{"Name": "Bob", "Age": 35, "Position": "Fourth"}],
#                        index = ["Contestant 4"])
# new_row = pd.DataFrame([{"Name": "Bob", "Position": "Fourth", "Age": 35}],  # key position does not matter
#                        index = ["Contestant 4"])
# df = pd.concat([df, new_row])
# print(df)

# Add new rows

# new_rows = pd.DataFrame([{"Name": "Bob", "Age": 35, "Position": "Fourth"},
#                          {"Name": "Joe", "Age": 31, "Position": "First"}],
#                        index = ["Contestant 4", "Contestant 5"])
# df = pd.concat([df, new_rows])
# print(df)

# Importing CSV and JSON files

# df = pd.read_csv("data.csv")
# print(df)
# print(df.to_string())
# df.to_json("data.json", orient="records", indent=4)

# df = pd.read_json("data.json")
# print(df.to_string())

# Selection

# df = pd.read_csv("data.csv")

# Selection by column

# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df[["Name", "Height", "Weight"]].to_string())

# Selection by row

# df = pd.read_csv("data.csv")
# print(df.loc[0])

# df = pd.read_csv("data.csv", index_col = "Name")
# print(df.loc["Moltres"])
# print(df.loc["Charizard"])
# print(df.loc["Charizard", ["Height", "Weight"]])
# print(df.loc["Charizard":"Pikachu", ["Height", "Weight"]])
# print(df.iloc[0])
# print(df.iloc[0:11])
# print(df.iloc[0:11:2])
# print(df.iloc[0:11:2, 0:3])
# print(df.iloc[0:11:2, 0:3:2])

# Exercise

# pokemon = input("Enter a Pokemon Name: ")
# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} not found in DataFrame")

# Filtering

# df = pd.read_csv("data.csv")
# Filtering = Keeping the rows that match a condition

# tall_pokemon = df[df["Height"] >= 2]
# print(tall_pokemon)
# heavy_pokemon = df[df["Weight"] >= 100]
# print(heavy_pokemon)
# legendary_pokemon = df[df["Legendary"] == True]
# legendary_pokemon = df[df["Legendary"] == 1]
# print(legendary_pokemon)
# water_pokemon =df[(df["Type1"] ==  "Water") |
#                   (df["Type2"] == "Water")]
# print(water_pokemon)
# ff_pokemon =df[((df["Type1"] ==  "Fire") & (df["Type2"] == "Flying")) |
#                 (df["Type1"] ==  "Flying") & (df["Type2"] == "Fire")]
# print(ff_pokemon)

# Aggregation

# aggregate functions = Reduces a set of values into a single summary value
#                       Used to summarize and analyze data
#                       Often used with the groupby() function

# df = pd.read_csv("data.csv")
# Whole DataFrame
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# Single column
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Type2"].count())

# Groupby()

# group = df.groupby("Type1")
# print(group)
# print((group.count()))
# a = (group["Height"].count().tolist())
# print(sum(a))
# print(group["Height"].mean())
# print(group["Height"].median())
# print(group["Height"].sum())
# print(group["Height"].min())
# print(group["Height"].max())

# Data Cleaning

# Data cleaning = the process of fixing/removing:
#                 incomplete, incorrect, or irrelevant data.
#                 ~75% of work done with Pandas is data cleaning

# df = pd.read_csv("data.csv")

# 1. Drop irrelevant columns
# df = df.drop(columns = ["Legendary", "No"])

# 2. Handle missing data
# df = df.dropna(subset = ["Type2"])
# df = df.fillna({"Type2": "None"})

# 3. Fix inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                    "Fire": "FIRE",
#                                    "Water": "WATER"})

# 4. Standardize Text
# df["Name"] = df["Name"].str.upper()

# 5. Fix data types
# df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicate values
# df = df.drop_duplicates()

# print(df.to_string())