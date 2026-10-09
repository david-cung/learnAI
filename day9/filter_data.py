import pandas as pd

duplicate_df = pd.DataFrame([
    {"ticket_id": 101, "description": "machine not starting", "category": "hardware"},
    {"ticket_id": 102, "description": "need refund", "category": "billing"},
    {"ticket_id": 101, "description": "machine not starting", "category": "hardware"},
    {"ticket_id": 103, "description": "change email", "category": "account"},
])

print(duplicate_df)

duplicated_rows = duplicate_df.duplicated()

print("\nDuplicated rows:\n", duplicated_rows)

print(duplicate_df[duplicated_rows])

drop_duplicates_df = duplicate_df.drop_duplicates()

print("\nDataFrame after dropping duplicates:\n", drop_duplicates_df)
