import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

print("Current Working Directory:", os.getcwd())

# Load dataset
df = pd.read_csv("IRIS.csv")

# Encode target
le = LabelEncoder()
df['species'] = le.fit_transform(df['species'])

# Split features and target
X = df.drop('species', axis=1)
y = df['species']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and label encoder
joblib.dump(model, "iris_model.pkl")
joblib.dump(le, "label_encoder.pkl")
print("✅ Model and encoder saved successfully.")
