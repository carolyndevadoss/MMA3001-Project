
"""Utility functions for indoor temperature prediction.

MMA3001 Numerical Methods and Machine Learning.
"""

import numpy as np


def calculate_prediction_errors(actual, predicted):
    """Calculate MAE and RMSE for temperature predictions.

    Parameters
    ----------
    actual : array-like
        Observed temperatures in degrees Celsius.
    predicted : array-like
        Predicted temperatures in degrees Celsius.

    Returns
    -------
    tuple of float
        Mean absolute error and root mean squared error,
        both expressed in degrees Celsius.

    Raises
    ------
    ValueError
        If inputs are empty, have different lengths,
        or contain non-finite values.
    """
    actual = np.asarray(actual, dtype=float)
    predicted = np.asarray(predicted, dtype=float)

    if actual.ndim != 1 or predicted.ndim != 1:
        raise ValueError("Inputs must be one-dimensional.")

    if len(actual) == 0 or len(actual) != len(predicted):
        raise ValueError("Inputs must be non-empty and equal length.")

    if not np.all(np.isfinite(actual)):
        raise ValueError("Actual values must be finite.")

    if not np.all(np.isfinite(predicted)):
        raise ValueError("Predictions must be finite.")

    mae = np.mean(np.abs(actual - predicted))
    rmse = np.sqrt(np.mean((actual - predicted) ** 2))

    return float(mae), float(rmse)


