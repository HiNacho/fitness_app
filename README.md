# 💪 Fitness Calorie Predictor

A beautiful, modern Streamlit web application that predicts calories burned during workouts using machine learning. Get instant, accurate estimates of calorie expenditure based on your workout parameters.

## ✨ Features

- 🎯 **Accurate Predictions**: 96.77% R² accuracy with ±12.45 calorie mean error
- 🌓 **Dark & Light Themes**: Toggle between dark and light modes for comfortable viewing
- 📊 **Beautiful UI**: Clean, modern, and intuitive interface
- 💡 **Smart Tips**: Personalized suggestions to maximize calorie burn
- 🚀 **Docker Ready**: Easily containerized and deployable
- ☁️ **Streamlit Cloud Compatible**: Deploy for free on Streamlit Cloud

## 🤖 Model Details

**Algorithm**: Scikit-learn Linear Regression with preprocessing pipeline
- **Features**: 11 input parameters (personal info, heart rate, workout details)
- **Performance**: Cross-validated with 5-Fold CV
- **Preprocessing**: Median imputation, standard scaling, and one-hot encoding

### Input Parameters
- Age, Height, Body Fat Percentage
- Resting BPM, Average BPM, Max BPM
- Session Duration, Workout Type
- Experience Level, Weekly Frequency
- Training Volume (Sets × Reps)

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose (recommended)
- OR Python 3.11+

### Option 1: Run with Docker (Recommended)

```bash
cd /Users/mac/Documents/Tech_projects/fitness_app
docker-compose up --build
```

Access the app at: `http://localhost:8501`

### Option 2: Run Locally (Python)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Access the app at: `http://localhost:8501`

## 📦 Project Structure

```
fitness_app/
├── app.py                           # Main Streamlit application
├── expanded_fitness_data.csv        # Training data
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker container configuration
├── docker-compose.yml               # Docker Compose setup
├── .streamlit/
│   └── config.toml                 # Streamlit configuration
└── README.md                        # This file
```

## 🐳 Docker Commands

### Build Image
```bash
docker build -t fitness-predictor .
```

### Run Container
```bash
docker run -p 8501:8501 \
  -v $(pwd)/expanded_fitness_data.csv:/app/expanded_fitness_data.csv \
  fitness-predictor
```

### Using Docker Compose (Recommended)
```bash
# Start
docker-compose up

# Stop
docker-compose down

# Rebuild
docker-compose up --build
```

## ☁️ Deploy to Streamlit Cloud

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add Fitness Calorie Predictor app"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Select this repository
   - Choose branch: `main`
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Configure in Streamlit Cloud**
   - No additional configuration needed
   - The app will auto-detect and use your local theme setting

## 🎨 Theme Customization

The app includes two built-in themes:

- **Dark Theme** 🌙: Perfect for low-light environments
- **Light Theme** ☀️: Classic bright interface

Users can toggle themes in the sidebar settings while using the app.

## 📝 Usage

1. **Enter Personal Information**: Age, height, body fat percentage
2. **Input Heart Rate Data**: Resting and workout BPMs
3. **Specify Workout Details**: Duration, type, experience level
4. **Set Training Volume**: Number of sets and reps
5. **Get Prediction**: Click "Predict Calories Burned" for instant results

The app provides:
- Predicted calories burned
- Workout summary metrics
- Personalized tips based on your inputs

## 🔧 Technologies Used

- **Frontend**: Streamlit 1.31.1
- **ML Framework**: Scikit-learn 1.3.2
- **Data Processing**: Pandas 2.1.4, NumPy 1.24.3
- **Container**: Docker
- **Deployment**: Streamlit Cloud / Docker

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| R² Score | 0.9677 (96.77%) |
| Mean Absolute Error | 12.45 calories |
| Cross-Validation Folds | 5 |
| Training Samples | 300+ |

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## 📧 Contact & Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Built with ❤️ using Streamlit**

*Note: This is an estimation tool. Actual calories burned may vary based on individual factors such as metabolism, fitness level, and body composition.*
