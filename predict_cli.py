"""Command-line helper to run concrete strength predictions without the web UI."""
from __future__ import annotations

import argparse
from pathlib import Path

import joblib
import numpy as np


MODEL_PATH = Path(__file__).resolve().parent / "concrete_strength_model.pkl"

# Reference sample pulled from README for a quick smoke test
SAMPLE_FEATURES = {
    "cement": 300.0,
    "slag": 100.0,
    "fly_ash": 0.0,
    "water": 180.0,
    "superplasticizer": 5.0,
    "coarse_agg": 1000.0,
    "fine_agg": 800.0,
    "age": 28,
}


def load_model(model_path: Path = MODEL_PATH):
    """Load the trained model from disk."""
    return joblib.load(model_path)


def predict_strength(model, features: dict[str, float | int]) -> float:
    """Run the model prediction for the supplied feature mapping."""
    ordered = [
        features["cement"],
        features["slag"],
        features["fly_ash"],
        features["water"],
        features["superplasticizer"],
        features["coarse_agg"],
        features["fine_agg"],
        features["age"],
    ]
    input_array = np.array([ordered], dtype=float)
    return float(model.predict(input_array)[0])


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Predict concrete compressive strength using the trained model.",
    )
    parser.add_argument(
        "--use-sample",
        action="store_true",
        help="Use the sample mix values from the README (ignores other arguments).",
    )
    parser.add_argument("--cement", type=float, help="Cement content.")
    parser.add_argument("--slag", type=float, help="Blast furnace slag content.")
    parser.add_argument("--fly-ash", dest="fly_ash", type=float, help="Fly ash content.")
    parser.add_argument("--water", type=float, help="Water content.")
    parser.add_argument("--superplasticizer", type=float, help="Superplasticizer content.")
    parser.add_argument("--coarse-agg", dest="coarse_agg", type=float, help="Coarse aggregate amount.")
    parser.add_argument("--fine-agg", dest="fine_agg", type=float, help="Fine aggregate amount.")
    parser.add_argument("--age", type=int, help="Age of the concrete sample (days).")
    return parser.parse_args()


def main():
    args = parse_arguments()
    if args.use_sample:
        features = SAMPLE_FEATURES
    else:
        missing = [
            name
            for name in SAMPLE_FEATURES
            if getattr(args, name) is None
        ]
        if missing:
            raise SystemExit(
                f"Missing required arguments: {', '.join(missing)}. "
                "Pass --use-sample to try the default mix."
            )
        features = {name: getattr(args, name) for name in SAMPLE_FEATURES}

    model = load_model()
    prediction = predict_strength(model, features)
    print(f"Predicted compressive strength: {prediction:.2f} MPa")


if __name__ == "__main__":
    main()
