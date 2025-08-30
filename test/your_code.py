import pandas as pd

# Завантажуємо датафрейм 
df = pd.read_csv('GoogleApps.csv')
#df.info()
#print(df.head(2))
#print(df.tail(2))
#print("MEAN:", round(df[(df["Rating"] > 4.9) & (df["Type"]=="Free")]["Installs"].mean(), 2))
#print(df["Installs"].mean())
#
#print("Price:", df[df["Type"] != "Free"]["Price"].min())
#print(df[df["Category"] == "ART_AND_DESIGN"]["Installs"].median())


print(df[df["Type"] == "Free"]["Reviews"].max() - df[df["Type"] != "Free"]["Reviews"].max())
print(df[df["Type"] != "Free"]["Reviews"].max())
