#!/bin/bash

# Fitness Calorie Predictor - Startup Script

echo "🏋️  Fitness Calorie Predictor"
echo "================================"
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "⚠️  Docker not found. Installing locally..."
    pip install -r requirements.txt
    streamlit run app.py
else
    echo "✅ Docker found. Starting with Docker Compose..."
    echo ""
    docker-compose up --build
fi
