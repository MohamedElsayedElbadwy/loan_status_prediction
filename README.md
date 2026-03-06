Loan Status Prediction
This project focuses on building a machine learning model to automate the loan approval process. By analyzing customer data,
the model predicts whether a loan application should be approved or rejected based on several financial and personal indicators.

Project Overview
The main goal is to help financial institutions minimize the risk of defaults by identifying high-risk applicants early in the process. 
The project covers the entire pipeline, from data cleaning and exploration (EDA) to model deployment.

File Structure
 * loan_data.csv: The raw dataset containing customer records (Income, Credit History, Education, etc.).
 * loan_status.ipynb: Jupyter notebook containing the analysis, data visualization, and model training steps.
 * model_loan.pkl: The trained model exported as a pickle file for production use.
 * App_loan_status.py: A Python script to run the web interface for the prediction tool.
 * requirements.txt: List of dependencies needed to run the project.

How to Run
 * Clone the repo:
   git clone https://github.com/MohamedElsayedElbadwy/loan_status_prediction.git

 * Install dependencies:
   pip install -r Requirements.txt

 * Launch the app:
   streamlit run App_loan_status.py

Key Features
 * Data preprocessing and handling missing values.
 * Feature engineering to improve model accuracy.
 * Interactive web dashboard for real-time predictions.
Author
Mohamed Elsayed Elbadwy GitHub Profile
