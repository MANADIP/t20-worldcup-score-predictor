# T20 Cricket Score Predictor
 A Machine Learning based web application that predicts the final total score of a T20 cricket match based on match conditions after 5 overs.

This project demonstrates a complete end-to-end ML workflow including data extraction, feature engineering, model training, and deployment using Streamlit.

##  Problem Statement
During a live T20 match, the projected final score is often estimated using only the current run rate (CRR). However, this approach is overly simplistic because it assumes that the scoring rate will remain constant throughout the innings. In reality, the final score depends on many dynamic factors such as the number of wickets fallen, overs remaining, match pressure, and recent scoring momentum. A team that has lost many wickets may slow down, while a team with wickets in hand may accelerate in the final overs. Therefore, relying solely on run rate does not accurately capture the true match situation.

To address this limitation, this project builds a Machine Learning model that considers multiple contextual features instead of depending only on the current run rate. The model incorporates variables such as current score, balls remaining, wickets remaining, recent scoring performance (runs in the last five overs), batting team, bowling team, and venue conditions. By integrating these factors, the model provides a more realistic and situation-aware prediction of the final total score.

##  Dataset

The dataset downloaded from:

 https://www.kaggle.com/datasets/veeralakrishna/cricsheet-a-retrosheet-for-cricket

### Data Files:
- `Ball_Wise_data.csv` – ball-by-ball match data
- `t20s_worldcup_cleaned.csv` – Cleaned and processed dataset

##  Project Workflow

### Data Extraction (`01_data_extraction.ipynb`)
- Cleaned raw cricket data
- Removed unnecessary columns
- Standardized match information
- Selected relevant match statistics

### Feature Engineering (`02_feature_engineering.ipynb`)
Created meaningful features:

- **Balls Left**
- **Wickets Left**
- **Current Run Rate (CRR)**
- **Runs in Last 5 Overs**
- Batting Team
- Bowling Team
- Match City

### Model Training (`03_model_training.ipynb`)
- Used Scikit-learn regression model
- Applied preprocessing pipeline
- Trained on engineered features
- Saved final trained pipeline as: pipe.pkl

---

### Model Deployment (`app.py`)
- Built interactive web app using Streamlit
- User inputs match details
- Model predicts final score instantly
- Displays prediction dynamically
<img width="721" height="743" alt="image" src="https://github.com/user-attachments/assets/d11b9a13-e0da-424e-96cb-33c28b1b3c8d" />


##  Features Used in Final Model
- Batting Team
- Bowling Team
- City
- Current Score
- Balls Left
- Wickets Left
- Current Run Rate (CRR)
- Runs in Last 5 Overs


## Project Structure
<img width="449" height="366" alt="image" src="https://github.com/user-attachments/assets/363fc1b1-a51a-42d2-9cd4-6e8102002a92" />


##  How To Run Locally

### 1) Clone the repository

### 2️) Install dependencies

### 3) Run the Streamlit app
streamlit run app.py/

## Learning Outcomes

This project helped in understanding:

- Real-world data cleaning
- Feature engineering for time-series sports data
- Regression modeling
- Model deployment using Streamlit
- Git and GitHub project structuring

---

## Author

**Manadip Sutradhar**   15/02/2026
M.Sc. Chemistry | Interested in Machine Learning & Data Science





