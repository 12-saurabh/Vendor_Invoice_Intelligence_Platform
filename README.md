# 🚀 Vendor Invoice Intelligence Platform

An **AI-powered Vendor Invoice Automation Platform** that digitizes and automates invoice processing using **OCR, Machine Learning, FastAPI, React, PostgreSQL, Redis, Docker, and Kubernetes**.

The platform enables organizations to automatically extract invoice data, validate information, predict invoice risks, automate approval workflows, generate reports, and monitor application performance.

---

# 📌 Project Overview

Traditional invoice processing requires manual data entry, verification, and approval, which is time-consuming and error-prone.

This project provides an intelligent automation solution that:

* Extracts invoice information automatically using OCR
* Processes vendor invoices digitally
* Predicts invoice risks using Machine Learning
* Identifies invoices requiring manual approval
* Provides analytics dashboards
* Generates downloadable reports
* Supports scalable cloud deployment

---

# ✨ Key Features

## 🔐 Authentication & Security

✅ JWT Authentication
✅ Password Hashing
✅ Role Based Access Control
✅ Protected REST APIs
✅ Admin / Accountant / Auditor Roles

---

# 📄 Invoice Management

✅ Invoice Upload
✅ PDF/Image Invoice Processing
✅ OCR Based Data Extraction
✅ Invoice CRUD Operations
✅ Invoice Search
✅ Invoice Status Tracking
✅ Approval Timeline

---

# 🤖 Artificial Intelligence Features

✅ Freight Cost Prediction
✅ Manual Approval Prediction
✅ Invoice Risk Score Generation
✅ AI Assisted Invoice Analysis
✅ ML Model Integration using Scikit-Learn

---

# 🔄 Approval Workflow

✅ Pending Review System
✅ Approve / Reject Workflow
✅ Approval History Tracking
✅ Audit Logs
✅ Role Based Approval Actions

---

# 📊 Dashboard & Analytics

✅ Invoice Statistics Dashboard
✅ Total Invoice Tracking
✅ Amount Analysis
✅ Risk Distribution
✅ Approval Analytics
✅ Vendor Spending Analysis

---

# 📑 Reporting System

✅ CSV Export
✅ Excel Export
✅ PDF Export

---

# ⚡ Real-Time Features

✅ WebSocket Notifications
✅ Redis Integration
✅ Background Processing Support

---

# 🏗 System Architecture

```text
                         Users
                           |
                           |
                    React Frontend
                           |
                           |
                    NGINX Ingress
                           |
                           |
                   FastAPI Backend
                           |
        ------------------------------------------------
        |                     |                       |
        |                     |                       |
 PostgreSQL              Redis Cache             ML Engine
 Database              Queue/Storage          Prediction Models
        |                     |                       |
        ------------------------------------------------
                           |
                           |
                   OCR Processing Pipeline
                           |
                           |
              Invoice Intelligence Engine
                           |
                           |
              Reports / Analytics / Monitoring
```

---

# 🛠 Tech Stack

## Frontend

| Technology   | Purpose            |
| ------------ | ------------------ |
| React        | User Interface     |
| React Router | Navigation         |
| Axios        | API Communication  |
| Recharts     | Data Visualization |
| CSS          | Styling            |

---

## Backend

| Technology | Purpose            |
| ---------- | ------------------ |
| FastAPI    | REST API Framework |
| SQLAlchemy | ORM                |
| Pydantic   | Data Validation    |
| Alembic    | Database Migration |
| JWT        | Authentication     |

---

## Database & Storage

| Technology | Purpose                    |
| ---------- | -------------------------- |
| PostgreSQL | Primary Database           |
| Redis      | Cache and Queue Management |

---

## AI / ML

| Technology    | Purpose              |
| ------------- | -------------------- |
| Python        | Programming Language |
| Scikit-learn  | Machine Learning     |
| Pandas        | Data Processing      |
| NumPy         | Numerical Processing |
| Joblib        | Model Serialization  |
| Tesseract OCR | Invoice Extraction   |

---

## DevOps

