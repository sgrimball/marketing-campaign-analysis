import pandas as pd

df = pd.read_csv("marketing_data.csv")

# See shape of the dataset
print(df.shape)

# See column names
print(df.columns)

# basic info about the data
print(df.info())

# Summary statistics
print(df.describe())

# check for missing values
print(df.isnull().sum())

# Average sales
print(df["Revenue"].mean())

# Highest sales value
print(df["Revenue"].max())

# Lowest sales value
print(df["Revenue"].min())

df["Date"] = pd.to_datetime(df["Date"])

# Performance snapshot
print("Total Revenue:", df["Revenue"].sum())
print("Total Impressions:", df["Impressions"].sum())
print("Total Clicks:", df["Clicks"].sum())
print("Total Conversions:", df["Conversions"].sum())
print("Average ROI:", df["ROI"].mean())

# best campaign performance
campaign_performance = df.groupby("Campaign_Type")["ROI"].mean().sort_values(ascending=False)
print(campaign_performance)

# Best marketing channel
channel_performance = df.groupby("Channel_Used")["ROI"].mean().sort_values(ascending=False)
print(channel_performance)

# conversion efficiency 
df["Conversion_Rate"] = df["Conversions"] / df["Clicks"]

print(df["Conversion_Rate"].mean())
print(df["Conversion_Rate"].describe())

# Create visuals
import matplotlib.pyplot as plt

campaign_performance = df.groupby("Campaign_Type")["ROI"].mean()

campaign_performance.plot(kind="bar")
plt.title("Average ROI by Campaign Type")
plt.ylabel("ROI")
plt.show()

# channel visualization
channel_performance = df.groupby("Channel_Used")["ROI"].mean().head(10)

channel_performance.plot(kind="bar")
plt.title("Top Channel Combinations by ROI")
plt.ylabel("ROI")

plt.show(block=True)

#create a correlation heatmap
import seaborn as sns

numeric_cols = df[[
    "Duration", "Impressions", "Clicks", "Leads",
    "Conversions", "Revenue", "Acquisition_Cost",
    "ROI", "Engagement_Score"
]]

corr = numeric_cols.corr()

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=False, cmap="coolwarm")
plt.title("Correlation Between Marketing Metrics")
plt.show()

# create customer segment chart
segment_performance = df.groupby("Customer_Segment")["ROI"].mean().sort_values()

segment_performance.plot(kind="bar")
plt.title("ROI by Customer Segment")
plt.ylabel("ROI")
plt.show()

# --------------------------------
KEY BUSINESS INSIGHTS
# --------------------------------

# 1. Social Meda campaigns generated the highest average ROI among all campaign types, however there was only a .07 difference between the min and max campaign ROI.

# 2. Multi-channel campaigns involving Email, WhatsApp, and Facebook produced the strongest ROI performance.

# 3. The average conversion rate across campaigns was approximately 22%, indicating strong customer engagement.

# 4. Correlation analysis showed strong relatingships between clicks, leads, conversions, revenue, and ROI, indicating that customer engagment metrics directly contribute to campaign profitability.

# 5. Duration has weak correlation with everything; longer campaigns are not necessarily more effective. 