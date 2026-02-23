import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("SP500_USA.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Return"] = (
    df.groupby("Ticker")["Adj Close"]
      .pct_change()
)
print(df["Return"].describe())
crash_days = df[df["Return"] < -0.1]
print(crash_days["Date"].dt.year.value_counts().sort_index())
df["Year"] = df["Date"].dt.year
yearly_vol = df.groupby("Year")["Return"].std()
print(yearly_vol.sort_values(ascending=False).head())
df["RollingVol_30"] = (
    df.groupby("Ticker")["Return"]
      .rolling(30)
      .std()
      .reset_index(level=0, drop=True)
)
daily_crash_count = (
    df[df["Return"] < -0.1]
      .groupby("Date")
      .size()
)
cross_sectional_vol = (
    df.groupby("Date")["Return"]
      .std()
)

print(cross_sectional_vol.sort_values(ascending=False).head())
print(daily_crash_count.sort_values(ascending=False).head())
print(df.nsmallest(10, "Return")[["Date", "Ticker", "Return"]])
print(df.nlargest(10, "RollingVol_30")[["Date", "Ticker", "RollingVol_30"]])
print(df.head())
print(df.columns)
print(df.info())


cross_sectional_vol.plot(figsize=(12,5))
plt.title("Cross-Sectional Volatility Over Time")
plt.show()
pre_2008 = df[df["Year"] < 2008]["Return"].std()
post_2008 = df[df["Year"] >= 2008]["Return"].std()

print("Pre-2008 volatility:", pre_2008)
print("Post-2008 volatility:", post_2008)