| Technology     | Purpose                 |
| -------------- | ----------------------- |
| Docker         | Containerization        |
| Docker Compose | Local Deployment        |
| Kubernetes     | Container Orchestration |
| NGINX Ingress  | Traffic Routing         |
| Prometheus     | Metrics Collection      |
| Grafana        | Monitoring Dashboard    |
| GitHub Actions | CI/CD Pipeline          |

---

# 📂 Project Structure

```text
Vendor_Invoice_Intelligence_Platform/

│
├── backend/
│
│   ├── app/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── auth/
│   │   └── main.py
│   │
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── requirements.txt
│
├── frontend/
│
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── package.json
│
├── kubernetes/
│
│   ├── namespace.yaml
│   ├── secret.yaml
│   ├── backend-deployment.yaml
│   ├── postgres-deployment.yaml
│   ├── redis-deployment.yaml
│   ├── frontend-deployment.yaml
│   └── ingress.yaml
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

# Environment Variables

Create `.env`

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/vendor_invoice_db

REDIS_HOST=localhost

REDIS_PORT=6379

SECRET_KEY=your-secret-key
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

Backend:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# ⚛ Frontend Setup

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Run:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🐳 Docker Deployment

Build and start services:

```bash
docker compose up --build
```

Services:

```text
Frontend

FastAPI Backend

PostgreSQL

Redis

Prometheus

Grafana
```

---

# ☸ Kubernetes Deployment

Apply Kubernetes resources:

```bash
kubectl apply -f kubernetes/
```

Check pods:

```bash
kubectl get pods -n vendor-invoice
```

Check services:

```bash
kubectl get services -n vendor-invoice
```

---

# 📡 API Documentation

Swagger Documentation:

```text
http://localhost:8000/docs
```

Main API Modules:

* Authentication
* Vendors
* Invoices
* Approval Workflow
* Predictions
* Analytics
* Reports
* Notifications
* Admin

---

# 📊 Monitoring

Monitoring Stack:

```text
Prometheus
        |
        |
     Grafana
```

Prometheus:

```text
http://localhost:9090
```

Grafana:

```text
http://localhost:3000
```

---

# 🔄 CI/CD Pipeline

GitHub Actions automatically performs:

✅ Backend validation
✅ Frontend build verification
✅ Docker image build
✅ Continuous Integration

---

# 🤖 Machine Learning Pipeline

Pipeline:

```text
Invoice Document

        |

OCR Extraction

        |

Data Cleaning

        |

Feature Engineering

        |

ML Model

        |

Prediction Result
```

Includes:

* Data preprocessing
* Feature engineering
* Model training
* Model deployment
* Prediction workflow

---

# 🗄 Database Design

Database contains:

* Users
* Vendors
* Invoices
* Approval History
* Audit Logs
* Notifications

Documentation:

`docs/DATABASE.md`

---

# 📸 Screenshots

Add screenshots:

```text
screenshots/

├── login.png
├── dashboard.png
├── invoices.png
├── analytics.png
├── reports.png
├── admin.png
├── grafana.png
```

---

# 🔮 Future Improvements

* Advanced Deep Learning OCR
* Kafka Event Streaming
* MLflow Model Registry
* AWS Cloud Deployment
* Kubernetes Auto Scaling
* Advanced Security Layer
* Email Notifications

---

# 👨‍💻 Author

**Saurabh Kumar**

B.Tech(Information Technology)

National Institute of Technology Raipur

---

# 📜 License

MIT License

---

# ⭐ Project Status

## Production Ready Prototype

Completed:

✅ React Frontend
✅ FastAPI Backend
✅ PostgreSQL Database
✅ Redis Integration
✅ OCR Processing
✅ Machine Learning Pipeline
✅ JWT Authentication
✅ Role Based Access Control
✅ Dashboard & Analytics
✅ Reporting System
✅ WebSocket Notifications
✅ Docker Deployment
✅ Kubernetes Deployment
✅ Prometheus Monitoring
✅ Grafana Dashboard
✅ CI/CD Pipeline
✅ Documentation
