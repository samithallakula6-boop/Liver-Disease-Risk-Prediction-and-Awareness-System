# Liver Disease Awareness System

## Project Overview

The Liver Disease Awareness System is a Machine Learning-based web application developed using Python and Streamlit.

The application predicts liver disease risk based on user-provided health and lifestyle information and provides personalized health awareness and precautions.

**Note:** This application is designed for educational and awareness purposes only. It does not provide medical diagnosis.

## Project Objectives

- Predict liver disease risk using Machine Learning.
- Provide an interactive and user-friendly interface.
- Generate personalized health awareness based on relevant user inputs.
- Promote awareness about liver health and healthy lifestyle habits.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Joblib

## Machine Learning Model

- Random Forest Classifier
- Model training and evaluation
- Hyperparameter tuning
- Model saving and loading

## Application Features

- 11 patient input features.
- Liver disease risk prediction.
- Risk detected and no-risk prediction outcomes.
- Personalized awareness and precautions.
- Healthcare-themed user interface.
- Medical disclaimer.

## Input Features

1. Age
2. Gender
3. BMI
4. Smoking
5. Alcohol Consumption
6. Genetic Risk
7. Physical Activity
8. Diabetes
9. Hypertension
10. Liver Function Test
11. Heavy Drinker

## Project Structure

```text
Liver-Disease-Awareness-System/
│
├── app.py
├── requirements.txt
├── README.md
├── my_project.ipynb
├── style.css
├── .gitignore
│
├── .streamlit/
│   └── config.toml
│
└── static/
    └── healthcare_background.png
```

The saved trained model file is also included in the project.

## Installation and Execution

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd Liver-Disease-Awareness-System
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

## Disclaimer

This project is developed for educational and health awareness purposes. Predictions are based on patterns learned from the training dataset and should not be considered medical advice or a diagnosis. Consult a qualified healthcare professional for medical evaluation.

## Author

Developed as a personal Machine Learning project.