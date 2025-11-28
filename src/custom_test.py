import joblib
from src.preprocess import clean_text

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

custom_text = [
    "Meet me at 3 today!",
    "Win free tickets today!!"
]

X = [clean_text(custom_text) for s in custom_text]      # clean the input

X_vec = vectorizer.transform(X)     # vectorize it

prediction = model.predict(X_vec)   # predict on it

for text, pred in zip(custom_text, prediction):
    print(text, pred)



