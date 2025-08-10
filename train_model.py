import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv(r"C:\Users\dell\Downloads\patentdata2.csv")  # Change path if needed

# Features and target column (removed History, Whendiagnoused)
FEATURES = [
    "Gender",
    "Age",
    "Patient",
    "TakeMedication",
    "Severity",
    "BreathShortness",
    "VisualChanges",
    "NoseBleeding",
    "Systolic",
    "Diastolic",
    "ControlledDiet"
]
TARGET = "Stages"

# Keep only needed columns
df = df[FEATURES + [TARGET]]

# Separate features and target before encoding
X = df[FEATURES]
y = df[TARGET]

# Convert categorical columns to numeric
X = pd.get_dummies(X, drop_first=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model and column names
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(list(X.columns), open("model_columns.pkl", "wb"))

print("✅ Model training completed successfully!")
