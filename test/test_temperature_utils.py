
"""Automated tests for temperature prediction utilities."""

import numpy as np
import pytest

from source.temperature_utils import calculate_prediction_errors


def test_perfect_predictions():
    """Perfect predictions should produce zero error."""
    actual = [20.0, 21.0, 22.0]
    predicted = [20.0, 21.0, 22.0]

    mae, rmse = calculate_prediction_errors(actual, predicted)

    assert mae == 0.0
    assert rmse == 0.0


def test_known_prediction_errors():
    """Check MAE and RMSE against manually calculated values."""
    actual = [20.0, 22.0, 24.0]
    predicted = [21.0, 20.0, 24.0]

    mae, rmse = calculate_prediction_errors(actual, predicted)

    assert np.isclose(mae, 1.0)
    assert np.isclose(rmse, np.sqrt(5 / 3))


def test_empty_inputs():
    """Empty arrays should raise a ValueError."""
    with pytest.raises(ValueError):
        calculate_prediction_errors([], [])


def test_mismatched_lengths():
    """Different input lengths should raise a ValueError."""
    with pytest.raises(ValueError):
        calculate_prediction_errors([20.0, 21.0], [20.0])


def test_non_finite_values():
    """NaN values should raise a ValueError."""
    with pytest.raises(ValueError):
        calculate_prediction_errors([20.0, np.nan], [20.0, 21.0])


def test_multidimensional_inputs():
    """Multidimensional arrays should raise a ValueError."""
    with pytest.raises(ValueError):
        calculate_prediction_errors(
            [[20.0, 21.0]],
            [[20.0, 21.0]]
        )
