# MMA3001 — Numerical Methods and Machine Learning

## Short-Term Indoor Temperature Prediction Using Smart Building Sensor Data

### 1. Project Overview

This project investigates the use of machine learning regression methods to predict indoor temperature approximately 30 minutes in advance using environmental sensor data from the Monash Smart Infrastructure (MSI) dataset.

The primary objective is to compare the prediction accuracy, computational efficiency and complexity of several regression methods.

### 2. Engineering Problem

Accurate short-term temperature predictions could assist smart building environmental monitoring and inform future HVAC control strategies.

The central research question is:

**How accurately can indoor temperature be predicted 30 minutes ahead using historical temperature measurements, and which computational method provides the best balance of accuracy and efficiency?**

### 3. Dataset

**Dataset:** Monash Smart Infrastructure Occupancy and Environmental Data (Dataset 2)

**Source file:** `5EnvSensor_MayToDec2024_180kRows.csv`

**Selected sensor:** `6012002000869`

The analysis uses 13,800 unique temperature measurements from the selected sensor, spanning February to June 2024.

The original environmental records contain JSON-encoded measurements, including temperature, humidity, carbon dioxide and other environmental variables.

This project focuses on temperature measurements.

**Data preparation includes:**
- Extracting temperature measurements and timestamps from JSON.
- Converting Unix timestamps to UTC datetimes.
- Removing duplicate measurements.
- Investigating irregular sampling intervals.
- Creating approximately 30-minute-ahead prediction targets.
- Creating historical temperature features from previous measurements.

The raw dataset is not included in this repository. Users must obtain the dataset through the authorised MMA3001 course materials and upload it to their Colab environment.

### 4. Computational Methods

Five prediction approaches are investigated:

1. Persistence baseline
2. Simple Linear Regression
3. Historical Linear Regression
4. Decision Tree Regression
5. Random Forest Regression

Models are evaluated using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

Decision Tree maximum depth is investigated using a chronological validation dataset.

### 5. Project Structure

```text
MMA3001-Project/
├── data/
├── docs/
│   ├── index.html
│   ├── temperature_utils.html
│   └── search.js
├── examples/
│   └── MMA3001_Temperature_Prediction.ipynb
├── source/
│   └── temperature_utils.py
├── test/
│   ├── test_temperature_utils.py
│   └── test_report.txt
├── .gitignore
├── LICENSE
└── README.md
```

### 6. Software Requirements

The project uses Python and the following libraries:

- NumPy
- Pandas
- Matplotlib
- scikit-learn
- pytest
- pdoc

The analysis was developed using Google Colab.

### 7. Running the Project

1. Open `examples/MMA3001_Temperature_Prediction.ipynb` in Google Colab.
2. Upload the environmental sensor CSV file to the Colab session.
3. Ensure the notebook's data-loading path matches the uploaded CSV filename.
4. Run the notebook cells sequentially.
5. Examine the generated data summaries, prediction results, optimisation tables and graphs.

The notebook requires access to the original dataset to reproduce the full analysis.

### 8. Automated Testing

The file `source/temperature_utils.py` contains a documented function for calculating prediction errors.

The automated tests check:

- Perfect predictions.
- Known MAE and RMSE values.
- Empty inputs.
- Mismatched input lengths.
- Non-finite numerical values.
- Multidimensional inputs.

Run the tests from the repository root using:

```bash
python -m pytest test/ -v
```

**Recorded test outcome:** Six tests passed.

The detailed pytest output is provided in `test/test_report.txt`.

### 9. HTML Documentation

Generated HTML documentation is available in the `docs/` folder.

Open `docs/index.html` in a browser to navigate the documentation.

The documentation was generated using `pdoc` from the Python source file's docstrings.

### 10. Results

In the exploratory final comparison, Random Forest achieved the lowest MAE and RMSE.

| Model | MAE (°C) | RMSE (°C) |
|---|---:|---:|
| Persistence | 0.2036 | 0.4008 |
| Simple Linear Regression | 0.2213 | 0.3954 |
| Historical Linear Regression | 0.1984 | 0.3272 |
| Decision Tree | 0.1739 | 0.2975 |
| Random Forest | 0.1725 | 0.2917 |

Random Forest demonstrated the strongest prediction accuracy in this comparison, while Decision Tree offered comparable accuracy with lower measured training time.

### 11. Limitations

- Only one environmental sensor was analysed.
- Historical measurement availability reduced the number of complete modelling samples.
- Irregular sampling intervals required timestamp-aware feature construction.
- The models were not tested on independent buildings or sensor locations.
- Parts of the eventual test period were examined during earlier development, limiting the independence of the final evaluation.
- Computational timings may vary depending on execution hardware and runtime conditions.
- Predictive accuracy does not establish that the models would improve real HVAC control performance.

### 12. AI Acknowledgement

ChatGPT was used during project development to assist with Python code suggestions, debugging, explanations of computational methods, documentation drafting and suggestions for automated tests.

AI-generated suggestions were reviewed through code execution, comparison with observed outputs, testing and interpretation of model results.

The use of AI and its contribution to the project will be discussed in the accompanying written report, including limitations of AI assistance and the student's responsibility for technical decisions and validation.

### 13. Licence

See the repository's `LICENSE` file for the licence applicable to the original project code. Third-party datasets remain subject to their own access and licensing conditions.
