### Text Prediction Model - Natural Language Toolkit(NLTK) and deployed app on streamlit
## Text prediction machine learning app

This Streamlit app, **Text Pred**, provides a user-friendly interface for performing sentiment analysis on text reviews. It allows users to input a single review or upload an Excel file containing multiple reviews for batch processing. The app uses a pre-trained machine learning model to predict whether the reviews are positive or negative.

## Features

- **Single Review Prediction**: Input a single text review and get an immediate sentiment prediction (positive/negative).
- **Batch Processing**: Upload an Excel file with multiple reviews, and the app will predict the sentiment for each review.
- **Download Results**: For batch processing, users can download an Excel file containing the original reviews and their corresponding sentiment predictions.

## How to Use the App

### 1. Single Review Prediction

- Open the app and select the **Single Review** option from the dropdown menu.
- Enter your review in the text input box.
- Click on the **Predict** button to get the sentiment result.
  - A green message will indicate a positive review.
  - A yellow message will indicate a negative review.

### 2. Batch Processing (Excel File)

- Select the **Batch Processing (Excel File)** option from the dropdown menu.
- Upload an Excel file (`.xlsx`) containing reviews.
  - The file should have a column named `review` which contains the text data to analyze.
- The app will display a preview of the uploaded data.
- Once processed, the sentiment analysis results will be displayed.
- You can download the updated Excel file with the new `Sentiment` column by clicking the **Download Excel with Sentiment** button.
## 3. Section showing visuals giving an overview of the analysis of the batch excel file uploaded

## Prerequisites

Before running the app, make sure you have the following installed:

- Python 3.x
- Required Python packages:
  - streamlit
  - pandas
  - openpyxl
  - scikit-learn (for model serialization and prediction)

You can install these packages using the following command:

```bash
pip install streamlit pandas openpyxl scikit-learn
