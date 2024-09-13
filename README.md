
# Hydrogen Concentration Prediction

This project involves developing a machine learning model to predict hydrogen concentration using a gas-phase sensor. The model analyzes experimental data under well-defined environmental conditions and predicts the hydrogen concentration (in ppm) based on various input features.

## Project Structure

The project directory is structured as follows:

```
root/
│
└── hydrogen_concentration/
    ├── data_analysis.ipynb
    ├── preprocessing.py
    └── train.py
```

### Files:

1. **`data_analysis.ipynb`**: A Jupyter notebook where exploratory data analysis (EDA), feature engineering, and model training experiments were conducted. This notebook was used for experimentation and validation of the model-building process.

2. **`preprocessing.py`**: A modular Python script that includes all the preprocessing steps carried out in the `data_analysis.ipynb`. It handles data cleaning, feature engineering, and transformations required for the model.

3. **`train.py`**: A Python script responsible for training the machine learning model using the preprocessed data and saving the trained model for future use. 

## Approach Overview

The following steps were performed to create the predictive model:

### 1. **Data Reading and Exploration**
   - The dataset contains several features, such as hydrogen concentration (ppm), sensor resistance, humidity, temperature, pressure, operator, and time.
   - Initial exploratory data analysis included KDE plots to visualize feature distributions, which guided the model selection process.
  
### 2. **Feature Engineering**
   - New attributes were derived from existing ones to enhance the model's predictive power.
   - Correlation analysis was conducted to identify the most relevant features for predicting hydrogen concentration.

### 3. **Model Selection**
   - Based on the EDA, a **Random Forest** model was chosen for its robustness and ability to handle correlated and noisy data.
   
### 4. **Data Splitting**
   - The dataset was split into two parts: 67% for training and 33% for testing the model.

### 5. **Data Preprocessing**
   - Standard scaling was applied to both the training and testing data to ensure consistent feature scaling.

### 6. **Model Evaluation**
   - **Mean Absolute Error (MAE)** and **R-squared (R²)** scores were used to evaluate the model's performance.
   - Cross-validation was performed to ensure the generality of the model.

### 7. **Results**
   - **Mean Absolute Error (Testing Data)**: 1.36
   - **R² (Testing Data)**: 0.99
   - **Mean Absolute Error (Cross Validation Mean)**: 2.7
   - **R² (Cross Validation Mean)**: 0.96

## Installation

This project uses `Poetry` for dependency management and packaging. Follow the steps below to install the project dependencies:

1. Install [Poetry](https://python-poetry.org/docs/#installation) if not already installed:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/hydrogen_concentration.git
   cd hydrogen_concentration
   ```

3. Install the dependencies:

   ```bash
   poetry install
   ```

## Usage

### Running Exploratory Data Analysis (EDA)

To perform exploratory data analysis and model training experiments, open the `data_analysis.ipynb` notebook and run the cells step by step:

```bash
jupyter notebook data_analysis.ipynb
```

### Preprocessing Data

To preprocess the dataset using the steps defined in the `preprocessing.py` file:

```bash
poetry run python hydrogen_concentration/preprocessing.py
```

### Training the Model

To train the Random Forest model and save it for production, run the `train.py` script:

```bash
poetry run python hydrogen_concentration/train.py
```

## Model Evaluation

After training the model, the performance metrics (MAE, R²) will be printed out in the console. You can also cross-validate the model to ensure its generalizability by modifying the relevant code in the `train.py` script.



This `README.md` provides a detailed guide for your project, including the approach, installation, and usage instructions for running the exploratory analysis, preprocessing, and training scripts. Let me know if you need any adjustments!