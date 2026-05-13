
import pandas as pd

df = pd.read_csv("orders.csv")

df["Sales"] = df["Sales"].str.replace("$", "", regex=False)
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

print(df.columns)
print(df.head(10))
print(df.tail(3))
print(df.shape)
print(df.info())
print(df.describe())

print(df["Sales"])
print(df[["Sales", "Coffee Type"]])

print(df.loc[0])
print(df.loc[0, "Sales"])

print(df[df["Sales"] > 20])
print(df[df["Size"] == "Large"])

print(df["Coffee Type"].unique())
print(df["Roast Type"].nunique())

print(df["Sales"].mean())
print(df["Sales"].min())
print(df["Sales"].max())

print(df.sort_values("Sales", ascending=False))

print(df.isnull().sum())

high_sales = df[df["Sales"] > 30]
high_sales.to_csv("high_sales.csv", index=False)

print("Done")