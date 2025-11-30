# 🚀 Deployment Guide - Fitness Calorie Predictor

## Quick Start

### Option 1: Local Development (Fastest)

```bash
cd /Users/mac/Documents/Tech_projects/fitness_app
python -m streamlit run app.py
```

Open browser to: `http://localhost:8501`

---

## Docker Deployment

### Local Testing with Docker

```bash
# Using docker-compose (recommended)
docker-compose up --build

# OR manually
docker build -t fitness-predictor .
docker run -p 8501:8501 fitness-predictor
```

### Push to Docker Hub (Optional)

```bash
# Login to Docker Hub
docker login

# Tag image
docker tag fitness-predictor YOUR_USERNAME/fitness-predictor:latest

# Push
docker push YOUR_USERNAME/fitness-predictor:latest
```

---

## 🌐 Deploy to Streamlit Cloud (FREE - RECOMMENDED)

### Step 1: Prepare GitHub Repository

```bash
cd /Users/mac/Documents/Tech_projects/fitness_app

# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit: Fitness Calorie Predictor app"

# Add remote (if not already)
git remote add origin https://github.com/HiNacho/fitness_app.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to [**share.streamlit.io**](https://share.streamlit.io)
2. Click **"New app"** button
3. Sign in with GitHub (if prompted)
4. Select:
   - **Repository**: `HiNacho/fitness_app`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click **"Deploy"**

### Step 3: Configuration (if needed)

Streamlit Cloud will automatically detect your `requirements.txt` and install dependencies.

For custom settings, create `.streamlit/secrets.toml` in the root (for sensitive data only):

```toml
# Example if you need API keys in future
# api_key = "your_key_here"
```

---

## 🐋 Deploy to Other Platforms

### Heroku (Note: Free tier discontinued, paid only)

```bash
# Install Heroku CLI, then:
heroku login
heroku create fitness-calorie-predictor
heroku config:set BUILDPACK_URL=https://github.com/heroku/heroku-buildpack-python
git push heroku main
```

### AWS EC2

```bash
# SSH into EC2 instance
ssh -i your-key.pem ec2-user@your-instance-ip

# Clone repository
git clone https://github.com/HiNacho/fitness_app.git
cd fitness_app

# Install Docker
sudo yum update -y
sudo yum install -y docker
sudo service docker start

# Run app
docker-compose up -d
```

Access at: `http://your-instance-ip:8501`

### Google Cloud Run

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Build and deploy
gcloud run deploy fitness-predictor \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8501
```

### DigitalOcean App Platform

1. Go to DigitalOcean Dashboard
2. Click **"Create"** → **"Apps"**
3. Connect GitHub repository
4. Set main file to `app.py`
5. Deploy

---

## 📋 File Structure for Deployment

```
fitness_app/
├── app.py                           # Main app (must be here)
├── expanded_fitness_data.csv        # Training data (must be here)
├── requirements.txt                 # Python dependencies (required)
├── Dockerfile                       # Docker config (optional, auto-detected)
├── docker-compose.yml               # Docker Compose (optional)
├── .streamlit/config.toml          # Streamlit config (optional)
├── .gitignore                       # Git ignore rules
├── README.md                        # Documentation
└── start.sh                         # Local startup script
```

---

## 🔐 Security Considerations

1. **Never commit secrets** to GitHub
2. Use environment variables for sensitive data
3. In Streamlit Cloud, set secrets in:
   - Dashboard → App settings → Secrets

Example `.streamlit/secrets.toml`:
```toml
[database]
connection_string = "your_connection_string"
api_key = "your_api_key"
```

Access in app:
```python
import streamlit as st
api_key = st.secrets["api_key"]
```

---

## 🌍 Environment Variables

For Docker/Cloud deployments, you can set:

```bash
# Optional - defaults provided
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_CLIENT_LOGGER_LEVEL=error
```

---

## 📊 Monitoring & Logs

### Local
```bash
# View logs
docker-compose logs -f
```

### Streamlit Cloud
- Go to app settings
- Click "Manage app" → "View logs"

### Docker Hub / Cloud Platforms
- Use platform-specific logging dashboards

---

## ✅ Deployment Checklist

- [ ] All files committed to Git
- [ ] `requirements.txt` updated
- [ ] `expanded_fitness_data.csv` in root directory
- [ ] `app.py` has correct path to data file
- [ ] GitHub repository is public (for Streamlit Cloud)
- [ ] No hardcoded secrets in code
- [ ] Dockerfile tested locally
- [ ] README.md updated with deployment info

---

## 🆘 Troubleshooting

### App won't start
```bash
# Check Python version
python --version  # Should be 3.9+

# Verify dependencies
pip list | grep streamlit

# Test imports
python -c "import streamlit; print(streamlit.__version__)"
```

### Data file not found
```bash
# Ensure file is in same directory as app.py
ls -la expanded_fitness_data.csv

# Update app.py path if needed:
df = pd.read_csv("./expanded_fitness_data.csv")
```

### Port already in use
```bash
# Change port in docker-compose.yml or run:
streamlit run app.py --server.port 8502
```

### Streamlit Cloud deployment fails
1. Check GitHub repository is public
2. Verify `requirements.txt` syntax
3. Check `app.py` path is correct
4. Review deployment logs in Streamlit Cloud dashboard

---

## 📞 Support Resources

- Streamlit Docs: https://docs.streamlit.io
- Docker Docs: https://docs.docker.com
- Streamlit Cloud: https://share.streamlit.io/docs/deploy/run-an-app

---

**Ready to deploy? Start with Streamlit Cloud - it's the easiest option! ☁️**
