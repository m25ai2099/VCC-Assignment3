#!/bin/bash

echo "🚀 Simulating cloud scaling..."

# Example: AWS CLI (replace with your real command if configured)
# aws ec2 run-instances --image-id ami-123456 --count 1 --instance-type t2.micro

# For demo:
echo "New cloud instance would be created here."

# Deploy app (simulate)
cd ../deployment
docker-compose up -d

echo "✅ Application deployed to cloud (simulated)"
