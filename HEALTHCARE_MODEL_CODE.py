import pandas as pd  # For reading and working with the CSV file
from sklearn.model_selection import train_test_split  # To split the data
from sklearn.ensemble import RandomForestClassifier  # ML model
from sklearn.metrics import accuracy_score  # To measure accuracy

# Step 1: Load the dataset
data = pd.read_csv(r'C:\Users\Saujanya Gadge\OneDrive\Desktop\internship\HEALTHCARE APPOINMENT NO_SHOW PROJECT 11.csv')
print(data.head())  # See first few rows
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')

# # Convert "No-show" column from 'Yes'/'No' to 1/0
data['NO_SHOW'] = data['NO_SHOW'].map({'Yes': 1, 'No': 0})

# # Handle categorical columns (like Gender, Neighbourhood)
data = pd.get_dummies(data, drop_first=True)
data = data.fillna(0)

# Step 3: Split into features and target
X = data.drop('NO_SHOW', axis=1)  # Features (input)
y = data['NO_SHOW']  # Target (output)

# Step 4: Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Step 5: Create and train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 6: Predict and check accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
