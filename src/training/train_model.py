import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import joblib

def load_processed_dataset(file_path):
    dataset = pd.read_csv(file_path)
    return dataset

def train_model(dataset):
    features = dataset[[
        "property_size_m2",
        "total_rooms",
        "construction_year"
    ]]

    target = dataset["listing_price_eur"]

    X_train, X_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.2,
        random_state=42
    )

    regression_model = LinearRegression()

    regression_model.fit(X_train, y_train)

    return regression_model

def save_model(model, output_path):
    joblib.dump(model, output_path)

if __name__ == "__main__":
    processed_dataset = load_processed_dataset(
        "../../data/processed/processed_housing_data.csv"
    )

    trained_model = train_model(processed_dataset)

    save_model(
        trained_model,
        "../../outputs/models/model_linear_regression.pkl"
    )

    print("Model training completed successfully.")
