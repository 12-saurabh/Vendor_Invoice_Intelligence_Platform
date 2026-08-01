# 📡 API Documentation

# Vendor Invoice Intelligence Platform API

This document describes the REST API endpoints provided by the Vendor Invoice Intelligence Platform.

The backend is developed using:

- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication
- Pydantic Schemas


---

# Base URL

Local Development:

```text
http://127.0.0.1:8000
```

Kubernetes Deployment:

```text
http://invoice.local
```


---

# API Documentation Interface

FastAPI automatically provides interactive documentation.


## Swagger UI

```text
/docs
```

Example:

```text
http://127.0.0.1:8000/docs
```


## ReDoc

```text
/redoc
```

Example:

```text
http://127.0.0.1:8000/redoc
```


---

# Authentication

The platform uses JWT based authentication.


Authentication Flow:

```text
User Login

     |

Credentials Validation

     |

JWT Token Generated

     |

Token Used For Protected APIs
```


JWT Header:


```http
Authorization: Bearer <access_token>
```


---

# 1. Authentication APIs


## Register User


### Endpoint

```http
POST /auth/register
```


### Description

Creates a new user account.


### Request Body


```json
{
  "username": "saurabh",
  "email": "user@gmail.com",
  "password": "password123",
  "role": "accountant"
}
```


### Response


```json
{
  "message": "User created successfully"
}
```


---

## Login User


### Endpoint


```http
POST /auth/login
```


### Description

Authenticates user and returns JWT token.


### Request


```json
{
  "username": "saurabh",
  "password": "password123"
}
```


### Response


```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```


---

# 2. Vendor APIs


## Create Vendor


### Endpoint

```http
POST /vendors/
```


### Authentication

Required


### Request


```json
{
  "name": "ABC Technologies",
  "email": "vendor@gmail.com",
  "phone": "9876543210"
}
```


### Response


```json
{
  "id":1,
  "name":"ABC Technologies"
}
```


---

## Get Vendors


### Endpoint


```http
GET /vendors/
```


Returns all registered vendors.


---

## Get Vendor By ID


### Endpoint


```http
GET /vendors/{vendor_id}
```


Example:


```text
/vendors/1
```


---

# 3. Invoice APIs


## Upload Invoice


### Endpoint


```http
POST /upload/
```


### Description

Uploads invoice document and starts processing.


Supported files:

```text
PDF

Images
```


Request:

```text
multipart/form-data
```


Response:

```json
{
  "message":"Invoice uploaded successfully",
  "invoice_id":10
}
```


---

## Get All Invoices


### Endpoint


```http
GET /invoices/
```


Response:


```json
[
 {
  "id":1,
  "invoice_number":"INV001",
  "status":"Pending"
 }
]
```


---

## Search Invoice


### Endpoint


```http
GET /invoices/search
```


Query Parameters:


```text
status

vendor

date
```


Example:


```http
/invoices/search?status=Pending
```


---

## Get Invoice Details


### Endpoint


```http
GET /invoices/{invoice_id}
```


Example:


```text
/invoices/10
```


---

## Invoice Timeline


### Endpoint


```http
GET /invoices/{invoice_id}/timeline
```


Returns complete invoice history.


Response:


```json
[
 {
  "event":"Uploaded",
  "timestamp":"2026-08-01"
 }
]
```


---

# 4. Approval APIs


## Approve Invoice


### Endpoint


```http
POST /approval/{invoice_id}/approve
```


Description:

Approves pending invoice.


---

## Reject Invoice


### Endpoint


```http
POST /approval/{invoice_id}/reject
```


Description:

Rejects invoice.


---

# 5. Prediction APIs


## Predict Invoice Risk


### Endpoint


```http
POST /predict/
```


Description:

Runs ML model prediction.


Request:


```json
{
 "invoice_id":10
}
```


Response:


```json
{
 "risk_score":0.85,
 "prediction":"Manual Approval Required"
}
```


---

# 6. Dashboard APIs


## Dashboard Summary


### Endpoint


```http
GET /dashboard/summary
```


Returns:


```json
{
 "total_invoices":100,
 "pending":20,
 "approved":70,
 "rejected":10
}
```


---

# 7. Analytics APIs


## Invoice Analytics


### Endpoint


```http
GET /analytics/invoices
```


Provides:


```text
Monthly invoice count

Approval trends

Vendor statistics
```


---

# 8. Export APIs


## Export Invoice Data


### Endpoint


```http
GET /export/invoices
```


Supported formats:


```text
CSV

Excel

PDF
```


Example:


```http
/export/invoices?format=csv
```


---

# 9. Notification APIs


## Get Notifications


### Endpoint


```http
GET /notifications/
```


Returns user notifications.


---

# 10. WebSocket API


## Real-Time Notification Socket


Endpoint:


```text
ws://localhost:8000/ws/notifications
```


Used for:

- Invoice updates
- Approval updates
- Risk alerts


---

# 11. Health Check APIs


## Application Health


Endpoint:


```http
GET /health
```


Response:


```json
{
 "status":"healthy"
}
```


---

# HTTP Status Codes


| Code | Meaning |
|---|---|
|200|Success|
|201|Created|
|400|Bad Request|
|401|Unauthorized|
|403|Forbidden|
|404|Not Found|
|500|Server Error|


---

# Error Response Format


Example:


```json
{
 "detail":"Invoice not found"
}
```


---

# API Security


Implemented security:


```text
JWT Authentication

Password Hashing

Protected Routes

Role Based Access Control

Environment Secrets
```


---

# API Testing


Recommended tools:


```text
Swagger UI

Postman

Curl

FastAPI Test Client
```


---

# Summary


The API layer provides:


✅ Secure authentication

✅ Vendor management

✅ Invoice processing

✅ OCR integration

✅ ML predictions

✅ Approval workflow

✅ Analytics

✅ Export functionality

✅ Real-time notifications