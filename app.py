import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Set page config
st.set_page_config(page_title='Retail Demand Prediction', layout='wide')

# Home page
def home():
    st.title('Retail Demand Prediction')
    st.markdown('**by Rizki Pria Aditama**')
    st.write('## Introduction')
    st.write('This Streamlit app is designed to predict retail demand based on historical sales data. The model is built to assist retailers in forecasting future sales and making informed inventory decisions.')

# Data Visualization and Storytelling page
def data_visualization():
    st.title('Data Visualization and Storytelling')
    st.write('## Exploratory Data Analysis')

    # Load your data
    df = pd.read_csv('mock_kaggle.csv')  # Adjust the path to your dataset

    # Data preparation steps
    df.rename(columns={'data': 'date', 'venda': 'sales', 'estoque': 'inventory', 'preco': 'price'}, inplace=True)
    
    # Various plots and analysis
    # (Keep this part the same as your existing code)

# Model Prediction page
def model():
    st.title('Model')
    st.write("Use the model here to make predictions. **For example:** You want to predict demand for the period February 2024, enter sales data, in November 2023 (Sales 3 months ago), December 2023 (Sales 2 Months Ago), & January 2024 (Last Month's Sales).")

    # User input
    last_month_sales = st.number_input("Last Month's Sales", min_value=0)
    two_months_ago_sales = st.number_input('Sales 2 Months Ago', min_value=0)
    three_months_ago_sales = st.number_input('Sales 3 Months Ago', min_value=0)

    # Load the trained model with error handling
    try:
        model = joblib.load('finalized_model.joblib')  # Ensure the path is correct
    except FileNotFoundError:
        st.error("Model file not found. Please check the path.")
        return
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
        return

    # Prediction
if st.button('Predict'):
    prediction = model.predict([[inventory_input, price_input, last_month_sales_input]])
    st.write(f'Demand Forecast: {prediction[0]}")


# Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select a page:', ['Home', 'Data Visualization and Storytelling', 'Model'])

if options == 'Home':
    home()
elif options == 'Data Visualization and Storytelling':
    data_visualization()
elif options == 'Model':
    model()
