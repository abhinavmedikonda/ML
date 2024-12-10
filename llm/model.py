import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('learn.csv')

# Define the features and target variable
X = df[['website_visits', 'time_spent_on_website']]
y = df['status']

# Convert categorical variables to numerical variables
df['status'] = df['status'].map({'active': 1, 'inactive': 0})

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the decision tree model
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

import joblib
# Save the trained model in pickle format
joblib.dump(clf, 'model.pkl')