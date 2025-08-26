import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

test_input = np.array([1500, 2, 5, 10000, 5000, 4000, 20000]).reshape(1, -1)
print("Predicted cost:", model.predict(test_input))
