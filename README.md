# 🚀 Vendor Invoice Intelligence Platform

An AI-powered invoice automation platform that digitizes vendor invoice processing using OCR, Machine Learning, FastAPI, PostgreSQL, Redis, Docker, and Kubernetes.

The platform automates invoice extraction, validation, prediction, approval workflow, analytics, and reporting.


---

# 📌 Project Overview


Traditional invoice processing requires manual data entry and verification.

This project provides an intelligent automation system that:

- Extracts invoice information automatically
- Predicts invoice risks
- Identifies invoices requiring manual approval
- Manages vendor invoices
- Provides dashboards and analytics
- Supports scalable cloud deployment


---

# ✨ Key Features


## 🔐 Authentication & Security

✅ JWT Authentication

✅ Password Hashing

✅ Role Based Access Control

✅ Protected APIs


---

## 📄 Invoice Management

✅ Invoice Upload

✅ PDF/Image Processing

✅ OCR Based Data Extraction

✅ Invoice Search

✅ Invoice Status Tracking


---

## 🤖 Machine Learning Features

✅ Freight Cost Prediction

✅ Manual Approval Prediction

✅ Risk Score Generation

✅ AI Assisted Invoice Analysis


---

## 🔄 Approval Workflow

✅ Pending Review

✅ Approval/Rejection System

✅ Approval History Tracking

✅ Audit Logs


---

## 📊 Analytics & Reporting

✅ Dashboard APIs

✅ Invoice Statistics

✅ Export Reports

✅ Performance Tracking


---

## ⚡ Real-Time Features

✅ Redis Integration

✅ Notification System

✅ Background Processing Support


---

# 🏗 System Architecture


```text
                         Client
                            |
                            |
                     NGINX Ingress
                            |
                            |
                    FastAPI Backend
                            |
        ------------------------------------------------
        |                      |                       |
        |                      |                       |
   PostgreSQL               Redis                 ML Model
   Database                Cache              Prediction Engine
        |                      |                       |
        ------------------------------------------------
                            |
                            |
                  OCR Processing Pipeline
                            |
                            |
              Invoice Processing Engine
                            |
                            |
                Reports / Analytics
```


Detailed architecture:

[Architecture Documentation](docs/ARCHITECTURE.md)


---

# 🛠 Tech Stack


## Backend

| Technology | Purpose |
|-|-|
|FastAPI|REST API Framework|
|SQLAlchemy|ORM|
|Pydantic|Data Validation|
|Alembic|Database Migration|
|JWT|Authentication|


---

## Database & Storage

|Technology|Purpose|
|-|-|
|PostgreSQL|Primary Database|
|Redis|Caching & Queue Management|


---

## AI / ML

|Technology|Purpose|
|-|-|
|Python|Programming Language|
|Scikit-learn|Machine Learning|
|Pandas|Data Processing|
|NumPy|Numerical Processing|
|Joblib|Model Serialization|
|Tesseract OCR|Document Extraction|


---

## DevOps

|Technology|Purpose|
|-|-|
|Docker|Containerization|
|Docker Compose|Local Deployment|
|Kubernetes|Container Orchestration|
|NGINX Ingress|Traffic Routing|
|Prometheus|Monitoring|
|Grafana|Visualization|
|GitHub Actions|CI/CD|


---

# 📂 Project Structure


```text
Vendor_Invoice_Intelligence_Platform/

│
├── backend/
│
│   ├── app/
│   │
│   ├── models/
│   │
│   ├── routers/
│   │
│   ├── services/
│   │
│   ├── Dockerfile
│   │
│   └── requirements.txt
│
│
├── k8s/
│
│   ├── namespace.yaml
│   ├── secret.yaml
│   ├── backend-deployment.yaml
│   ├── postgres-deployment.yaml
│   ├── redis-deployment.yaml
│   └── ingress.yaml
│
│
├── docs/
│
│   ├── ARCHITECTURE.md
│   ├── API.md
│   ├── DEPLOYMENT.md
│   ├── MONITORING.md
│   ├── ML_PIPELINE.md
│   └── DATABASE.md
│
│
└── README.md
```


---

# ⚙️ Installation & Setup


## Clone Repository


```bash
git clone https://github.com/12-saurabh/Vendor_Invoice_Intelligence_Platform.git

cd Vendor_Invoice_Intelligence_Platform
```


---

# 🐍 Backend Setup


Go to backend:


```bash
cd backend
```


Create virtual environment:


```bash
python -m venv venv
```


Activate:


Windows:

```bash
venv\Scripts\activate
```


Install dependencies:


```bash
pip install -r requirements.txt
```


---

# 🗄 Database Setup


Run migrations:


```bash
alembic upgrade head
```


---

# ▶ Run Backend


```bash
uvicorn app.main:app --reload
```


Application:

```text
http://127.0.0.1:8000
```


Swagger:


```text
http://127.0.0.1:8000/docs
```


---

# 🐳 Docker Deployment


Build image:


```bash
docker build -t vendor-backend .
```


Run using Docker Compose:


```bash
docker compose up
```


Services:


```text
FastAPI

PostgreSQL

Redis
```


---

# ☸ Kubernetes Deployment


Start Kubernetes cluster.


Apply resources:


```bash
kubectl apply -f k8s/namespace.yaml

kubectl apply -f k8s/secret.yaml

kubectl apply -f k8s/postgres-pvc.yaml

kubectl apply -f k8s/postgres-deployment.yaml

kubectl apply -f k8s/redis-deployment.yaml

kubectl apply -f k8s/backend-deployment.yaml

kubectl apply -f k8s/ingress.yaml
```


Check:


```bash
kubectl get pods -n vendor-invoice
```


---

# 📡 API Documentation


Complete API documentation:

[API Documentation](docs/API.md)


Swagger UI:


```text
/docs
```


---

# 📊 Monitoring


Monitoring stack:


```text
Prometheus

Grafana
```


Documentation:

[Monitoring Documentation](docs/MONITORING.md)


---

# 🤖 Machine Learning Pipeline


ML documentation:

[ML Pipeline Documentation](docs/ML_PIPELINE.md)


Includes:

- Data preprocessing
- Feature engineering
- Model training
- Prediction workflow


---

# 🗄 Database Design


Database documentation:

[Database Documentation](docs/DATABASE.md)


Includes:

- Tables
- Relationships
- Migration strategy


---

# 🚀 Deployment Documentation


Complete deployment guide:

[Deployment Documentation](docs/DEPLOYMENT.md)


---

# 🔮 Future Improvements


Planned features:


- Advanced Deep Learning OCR

- Kafka based event processing

- MLflow Model Registry

- Cloud Deployment on AWS

- Kubernetes Horizontal Pod Autoscaling

- Advanced Security Layer


---

# 👨‍💻 Author


**Saurabh Kumar**

B.Tech Information Technology

National Institute of Technology Raipur


---

# 📜 License


This project is licensed under the MIT License.


---

# ⭐ Project Status


## Production Ready


Completed:

✅ FastAPI Backend

✅ PostgreSQL Database

✅ Redis Integration

✅ OCR Processing

✅ Machine Learning Pipeline

✅ JWT Authentication

✅ Docker Deployment

✅ Kubernetes Deployment

✅ Monitoring Setup

✅ Complete Documentation
