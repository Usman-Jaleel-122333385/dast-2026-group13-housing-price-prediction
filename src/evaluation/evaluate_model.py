import pandas as pd
import joblib

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def load_dataset(file_path):
    dataset = pd.read_csv(file_path)
    return dataset

def load_model(model_path):
    model = joblib.load(model_path)
    return model

def evaluate_model(model, dataset):
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

    predictions = model.predict(X_test)

    results = {
        "mean_absolute_error": mean_absolute_error(y_test, predictions),
        "mean_squared_error": mean_squared_error(y_test, predictions),
        "r2_score": r2_score(y_test, predictions)
    }

    return results

if __name__ == "__main__":
    dataset = load_dataset("../../data/processed/processed_housing_data.csv")
    model = load_model("../../outputs/models/model_linear_regression.pkl")

    evaluation_results = evaluate_model(model, dataset)

    for metric, value in evaluation_results.items():
        print(f"{metric}: {value}")
