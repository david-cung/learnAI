import pandas as pd

tickets = [
    {"ticket_id": 101, "category": "Software", "waiting_minutes": 90, "subject": "Issue with login"},
    {"ticket_id": 102, "category": "Hardware", "waiting_minutes": 150, "subject": "Computer not starting"},
]

df = pd.DataFrame(tickets)

print(df)

print("\nCategory column")

print(df["category"])

print(df[["ticket_id", "category"]])

mask = df["category"] == "Hardware"

print(mask)

hardware_tickets = df[mask]
print("\nTickets in Hardware category:\n", hardware_tickets)

slow_tickets = df["waiting_minutes"] >= 120

print("\n tickets with waiting time at least 120 minutes:\n")
print(df[slow_tickets])

ticket_selection = df[slow_tickets]
print(ticket_selection[["ticket_id", "waiting_minutes"]])

missing_df = pd.DataFrame([
    {"ticket_id": 103, "category": "Software", "waiting_minutes": None, "subject": "Password reset"}, 
    {"ticket_id": 104, "category": "Hardware", "waiting_minutes": 200, "subject": "Monitor flickering"},
    {"ticket_id": 105, "category": "Software", "waiting_minutes": 30, "subject": "Software installation issue"},
    {"ticket_id": 106, "category": "Hardware", "waiting_minutes": None, "subject": "Keyboard not working"},
])

print(missing_df)

print("\nMissing values in waiting_minutes column:\n")
print(missing_df.isna())

missing_waiting_minutes = missing_df["waiting_minutes"].isna()
