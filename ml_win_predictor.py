import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib


# Load data
df = pd.read_csv("data/matches.csv")

# Drop rows with missing winner
df = df.dropna(subset=["winner"])

# Create target column
df["won_match"] = (df["toss_winner"] == df["winner"]).astype(int)  # 1 if toss winner also won match

# Encode categorical columns
df_encoded = pd.get_dummies(df[["toss_winner", "toss_decision", "venue"]])

# Features and label
X = df_encoded
y = df["won_match"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("Accuracy:", acc)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))


# Save model & column list
joblib.dump(model, "toss_win_model.pkl")
joblib.dump(X.columns.tolist(), "columns.pkl")