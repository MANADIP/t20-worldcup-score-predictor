import streamlit as st
import numpy as np
import pandas as pd
import pickle
st.set_page_config(
    page_title="T20 Score Predictor",
    page_icon="🏏",
    layout="centered"
)
pipe = pickle.load(open('pipe.pkl', 'rb'))
#Model Loading
allowed_teams = [
    'Australia', 'India', 'Bangladesh', 'New Zealand',
    'South Africa', 'England', 'West Indies',
    'Afghanistan', 'Pakistan', 'Sri Lanka',
    'United States of America'
]

eligible_city = [
    'Melbourne', 'Adelaide', 'Mount Maunganui', 'Auckland',
    'Southampton', 'Cardiff', 'Nagpur', 'Bangalore',
    'Lauderhill', 'Dubai', 'Abu Dhabi', 'Sydney',
    'Wellington', 'Hamilton', 'Barbados', 'Trinidad',
    'Colombo', 'St Kitts', 'Manchester', 'Delhi',
    'Lahore', 'Johannesburg', 'Centurion', 'Cape Town',
    'Mumbai', 'Kolkata', 'Durban', 'Chandigarh',
    'Christchurch', 'London', 'Nottingham',
    'St Lucia', 'Pallekele', 'Mirpur', 'Chittagong'
]
st.title("T20 Cricket Score Predictor")
st.markdown("Predict final total score after 6 overs")

st.divider()
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Batting Team", sorted(allowed_teams))

with col2:
    bowling_team = st.selectbox("Bowling Team", sorted(allowed_teams))

if batting_team == bowling_team:
    st.warning("Batting and Bowling team cannot be same.")

city = st.selectbox("Match City", sorted(eligible_city))

st.divider()

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input(
        "Current Score",
        min_value=0,
        max_value=300,
        step=1
    )
with col4:
    overs = st.number_input(
        "Overs Completed (Min 5)",
        min_value=0.0,
        max_value=20.0,
        step=0.1
    )

with col5:
    wickets = st.number_input(
        "Wickets Fallen",
        min_value=0,
        max_value=10,
        step=1
    )

last_five = st.number_input(
    "Runs in Last 5 Overs",
    min_value=0,
    max_value=100,
    step=1
)

st.divider()

# Prediction
if st.button("Predict Final Score"):

    if batting_team == bowling_team:
        st.error("Batting and Bowling team must be different!")

    elif overs < 5:
        st.error("Model works only after 5 overs!")

    else:
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets

        if overs > 0:
            crr = current_score / overs
        else:
            crr = 0

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [city],
            'current_score': [current_score],
            'ball_left': [balls_left],
            'wickets_left': [wickets_left],
            'crr': [crr],
            'last_five': [last_five]
        })

        result = pipe.predict(input_df)

        st.success(f"Predicted Final Score: {int(result[0])}")
