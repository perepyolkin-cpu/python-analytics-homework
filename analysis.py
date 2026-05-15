import pandas as pd
data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 950, 500]}
df = pd.DataFrame(data)
print("Тимчасова назва — Sales Report (temporary title change)")
print(df)
print("Середнє значення:", df["sales"].mean())
