# Flask Application Deployment using Docker and Kubernetes

## Overview

This project demonstrates the complete deployment lifecycle of a Flask application using Docker and Kubernetes.

## Technologies Used

* Python (Flask)
* Docker
* Docker Hub
* Kubernetes (Minikube)
* YAML
* Git/GitHub

## Architecture

Flask Application
↓
Docker Image
↓
Docker Hub
↓
Kubernetes Deployment
↓
ReplicaSet
↓
Pods
↓
Kubernetes Service
↓
Browser Access

## Features

* Containerized Flask application
* Docker image published to Docker Hub
* Kubernetes Deployment with 3 replicas
* Self-healing capability through Kubernetes
* Service exposure using NodePort

## Commands Used

Build Docker image:

docker build -t YOUR_USERNAME/flask-k8s-project:v1 .

Push image:

docker push YOUR_USERNAME/flask-k8s-project:v1

Deploy application:

kubectl apply -f deployment.yaml

Expose application:

kubectl apply -f service.yaml

Access application:

minikube service flask-service
