import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"].value_counts())

gray = data["Primary Fur Color"].value_counts().Gray
cinnamon = data["Primary Fur Color"].value_counts().Cinnamon
black = data["Primary Fur Color"].value_counts().Black


df = pandas.DataFrame({"Fur Color":["grey", "red", "black"],
                       "Count": [gray, cinnamon, black]})
df.to_csv("squirrel_count.csv", index=False)

