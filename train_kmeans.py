import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("personality_dataset.csv")

# Drop rows with missing target (optional if target exists)
df = df.dropna(subset=["Personality"])

# Define feature columns
numeric_features = ['Time_spent_Alone', 'Social_event_attendance',
                    'Going_outside', 'Friends_circle_size', 'Post_frequency']

categorical_features = ['Stage_fear', 'Drained_after_socializing']

# Define transformations
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(drop='first'))
])

# Full preprocessing pipeline
preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

# Apply preprocessing
X_processed = preprocessor.fit_transform(df)

# Train KMeans model
kmeans_model = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_model.fit(X_processed)

# Save the preprocessor
with open("preprocessor.pkl", "wb") as f:
    pickle.dump(preprocessor, f)

# Save the KMeans model
with open("kmeans_model.pkl", "wb") as f:
    pickle.dump(kmeans_model, f)

print("✅ Models saved: preprocessor.pkl and kmeans_model.pkl")
