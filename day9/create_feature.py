import pandas as pd

feature_df = pd.DataFrame([
    {"ticket_id": 101, "description": "machine not starting"},
    {"ticket_id": 102, "description": "need refund"},
    {"ticket_id": 103, "description": "change email"},
])

text = "machine not starting"

print(len(text))

feature_df["description_char_count"] = (
    feature_df["description"].str.len()
)

feature_df["description_word_count"] = (
    feature_df["description"].str.split().str.len()
)

print(feature_df)

long_ticket_mask = feature_df["description"].str.len() > 15
print("\nLong tickets:\n", long_ticket_mask)
print(feature_df[long_ticket_mask][["ticket_id", "description_char_count"]])

feature_column = [
    "description_char_count",
    "description_word_count",
]

X = feature_df[feature_column].to_numpy(dtype="float")

print("\nX:")
print(X)
print("\n nX shape:", X.shape)

feature_df[feature_column]

