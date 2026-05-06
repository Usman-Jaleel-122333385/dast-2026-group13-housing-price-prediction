import pandas as pd

def load_dataset(file_path):
    dataset = pd.read_csv(file_path)
    return dataset

def preprocess_dataset(dataset):
    dataset = dataset.drop_duplicates()

    dataset = dataset.dropna()

    dataset["property_size_m2"] = dataset["property_size_m2"].astype(float)

    dataset["listing_price_eur"] = dataset["listing_price_eur"].astype(float)

    return dataset

def save_processed_dataset(dataset, output_path):
    dataset.to_csv(output_path, index=False)

if __name__ == "__main__":
    raw_dataset = load_dataset("../../data/raw/raw_housing_data.csv")

    processed_dataset = preprocess_dataset(raw_dataset)

    save_processed_dataset(
        processed_dataset,
        "../../data/processed/processed_housing_data.csv"
    )

    print("Preprocessing completed successfully.")
