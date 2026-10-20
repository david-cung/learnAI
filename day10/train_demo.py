import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


data = [
    ("The computer will not start", "hardware"),
    ("The monitor is broken", "hardware"),
    ("The keyboard is not working", "hardware"),
    ("The computer mouse is faulty", "hardware"),

    ("I want a refund for my order", "billing"),
    ("I was charged twice", "billing"),
    ("The payment invoice is incorrect", "billing"),
    ("Please check the payment fee", "billing"),

    ("I cannot log into my account", "account"),
    ("I forgot my account password", "account"),
    ("I need to change my account email", "account"),
    ("My account has been locked", "account"),
]

df = pd.DataFrame(
    data,
    columns=["description", "category"],
)

print(df)
print("\n Ticket each category:")
print(df["category"].value_counts())

texts = df["description"]
labels = df["category"]

train_texts, test_texts, train_labels, test_labels = train_test_split(
    texts, labels, test_size=0.2, random_state=42, stratify=labels,
)

vectorizer = CountVectorizer()

X_train = vectorizer.fit_transform(train_texts)
X_test = vectorizer.transform(test_texts)


model = MultinomialNB()

model.fit(X_train, train_labels)
print("\nModel trained successfully.")


