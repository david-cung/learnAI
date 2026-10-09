import pandas as pd

df = pd.read_csv("tickets.csv")

print(df.head())
print("\nShape", df.shape)
print("\nColumns", df.columns.tolist())
print("\n Types:")
print(df.dtypes)

print("\nSubject column")
print(df["subject"])

print("\nColumn specific data")
print(df[["ticket_id", "category"]])

mask = df["waiting_minutes"] >= 120
slow_tickets = df[mask]

print("\n tickets with waiting time at least 120 minutes:")
print(slow_tickets[["ticket_id", "waiting_minutes"]])
