
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])


print(df) 
print(df.loc[0])
print(df.iloc[0])
print(df.loc[[0, 1]])
# print(df.loc["day2"])
print(df.iloc[[0, 1]])