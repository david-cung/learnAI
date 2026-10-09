import pandas as pd

missing_df = pd.DataFrame([
    {"ticket_id": 101, "description": "machine not starting", "category": "hardware"},
    {"ticket_id": 102, "description": None, "category": "hardware"},
    {"ticket_id": 103, "description": "payment failed", "category": None},
    {"ticket_id": 104, "description": "need refund", "category": "billing"},
])

print(missing_df)

clean_df = missing_df.dropna(
    subset=["description", "category"]
)

print(clean_df)

missing_category = missing_df["category"].isna()

print("Tickets with missing category:")
print(missing_df[missing_category]["ticket_id"])

print("\nMissing df rows")
print(len(missing_df))
