# 🚀 Deployment Documentation

# Vendor Invoice Intelligence Platform

This document explains how to deploy the Vendor Invoice Intelligence Platform using:

- Local Development
- Docker
- Docker Compose
- Kubernetes
- NGINX Ingress


---

# Deployment Architecture


```text
Developer

    |
    |

GitHub Repository

    |
    |

Docker Image Build

    |
    |

Container Registry

    |
    |

Kubernetes Cluster

    |
    |

Production Application
```


---

# 1. Local Development Deployment


## Requirements


Install:


```text
Python 3.11+

PostgreSQL 16+

Redis 7+

Tesseract OCR

Git
```


---

## Clone Repository


```bash
git clone https://github.com/12-saurabh/Vendor_Invoice_Intelligence_Platform.git

cd Vendor_Invoice_Intelligence_Platform/backend
```


---

## Create Virtual Environment


Windows:


```bash
python -m venv venv

venv\Scripts\activate
```


Linux/macOS:


```bash
python3 -m venv venv

source venv/bin/activate
```


---

## Install Dependencies


```bash
pip install -r requirements.txt
```


---

## Configure Environment Variables


Create:

```text
.env
```


Example:


```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/vendor_invoice_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

MAIL_USERNAME=email@gmail.com

MAIL_PASSWORD=password

REDIS_HOST=localhost

REDIS_PORT=6379
```


---

## Run Database Migration


```bash
alembic upgrade head
```


---

## Start Backend


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

# 2. Docker Deployment


## Build Docker Image


Navigate to backend folder:


```bash
cd backend
```


Build:


```bash
docker build -t vendor-backend .
```


Check image:


```bash
docker images
```


---

## Run Backend Container


```bash
docker run -d \
--name vendor-api \
-p 8000:8000 \
--env-file .env \
vendor-backend
```


Check container:


```bash
docker ps
```


Logs:


```bash
docker logs vendor-api
```


---

# 3. Docker Compose Deployment


Docker Compose runs:


```text
FastAPI Backend

PostgreSQL Database

Redis Cache
```


---

## Start Services


```bash
docker compose up -d
```


Check services:


```bash
docker compose ps
```


---

## Stop Services


```bash
docker compose down
```


---

## View Logs


Backend:


```bash
docker compose logs backend
```


PostgreSQL:


```bash
docker compose logs postgres
```


Redis:


```bash
docker compose logs redis
```


---

# 4. Kubernetes Deployment


The application is deployed using Kubernetes.


Kubernetes resources:


```text
Namespace

Secrets

Deployments

Services

Persistent Volume

Ingress
```


---

# Create Namespace


```bash
kubectl apply -f k8s/namespace.yaml
```


Verify:


```bash
kubectl get namespaces
```


---

# Create Secrets


```bash
kubectl apply -f k8s/secret.yaml
```


Verify:


```bash
kubectl get secrets -n vendor-invoice
```


---

# Deploy PostgreSQL


Apply:


```bash
kubectl apply -f k8s/postgres-pvc.yaml

kubectl apply -f k8s/postgres-deployment.yaml

kubectl apply -f k8s/postgres-service.yaml
```


Check:


```bash
kubectl get pods -n vendor-invoice
```


Expected:


```text
postgres   Running
```


---

# Deploy Redis


Apply:


```bash
kubectl apply -f k8s/redis-deployment.yaml

kubectl apply -f k8s/redis-service.yaml
```


Check:


```bash
kubectl get pods -n vendor-invoice
```


---

# Deploy Backend


Apply:


```bash
kubectl apply -f k8s/backend-deployment.yaml

kubectl apply -f k8s/backend-service.yaml
```


Verify:


```bash
kubectl get pods -n vendor-invoice
```


Expected:


```text
backend   Running
```


---

# 5. Kubernetes Service Architecture


```text
                 Client

                    |

                    |

             NGINX Ingress

                    |

                    |

             Backend Service

                    |

                    |

             FastAPI Pods


        --------------------------

        |                        |

 PostgreSQL Service        Redis Service
```


---

# 6. Install NGINX Ingress


Install:


```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```


Check:


```bash
kubectl get pods -n ingress-nginx
```


Expected:


```text
ingress-nginx-controller Running
```


---

# 7. Configure Ingress


Apply:


```bash
kubectl apply -f k8s/ingress.yaml
```


Verify:


```bash
kubectl get ingress -n vendor-invoice
```


---

# 8. Local Domain Setup


Add entry in Windows hosts file:


Location:


```text
C:\Windows\System32\drivers\etc\hosts
```


Add:


```text
127.0.0.1 invoice.local
```


Test:


```bash
ping invoice.local
```


---

# 9. Access Application


Swagger:


```text
http://invoice.local/docs
```


API:


```text
http://invoice.local
```


---

# 10. Production Deployment Checklist


Before production:


```text
✓ Environment variables configured

✓ Database migrations completed

✓ Docker images built

✓ Kubernetes resources deployed

✓ Secrets configured

✓ Monitoring enabled

✓ Logs verified

✓ Health checks working
```


---

# 11. Troubleshooting


## Check Pods


```bash
kubectl get pods -n vendor-invoice
```


---

## Check Logs


```bash
kubectl logs <pod-name> -n vendor-invoice
```


---

## Describe Resource


```bash
kubectl describe pod <pod-name> -n vendor-invoice
```


---

# Summary


The platform supports:


✅ Local deployment

✅ Docker deployment

✅ Docker Compose deployment

✅ Kubernetes deployment

✅ Ingress routing

✅ Production-ready infrastructure