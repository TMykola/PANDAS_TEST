import pandas as pd

# Завантажуємо датафрейм 
df = pd.read_csv('GoogleApps.csv')
#df.info()
print(df.head(25))
#print(df.tail(2))
#print(df["Installs"].mean())
#print("Price:", df[df["Type"] != "Free"]["Price"].min())
#print(df[df["Category"] == "ART_AND_DESIGN"]["Installs"].median())
#print(df[df["Type"] != "Free"]["Reviews"].max())
#print(df["Content Rating"].value_counts()["Everyone"])
#print(df[df["Category"] == "BUSINESS"])
#df.info()
#print("MEAN:", round(df[(df["Rating"] > 4.9) & (df["Category"]=="FINANCE"))
#result = df["Content Rating"].value_counts()["Teen"] / df["Content Rating"].value_counts()["Everyone 10+"] 
#print(round(result, 2))
#print(df[df["Type"] == "Free"]["Rating"].max() - df[df["Type"] != "Free"]["Rating"].max())
#print(df[df["Type"] != "Free"]["Rating"].mean() - df[df["Type"] == "Free"]["Rating"].mean())
#print(len(df[(df["Type"] != "Free")  & (df["Rating"] > 4.9) & (df["Category"] == "GAME")].value_counts()))
#print(len(df[(df["Type"] == "Free")  & (df["Rating"] > 4.9) & (df["Category"] == "GAME")].value_counts()))
#print(df["Category"].value_counts())


#print(df.groupby(by= "Type")["Rating"].agg(["min", "mean", "max"]))
#print(df.groupby(by= "Content Rating")["Price"].agg(["min", "mean", "max"]))
#print(df[df["Category"] == "GAME"]["Content Rating"].max())
#print(df[(df["Content Rating"] == "Everyone") & (df["Type"] == "Paid")]["Category"].value_counts())

print(len(df[(df["Content Rating"] != "Everyone") & (df["Type"] == "Free")]["Category"].value_counts()))




