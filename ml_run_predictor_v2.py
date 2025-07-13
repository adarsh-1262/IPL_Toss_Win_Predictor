import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv("data/deliveries.csv")

# Filter unnecessary innings
df = df[df["inning"] < 3]  # exclude Super Overs etc.

# Encode teams using one-hot encoding
df_encoded = pd.get_dummies(df, columns=["batting_team", "bowling_team"])

# Features: over, inning, batting_team, bowling_team
features = ["over", "inning"] + [col for col in df_encoded.columns if "batting_team_" in col or "bowling_team_" in col]

X = df_encoded[features]
y = df_encoded["total_runs"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
print("Improved Mean Squared Error:", mse)
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv("data/deliveries.csv")

# Filter unnecessary innings
df = df[df["inning"] < 3]  # exclude Super Overs etc.

# Encode teams using one-hot encoding
df_encoded = pd.get_dummies(df, columns=["batting_team", "bowling_team"])

# Features: over, inning, batting_team, bowling_team
features = ["over", "inning"] + [col for col in df_encoded.columns if "batting_team_" in col or "bowling_team_" in col]

X = df_encoded[features]
y = df_encoded["total_runs"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
print("Improved Mean Squared Error:", mse)
