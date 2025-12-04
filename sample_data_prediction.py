"""Evaluate model predictions against rows from the sample dataset."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict

import pandas as pd

from predict_cli import load_model, predict_strength

DATA_PATH = Path(__file__).resolve().parent / "Concrete_Data.csv"
TARGET_COLUMN = "Concrete compressive strength(MPa, megapascals) "
COLUMN_TO_FEATURE: Dict[str, str] = {
    "Cement (component 1)(kg in a m^3 mixture)": "cement",
    "Blast Furnace Slag (component 2)(kg in a m^3 mixture)": "slag",
    "Fly Ash (component 3)(kg in a m^3 mixture)": "fly_ash",
    "Water  (component 4)(kg in a m^3 mixture)": "water",
    "Superplasticizer (component 5)(kg in a m^3 mixture)": "superplasticizer",
    "Coarse Aggregate  (component 6)(kg in a m^3 mixture)": "coarse_agg",
    "Fine Aggregate (component 7)(kg in a m^3 mixture)": "fine_agg",
    "Age (day)": "age",
}


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the trained model against a row from the sample dataset.",
    )
    parser.add_argument(
        "--data-path",
        type=Path,
        default=DATA_PATH,
        help="Path to Concrete_Data.csv (defaults to repository copy).",
    )
    parser.add_argument(
        "--row",
        type=int,
        default=0,
        help="Zero-based row index to test (default: 0).",
    )
    return parser.parse_args()


def extract_features(row: pd.Series) -> dict[str, float]:
    features = {}
    for column, feature_name in COLUMN_TO_FEATURE.items():
        features[feature_name] = float(row[column])
    return features


def main():
    args = parse_arguments()
    data_path: Path = args.data_path
    df = pd.read_csv(data_path)

    if args.row < 0 or args.row >= len(df):
        raise SystemExit(
            f"Row index {args.row} is out of range for dataset with {len(df)} rows."
        )

    row = df.iloc[args.row]
    features = extract_features(row)
    actual_strength = float(row[TARGET_COLUMN])

    model = load_model()
    predicted_strength = predict_strength(model, features)

    print(f"Using row {args.row} from {data_path.name}")
    print("Input features:")
    for key, value in features.items():
        print(f"  {key}: {value}")
    print(f"Actual strength:    {actual_strength:.2f} MPa")
    print(f"Predicted strength: {predicted_strength:.2f} MPa")
    print(f"Error: {predicted_strength - actual_strength:+.2f} MPa")


if __name__ == "__main__":
    main()
