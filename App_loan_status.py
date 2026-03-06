import streamlit as st
import joblib
import numpy as np
import pandas as pd

try:
    model = joblib.load('model_loan.pkl')
except:
    st.error("file model not exists 'model_loan.joblib' ⚠️")

st.title("Loan Forecasting System 💳")

col1, col2 = st.columns(2)

with col1:
    person_age = st.number_input("person_age", value=30)
    person_gender = st.number_input("person_gender (0 or 1)", value=0)
    person_education = st.number_input("person_education (numerical)", value=1)
    person_income = st.number_input("person_income", value=50000.0)
    person_emp_exp = st.number_input("person_emp_exp", value=5.0)
    person_home_ownership = st.number_input("person_home_ownership (numerical)", value=1)

with col2:
    loan_amnt = st.number_input("loan_amnt", value=10000.0)
    loan_intent = st.number_input("loan_intent (numerical)", value=2)
    loan_int_rate = st.number_input("loan_int_rate", value=11.0)
    loan_percent_income = st.number_input("loan_percent_income", value=0.1)
    cb_person_cred_hist_length = st.number_input("cb_person_cred_hist_length", value=3.0)
    credit_score = st.number_input("credit_score", value=650)

previous_loan_defaults_on_file = st.number_input("previous_loan_defaults_on_file (0 or 1)", value=0)

if st.button("Predict"):
    if person_age<18:
        st.error("Result : Rejected Age Is Below Legal Requirement Under 18 ❌ ")
    else:
        features = np.array([[
            person_age, 
            person_gender, 
            person_education, 
            person_income,
            person_emp_exp, 
            person_home_ownership, 
            loan_amnt, 
            loan_intent,
            loan_int_rate, 
            loan_percent_income, 
            cb_person_cred_hist_length,
            credit_score, 
            previous_loan_defaults_on_file
    ]])

    prediction = model.predict(features)
    
    st.divider()
    if prediction[0] == 1:
        st.success("Result : You Can Take The Loan (Approved) ✅")
    else:
        st.error("Result : You Can't Take The Loan (Rejected) ❌")