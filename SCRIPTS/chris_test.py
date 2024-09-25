from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "The quick brown fox jumps over the lazy dog.",
    "Never jump over the lazy dog quickly.",
    "The quick fox is faster than the lazy dog."
]

# Initialize the vectorizer
vectorizer = CountVectorizer()

# Fit and transform the documents
count_matrix = vectorizer.fit_transform(documents)

# Convert to dense matrix
dense_matrix = count_matrix.toarray()

# Print the word count matrix
print(dense_matrix)

# Print the feature names (words)
print(vectorizer.get_feature_names_out())
