# Import necessary libraries
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
    st.write('## Introduction')
    st.write('This Streamlit app is designed to predict retail demand based on historical sales data. The model is built to assist retailers in forecasting future sales and making informed inventory decisions.')

# Data Visualization and Storytelling page
def data_visualization():
    st.title('Data Visualization and Storytelling')
    st.write('## Exploratory Data Analysis')

    # Load your data
    df = pd.read_csv('mock_kaggle.csv')  # Adjust the path to your dataset
    df_eda = df.copy()

    # Time Series Plot of Sales
    st.write('### Time Series Plot of Sales')
    fig1, ax1 = plt.subplots()
    df_eda['sales'].plot(figsize=(14, 7), ax=ax1)
    ax1.set_title('Time Series Plot of Sales')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Sales')
    st.pyplot(fig1)
    st.write('**Insight:** An upward or downward trend in sales over time could indicate the effectiveness of marketing strategies or shifts in consumer preferences.')
    st.write('**Action:** Conduct a deeper analysis to identify potential causes behind the trend and adjust your business strategies accordingly.')

    # Rolling Mean and Standard Deviation of Sales
    st.write('### Rolling Mean and Standard Deviation of Sales')
    fig2, ax2 = plt.subplots()
    df_eda['sales'].rolling(window=30).mean().plot(label='30 Day Rolling Mean', ax=ax2)
    df_eda['sales'].rolling(window=30).std().plot(label='30 Day Rolling Std', ax=ax2)
    ax2.legend()
    ax2.set_title('Rolling Mean and Standard Deviation of Sales')
    st.pyplot(fig2)
    st.write('**Insight:** An increasing rolling mean might suggest overall growth in sales, while an increasing rolling standard deviation indicates greater variability in sales.')
    st.write('**Action:** Modify inventory or stocking levels based on observed trends to optimize stock levels.')

    # Sales Distribution
    st.write('### Sales Distribution')
    fig3, ax3 = plt.subplots()
    sns.histplot(df_eda['sales'], kde=True, ax=ax3)
    ax3.set_title('Sales Distribution')
    st.pyplot(fig3)
    st.write('**Insight:** The shape of the sales distribution can indicate a high concentration of transactions within certain price or volume ranges.')
    st.write('**Action:** Focus marketing efforts and inventory on the most frequent sales segments.')

    # Correlation Heatmap
    st.write('### Correlation Heatmap')
    fig4, ax4 = plt.subplots()
    correlation_matrix = df_eda[['sales', 'inventory', 'price']].corr()
    sns.heatmap(correlation_matrix, annot=True, ax=ax4)
    ax4.set_title('Correlation Heatmap')
    st.pyplot(fig4)
    st.write('**Insight:** A significant positive or negative correlation between variables like inventory and sales could indicate relationships that might be leveraged.')
    st.write('**Action:** Ensure adequate stock levels to meet anticipated demand if inventory and sales are highly correlated.')

    # Scatter Plot of Price vs Sales
    st.write('### Scatter Plot of Price vs Sales')
    fig5, ax5 = plt.subplots()
    ax5.scatter(df_eda['price'], df_eda['sales'])
    ax5.set_title('Scatter Plot of Price vs Sales')
    ax5.set_xlabel('Price')
    ax5.set_ylabel('Sales')
    st.pyplot(fig5)
    st.write('**Insight:** Patterns in the scatter plot between price and sales could indicate price sensitivity.')
    st.write('**Action:** Test different pricing to see its effect on sales and use this information to formulate an optimal pricing strategy.')

# Model Prediction page
def model():
    st.title('Predict Retail Sales')
    st.write('## Model Prediction')
    st.write('Enter the sales data for the past three months to predict the sales for the upcoming month.')

    # User input
    last_month_sales = st.number_input('Sales Last Month', min_value=0.0, format='%f')
    two_months_ago_sales = st.number_input('Sales 2 Months Ago', min_value=0.0, format='%f')
    three_months_ago_sales = st.number_input('Sales 3 Months Ago', min_value=0.0, format='%f')

    # Load your trained model
    # model = joblib.load('path_to_your_trained_model.pkl')  # Adjust the path to your trained model

    # Predict button
    if st.button('Predict Sales'):
        # prediction = model.predict([[last_month_sales, two_months_ago_sales, three_months_ago_sales]])  # Use your model for prediction
        # st.write(f'Predicted Sales: {prediction[0]}')
        st.write('Predicted Sales: [Your prediction here]')  # Placeholder for actual prediction

# Navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select a page:', ['Home', 'Data Visualization and Storytelling', 'Predict Sales'])

if options == 'Home':
    home()
elif options == 'Data Visualization and Storytelling':
    data_visualization()
elif options == 'Predict Sales':
    model()
