# 🎨 Customization Guide

## Colors & Theme

Edit `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#FF6B6B"           # Red accent (change this for different theme)
backgroundColor = "#FFFFFF"        # White background
secondaryBackgroundColor = "#F5F5F5" # Light gray for cards
textColor = "#2C3E50"              # Dark text color
font = "sans serif"
```

### Suggested Color Schemes

**Blue Theme** (Tech-forward)
```toml
primaryColor = "#3498DB"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#ECF0F1"
textColor = "#2C3E50"
```

**Green Theme** (Health-focused)
```toml
primaryColor = "#2ECC71"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0FFF4"
textColor = "#27AE60"
```

**Purple Theme** (Modern)
```toml
primaryColor = "#9B59B6"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F4ECF7"
textColor = "#6C3483"
```

---

## App Configuration

Edit `app.py` to customize:

### 1. Change App Title & Icon
```python
st.set_page_config(
    page_title="💪 Custom App Name",  # Change this
    page_icon="💪",                    # Change emoji
    layout="wide",
    initial_sidebar_state="expanded"
)
```

### 2. Modify Default Values
```python
# In the form section, change defaults:
age = st.slider("Age (years)", 18, 80, 35, help="...")  # Default: 35
height = st.number_input("Height (m)", 1.4, 2.2, 1.80, step=0.01)  # Default: 1.80
fat_percentage = st.slider("Body Fat (%)", 5, 50, 25, help="...")  # Default: 25
```

### 3. Adjust Input Ranges
```python
# Make ranges stricter or wider:
avg_bpm = st.slider("Average BPM", 50, 250, 140)  # Changed from 80-200
session_duration = st.number_input("Duration (hours)", 0.1, 5.0, 1.0)  # Extended range
```

### 4. Change Workout Types
```python
workout_type = st.selectbox("Workout Type", [
    "Cardio", "Strength", "Flexibility", "Sports", "HIIT",
    "Yoga",  # Add new
    "Pilates",  # Add new
], help="...")
```

### 5. Modify Tips Logic
Edit the tips section:
```python
tips = []
if avg_bpm < 120:
    tips.append("🏃 Your custom tip here")
if session_duration < 0.75:
    tips.append("⏱️ Another custom tip")
```

---

## Docker Customization

### Change Port

Edit `docker-compose.yml`:
```yaml
ports:
  - "8502:8501"  # Access on http://localhost:8502
```

Or in `Dockerfile`:
```dockerfile
EXPOSE 8502
```

### Add Environment Variables

In `docker-compose.yml`:
```yaml
environment:
  - STREAMLIT_SERVER_HEADLESS=true
  - CUSTOM_VAR="value"  # Add custom variables
```

### Change Base Python Image

In `Dockerfile`:
```dockerfile
FROM python:3.11-slim  # Change version (3.9, 3.10, 3.12)
```

---

## Input Form Customization

### Add New Input Fields

```python
# In the form, add:
injury_status = st.selectbox("Any Injuries?", ["None", "Back", "Knee", "Shoulder"])
motivation_level = st.slider("Motivation (1-10)", 1, 10, 5)
```

### Change Input Types

```python
# Slider instead of number input:
training_experience = st.slider("Years of Experience", 0, 30, 5)

# Text input:
fitness_goal = st.text_input("What's your fitness goal?")

# Checkbox:
is_beginner = st.checkbox("I'm new to fitness")
```

### Reorder Form Sections

```python
# Simply move the col1, col2, col3 sections around
# Or create new column layouts:
col_a, col_b, col_c, col_d = st.columns(4)
```

---

## Results Display Customization

### Change Result Card Color

In `app.py`, modify the gradient:
```python
st.markdown(f"""
<div style='
    background: linear-gradient(135deg, #3498DB 0%, #5DADE2 100%);  # Blue gradient
    padding: 2rem;
    border-radius: 15px;
    ...
</div>
""", unsafe_allow_html=True)
```

### Add More Metrics

