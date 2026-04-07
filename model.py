import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample dataset
data = {
    "size": [500, 800, 1000, 1200, 1500],
    "price": [50, 80, 100, 120, 150]
}

df = pd.DataFrame(data)

X = df[["size"]]
y = df["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")