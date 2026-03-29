# Cloud Auto Scaling Project

## Overview
This project demonstrates local VM monitoring and auto-scaling to cloud when CPU/Memory exceeds 75%.

## Features
- Resource monitoring using Python (psutil)
- Threshold trigger at 75%
- Simulated cloud scaling
- Docker-based application deployment

## Setup

### 1. Install dependencies
pip install -r monitoring/requirements.txt

### 2. Run app locally
cd deployment
docker-compose up

### 3. Start monitoring
cd monitoring
python monitor.py

### 4. Generate load
bash ../scripts/stress.sh

## Architecture
Local VM → Monitoring Script → Threshold Trigger → Cloud Scaling → App Deployment

## Demo Video
https://drive.google.com/file/d/1dMK-R5IS1JMgB7d0WL-Kcp8pYeszg3lG/view?usp=sharing
