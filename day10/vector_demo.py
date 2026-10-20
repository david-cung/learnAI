from sklearn.feature_extraction.text import CountVectorizer

texts = [
    "broken keyboard",
    "broken screen",
    "keyboard repair",
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(texts)

print("Feature names:")
print(vectorizer.get_feature_names_out())


print("\nFeature values:")
print(X.toarray())

print("\nShape", X.shape)