```python
col_s1, col_s2, col_s3, col_s4, col_s5 = st.columns(5)  # Add 5th column

with col_s1:
    st.metric("Duration", f"{session_duration}h")
with col_s2:
    st.metric("Workout Type", workout_type)
with col_s3:
    st.metric("Training Volume", f"{sets*reps} reps")
with col_s4:
    st.metric("Avg Heart Rate", f"{avg_bpm} BPM")
with col_s5:
    st.metric("Experience", f"Level {experience_level}")
```

---

## Model Customization

### Use Different Input Ranges

The model works best with these ranges:
- Age: 18-80
- Heart Rate: 40-220
- Duration: 0.25-4 hours

You can extend, but accuracy may vary.

### Add/Remove Features

To add features, you need to retrain with your notebook:
1. Edit `fitness_linear_reg.ipynb`
2. Add new features to `final_features` list
3. Retrain the model
4. Update `app.py` with new inputs
5. Re-commit and redeploy

---

## Sidebar Customization

Change model info display:
```python
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    theme = st.radio("Select Theme:", ["🌙 Dark", "☀️ Light"])
    
    st.markdown("---")
    st.markdown("### 📊 Model Info")
    st.info(
        "**Model Accuracy:** 96.77% R²\n\n"
        "**Mean Error:** ±12.45 calories\n\n"
        "**Algorithm:** Linear Regression"
    )
    
    # Add your custom section:
    st.markdown("### ℹ️ About")
    st.write("Custom info here")
```

---

## Footer Customization

Edit the footer section:
```python
st.markdown("""
<div style='text-align: center; color: #888; font-size: 0.9rem;'>
    <p>Built with ❤️ using Streamlit | Model Accuracy: 96.77% R²</p>
    <p>Your custom message here</p>
</div>
""", unsafe_allow_html=True)
```

---

## Advanced CSS Customization

Add custom CSS at the top of `app.py`:
```python
st.markdown("""
<style>
    /* Custom button styling */
    .stButton > button {
        background-color: #FF6B6B;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
    }
    
    /* Custom metric styling */
    .metric-card {
        background-color: #F5F5F5;
        padding: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)
```

---

## Deployment Customization

### Change App Name in Cloud

Update `README.md` title and description before deploying.

### Add Custom Domain

On Streamlit Cloud:
1. Go to app settings
2. Domain Management
3. Configure custom domain (requires DNS setup)

---

## Example: Full Green Health Theme

Here's a complete customization for a "Health & Wellness" theme:

**`.streamlit/config.toml`:**
```toml
[theme]
primaryColor = "#27AE60"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0FFF4"
textColor = "#145A32"
font = "sans serif"
```

**`app.py` title change:**
```python
st.set_page_config(
    page_title="🌱 Health Fitness Tracker",
    page_icon="🌱",
    layout="wide"
)
```

**Result card gradient:**
```python
background: linear-gradient(135deg, #27AE60 0%, #58D68D 100%);
```

---

## Tips for Customization

1. **Test locally first**: Always test changes locally before pushing
   ```bash
   streamlit run app.py
   ```

2. **Keep backups**: Before major changes, commit current version:
   ```bash
   git commit -am "Backup before customization"
   ```

3. **Use design tools**: Plan colors at [colorhexa.com](https://www.colorhexa.com)

4. **Mobile responsive**: Test on mobile before deploying

5. **Accessibility**: Ensure good contrast ratios for text

6. **User testing**: Get feedback before finalizing design

---

## Quick Customization Checklist

- [ ] Change color scheme in `.streamlit/config.toml`
- [ ] Update app title and icon
- [ ] Modify form inputs as needed
- [ ] Customize tips and recommendations
- [ ] Update README with your changes
- [ ] Test locally: `streamlit run app.py`
- [ ] Commit changes: `git add . && git commit -m "Customize app"`
- [ ] Push to GitHub: `git push origin main`
- [ ] Redeploy on Streamlit Cloud

---

**Need help? Check the Streamlit docs: https://docs.streamlit.io**
