"""
Train and test a deep neural network regression model reproducibly for reservoir walls.
Usage: PYTHONHASHSEED=0 python src/train.py --seed 42
"""
import argparse
import hashlib
import json
import random
import os
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score

def set_reproducibility_seeds(seed):
    """Fix all random seeds across python, numpy, and tensorflow environments."""
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)
    # Configure deterministic execution for TensorFlow operations
    os.environ['TF_DETERMINISTIC_OPS'] = '1'
    os.environ['TF_CUDNN_DETERMINISTIC'] = '1'
    tf.keras.backend.clear_session()

def main(seed=42, data_path="data/reservoir_data.csv"):
    # Enforce environment and system reproducibility
    set_reproducibility_seeds(seed)
    
    # Load dataset
    #df = pd.read_csv(data_path)
    df = df
    
    # Target engineering variables configuration from your structural analysis setup
    features = ["D", "hn", "HL", "ssuelo", "tp", "tl"]
    X = df[features].copy().values
    y = df[['mu22']].copy().values # Bending moment (Esfuerzo)
    
    # Split into train and test evaluation subsets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=seed
    )
    
    # Isolate scaling fit configurations to prevent Data Leakage
    scaler_features = MinMaxScaler()
    scaler_target = MinMaxScaler()
    
    X_train_scaled = scaler_features.fit_transform(X_train)
    y_train_scaled = scaler_target.fit_transform(y_train)
    
    X_test_scaled = scaler_features.transform(X_test)
    
    # Build a stable Multilayer Perceptron architecture for regression
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(X_train_scaled.shape[1],)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    
    # Define optimizer parameters and compile
    optimizer_stable = tf.keras.optimizers.Adam(learning_rate=0.0005)
    model.compile(optimizer=optimizer_stable, loss='mse', metrics=['mae'])
    
    # Train the network with quiet verbose output logs
    model.fit(
        X_train_scaled, y_train_scaled, 
        epochs=150, batch_size=32, 
        validation_split=0.1, verbose=0
    )
    
    # Infer and reconstruct real domain scale output predictions (mu22)
    predictions_scaled = model.predict(X_test_scaled, verbose=0)
    predictions = scaler_target.inverse_transform(predictions_scaled)
    
    # Evaluate performance metric
    r2 = r2_score(y_test, predictions)
    
    return {
        "seed": seed,
        "data_md5": hashlib.md5(open(data_path, "rb").read()).hexdigest(),
        "r2_score": round(float(r2), 5)
    }

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    print(json.dumps(main(ap.parse_args().seed)))
