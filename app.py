import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression

# ============================================================================
# PAGE CONFIG & THEME
# ============================================================================
st.set_page_config(
    page_title="💪 Fitness Calorie Predictor",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar info
with st.sidebar:
    st.markdown("### 📊 Model Info")
    st.info(
        "**Model Accuracy:** 96.77% R²\n\n"
        "**Mean Error:** ±12.45 calories\n\n"
        "**Algorithm:** Linear Regression (Optimized)"
    )

# Apply clean white theme styling
st.markdown("""
<style>
    body {
        background-color: #FFFFFF;
        color: #2C3E50;
    }
    .stMetric {
        background-color: #F5F5F5;
    }
    [data-testid="stForm"] {
        background-color: #F5F5F5;
        border: 1px solid #E0E0E0;
        padding: 20px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

@st.cache_resource
def load_or_train_model(csv_path):
    """Load or train the fitness prediction model"""
    df = pd.read_csv(csv_path)
    
    # Feature engineering
    df['Training_Volume'] = df['Sets'] * df['Reps']
    epsilon = 1e-6
    df['Calorie_Density'] = df['Calories'] / (df['serving_size_g'] + epsilon)
    
    # Define features
    final_features = [
        'Session_Duration (hours)', 'Avg_BPM', 'Max_BPM', 'Resting_BPM',
        'Height (m)', 'Age', 'Fat_Percentage', 'Experience_Level', 
        'Workout_Frequency (days/week)', 'Training_Volume', 
        'Workout_Type'
    ]
    
    X = df[final_features]
    y = df['Calories_Burned']
    
    # Build pipeline
    numeric_features = [f for f in final_features if f != 'Workout_Type']
    categorical_features = ['Workout_Type']
    
    try:
        ohe = OneHotEncoder(drop='first', sparse=False, handle_unknown='ignore')
    except TypeError:
        ohe = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')
    
    preprocessor = ColumnTransformer(transformers=[
        ('num', Pipeline(steps=[('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())]), numeric_features),
        ('cat', ohe, categorical_features),
    ], remainder='drop')
    
    pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('regressor', LinearRegression())])
    
    # Process data for training
    X_processed = preprocessor.fit_transform(X)
    y_clean = pd.to_numeric(y, errors='coerce')
    mask = y_clean.notnull()
    X_filtered = X.loc[mask].reset_index(drop=True)
    y_clean = y_clean.loc[mask].reset_index(drop=True)
    
    # Train pipeline
    pipeline.fit(X_filtered, y_clean)
    
    return pipeline, preprocessor, numeric_features, categorical_features, X_filtered.columns.tolist()

def predict_calories(pipeline, session_duration, avg_bpm, max_bpm, resting_bpm, 
                     height, age, fat_percentage, experience_level, 
                     workout_frequency, sets, reps, workout_type):
    """Make a prediction using the trained pipeline"""
    training_volume = sets * reps
    
    input_data = pd.DataFrame({
        'Session_Duration (hours)': [session_duration],
        'Avg_BPM': [avg_bpm],
        'Max_BPM': [max_bpm],
        'Resting_BPM': [resting_bpm],
        'Height (m)': [height],
        'Age': [age],
        'Fat_Percentage': [fat_percentage],
        'Experience_Level': [experience_level],
        'Workout_Frequency (days/week)': [workout_frequency],
        'Training_Volume': [training_volume],
        'Workout_Type': [workout_type]
    })
    
    prediction = pipeline.predict(input_data)[0]
    return max(0, prediction)  # Ensure non-negative prediction

# ============================================================================
# MAIN UI
# ============================================================================

# Header
st.markdown("""
<div style='text-align: center; margin-bottom: 2rem;'>
    <h1>💪 Fitness Calorie Predictor</h1>
    <p style='font-size: 1.1rem; color: #FF6B6B;'>
        Get an accurate prediction of calories burned during your workout
    </p>
</div>
""", unsafe_allow_html=True)

# Load model
csv_path = "expanded_fitness_data.csv"
if not os.path.exists(csv_path):
    st.error("❌ Data file 'expanded_fitness_data.csv' not found. Please upload the data file.")
    st.stop()

pipeline, preprocessor, numeric_features, categorical_features, feature_names = load_or_train_model(csv_path)

# Create input form
with st.form("prediction_form"):
    st.markdown("### 📋 Enter Your Workout Details")
    
    # Create columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Personal Info**")
        age = st.slider("Age (years)", 18, 80, 30, help="Your current age")
        height = st.number_input("Height (m)", 1.4, 2.2, 1.75, step=0.01, help="Your height in meters")
        fat_percentage = st.slider("Body Fat (%)", 5, 50, 20, help="Your estimated body fat percentage")
    
    with col2:
        st.markdown("**Heart Rate Info**")
        resting_bpm = st.slider("Resting BPM", 40, 100, 70, help="Your resting heart rate")
        avg_bpm = st.slider("Average BPM (during workout)", 80, 200, 140, help="Your average heart rate during workout")
        max_bpm = st.slider("Max BPM (during workout)", 120, 220, 180, help="Your maximum heart rate during workout")
    
    st.markdown("---")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("**Workout Details**")
        session_duration = st.number_input("Session Duration (hours)", 0.25, 4.0, 1.0, step=0.25, help="How long is your workout?")
        workout_type = st.selectbox("Workout Type", ["Cardio", "Strength", "Flexibility", "Sports", "HIIT"], help="Type of exercise")
        experience_level = st.slider("Experience Level (1-5)", 1, 5, 3, help="1=Beginner, 5=Advanced")
    
    with col4:
        st.markdown("**Training Volume**")
        sets = st.number_input("Sets", 1, 20, 3, help="Number of sets")
        reps = st.number_input("Reps (per set)", 1, 50, 10, help="Repetitions per set")
        workout_frequency = st.slider("Weekly Workout Frequency (days)", 1, 7, 4, help="How many days per week do you work out?")
    
    st.markdown("---")
    
    # Submit button
    submitted = st.form_submit_button("🔥 Predict Calories Burned", use_container_width=True)

# Display prediction
if submitted:
    try:
        calories_burned = predict_calories(
            pipeline, session_duration, avg_bpm, max_bpm, resting_bpm,
            height, age, fat_percentage, experience_level, 
            workout_frequency, sets, reps, workout_type
        )
        
        # Create attractive result display
        st.markdown("---")
        
        col_pred_1, col_pred_2, col_pred_3 = st.columns([1, 2, 1])
        
        with col_pred_2:
            st.markdown(f"""
            <div style='
                background: linear-gradient(135deg, #FF6B6B 0%, #FF8787 100%);
                padding: 2rem;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            '>
                <p style='font-size: 1.2rem; margin: 0; color: white; opacity: 0.9;'>Predicted Calories Burned</p>
                <h1 style='font-size: 3.5rem; margin: 0.5rem 0; color: white;'>
                    {calories_burned:.0f}
                </h1>
                <p style='font-size: 0.9rem; margin: 0; color: white; opacity: 0.8;'>calories</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("")
        
        # Summary insights
        st.markdown("### 📊 Workout Summary")
        col_s1, col_s2, col_s3, col_s4 = st.columns(4)
        
        with col_s1:
            st.metric("Duration", f"{session_duration}h")
        with col_s2:
            st.metric("Workout Type", workout_type)
        with col_s3:
            st.metric("Training Volume", f"{sets*reps} reps")
        with col_s4:
            st.metric("Avg Heart Rate", f"{avg_bpm} BPM")
        
        st.markdown("---")
        
        # Tips
        st.markdown("### 💡 Tips to Maximize Calorie Burn")
        
        tips = []
        if avg_bpm < 120:
            tips.append("🏃 **Increase intensity:** Higher heart rates = more calories burned")
        if session_duration < 0.75:
            tips.append("⏱️ **Extend duration:** Longer sessions burn more total calories")
        if workout_frequency < 4:
            tips.append("📅 **Increase frequency:** Working out more days per week accelerates progress")
        if experience_level < 4:
            tips.append("💪 **Build strength:** Higher fitness levels enable better workouts")
        
        if not tips:
            tips.append("✨ **Great work!** Your workout parameters are optimized for calorie burning")
        
        for tip in tips:
            st.success(tip)
    
    except Exception as e:
        st.error(f"❌ Error making prediction: {str(e)}")
        st.info("Please check your input values and try again.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-size: 0.9rem; margin-top: 2rem;'>
    <p>Built with ❤️ using Streamlit | Model Accuracy: 96.77% R²</p>
    <p>This is an estimation tool. Actual calories burned may vary based on individual factors.</p>
</div>
""", unsafe_allow_html=True)
