import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error


## Load the dataset

df = pd.read_csv("insurance 2.csv")

# Data Preprocessing
numeric_column = df.select_dtypes(include=['int64','float64']).columns
catagorical_column = df.select_dtypes(include=['object']).columns


#Features Engineering

df["age_group"] = pd.cut(df["age"], bins=[0, 18, 25, 35, 50, 100], labels=["0-18", "19-25", "26-35", "36-50", "51+"])
df["bmi_group"] = pd.cut(df["bmi"], bins=[0, 18.5, 25, 30, 100], labels=["under","normal","over","obese"])

X = df.drop("charges",axis=1)
y = df["charges"]

numeric_column = X.select_dtypes(include=['int64','float64']).columns
categorical_column = X.select_dtypes(include=['object']).columns


#Numeric Transform

num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])


# Combine them together
preprocessor = ColumnTransformer(transformers=[
    ('num', num_transformer, numeric_column),
    ('cat', cat_transformer, categorical_column)
])

# split the data set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

pipeline = Pipeline(
    [
        ('preprocessor', preprocessor),
        ('model', GradientBoostingRegressor(n_estimators=100, random_state=42))
    ])

pipeline.fit(X_train, y_train)
y_best_pred = pipeline.predict(X_test)

# evalute the model

r2 = r2_score(y_test, y_best_pred)
mae = mean_absolute_error(y_test, y_best_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_best_pred))


print(f"R2 Score: {r2}")
print(f"Mean Absolute Error: {mae}")
print(f"Root Mean Squared Error: {rmse}")


with open("medical_gb_pipeline.pkl", "wb") as f:
    pickle.dump(pipeline, f)
