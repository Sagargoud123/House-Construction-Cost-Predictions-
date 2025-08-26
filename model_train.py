import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("house_construction_data.csv")

# Features and Target
X = df[["Area (sq. ft.)", "Labor Cost (₹)", "Material Type", 
        "Pipes (₹)", "Lights (₹)", "Fans (₹)", "Steel (₹)", "Bricks (₹)"]]
y = df["Total Cost (₹)"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
