import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset
documents = [
    "I'm walking on sunshine, whoa oh! And don't it feel good?",
    "You are my fire, the one desire. Believe when I say, I want it that way.",
    "I can't feel my face when I'm with you, but I love it.",
    "Just a small-town girl, living in a lonely world.",
    "Hello from the other side, I must have called a thousand times.",
    "Is it too late now to say sorry? 'Cause I'm missing more than just your body.",
    "We don't talk anymore like we used to do.",
    "Cause baby you're a firework, come on show 'em what you're worth.",
    "I got a feeling that tonight's gonna be a good night.",
    "It's a party in the USA!",
    "I will always love you, I hope life treats you kind.",
    "I'm sorry, Ms. Jackson, I am for real.",
    "Don't stop believing, hold on to that feeling.",
    "Shake it off, shake it off!",
    "Rolling in the deep, you had my heart inside of your hand."
]

# Corresponding labels (genres)
labels = [
    'Pop',
    'Pop',
    'Pop',
    'Rock',
    'Pop',
    'Pop',
    'Pop',
    'Pop',
    'Pop',
    'Pop',
    'R&B',
    'Hip Hop',
    'Rock',
    'Pop',
    'Pop'
]


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(documents, labels, test_size=0.2, random_state=42)

# Initialize the TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the training data
X_train_tfidf = vectorizer.fit_transform(X_train)

# Transform the testing data
X_test_tfidf = vectorizer.transform(X_test)

# Initialize the Logistic Regression classifier
classifier = LogisticRegression()

# Train the classifier
classifier.fit(X_train_tfidf, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test_tfidf)

# Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy:.2f}")
# print(classification_report(y_test, y_pred))
print(y_test)
print(y_pred)
