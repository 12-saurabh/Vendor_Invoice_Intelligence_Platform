# 🗄 Database Documentation

# Vendor Invoice Intelligence Platform


## Overview


The Vendor Invoice Intelligence Platform uses PostgreSQL as the primary relational database system.

PostgreSQL stores all application data including:

- User information
- Vendor details
- Invoice records
- Prediction results
- Approval workflow
- Notifications
- Audit history


Database technology:

```text
PostgreSQL 16

SQLAlchemy ORM

Alembic Migration
```


---

# Database Architecture


```text
                 FastAPI Backend

                       |

                       |

                SQLAlchemy ORM

                       |

                       |

                PostgreSQL Database

                       |

                       |

              Database Tables
```


---

# Entity Relationship Overview


```text
                    Users

                      |

                      |

                    Invoices

                  /     |      \

                 /      |       \

          Vendors   Predictions   Approval History


                      |

                      |

               Notifications


                      |

                      |

                 Audit Logs
```


---

# Database Tables


## 1. Users Table


Stores registered application users.


Table:

```text
users
```


Columns:


| Column | Type | Description |
|---|---|---|
|id|Integer|Primary Key|
|username|String|User name|
|email|String|User email|
|hashed_password|String|Encrypted password|
|role|String|User role|
|created_at|Timestamp|Creation time|


Roles:


```text
Admin

Accountant

Approver
```


---

# 2. Vendors Table


Stores vendor information.


Table:

```text
vendors
```


Columns:


| Column | Type | Description |
|-|-|-|
|id|Integer|Primary Key|
|name|String|Vendor name|
|email|String|Vendor email|
|phone|String|Contact number|
|created_at|Timestamp|Creation time|


Relationship:


```text
One Vendor

      |

      |

Many Invoices
```


---

# 3. Invoices Table


Main invoice storage table.


Table:


```text
invoices
```


Columns:


| Column | Type | Description |
|-|-|-|
|id|Integer|Primary Key|
|invoice_number|String|Invoice identifier|
|vendor_id|Integer|Vendor reference|
|amount|Float|Invoice amount|
|currency|String|Currency type|
|invoice_date|Date|Invoice date|
|due_date|Date|Payment due date|
|status|String|Current status|
|file_path|String|Uploaded file location|
|created_at|Timestamp|Created time|


Invoice Status:


```text
Pending

Approved

Rejected

Processing
```


---

# 4. Invoice Documents Table


Stores uploaded document information.


Table:


```text
invoice_documents
```


Columns:


|Column|Type|Description|
|-|-|-|
|id|Integer|Primary Key|
|invoice_id|Integer|Invoice reference|
|file_name|String|Document name|
|file_path|String|Storage path|
|file_type|String|PDF/Image|
|uploaded_at|Timestamp|Upload time|


---

# 5. Predictions Table


Stores ML prediction results.


Table:


```text
predictions
```


Columns:


|Column|Type|Description|
|-|-|-|
|id|Integer|Primary Key|
|invoice_id|Integer|Invoice reference|
|risk_score|Float|Risk probability|
|prediction|String|Model output|
|confidence|Float|Confidence score|
|created_at|Timestamp|Prediction time|


Relationship:


```text
One Invoice

      |

      |

One Prediction
```


---

# 6. Approval History Table


Tracks invoice approval workflow.


Table:


```text
approval_history
```


Columns:


|Column|Type|Description|
|-|-|-|
|id|Integer|Primary Key|
|invoice_id|Integer|Invoice reference|
|action|String|Approve/Reject|
|performed_by|Integer|User reference|
|comment|Text|Approval comment|
|created_at|Timestamp|Action time|


Workflow:


```text
Pending

   |

Review

   |

Approved / Rejected
```


---

# 7. Notifications Table


Stores user notifications.


Table:


```text
notifications
```


Columns:


|Column|Type|Description|
|-|-|-|
|id|Integer|Primary Key|
|user_id|Integer|User reference|
|message|Text|Notification message|
|read_status|Boolean|Read state|
|created_at|Timestamp|Creation time|


---

# 8. Audit Logs Table


Maintains system activity tracking.


Table:


```text
audit_logs
```


Columns:


|Column|Type|Description|
|-|-|-|
|id|Integer|Primary Key|
|user_id|Integer|User reference|
|action|String|Performed action|
|timestamp|Timestamp|Action time|


---

# Database Relationships


```text
Users

 1

 |

 |

 *

Invoices


Vendors

 1

 |

 |

 *

Invoices


Invoices

 1

 |

 |

 1

Predictions


Invoices

 1

 |

 |

 *

Approval History
```


---

# Database Migration


Database schema changes are managed using:


```text
Alembic
```


Migration commands:


Create migration:


```bash
alembic revision --autogenerate -m "migration_name"
```


Apply migration:


```bash
alembic upgrade head
```


Check migration status:


```bash
alembic current
```


---

# Database Security


Implemented security practices:


```text
Password Hashing

Database Credentials Using Environment Variables

Kubernetes Secrets

Role Based Access Control

SQL Injection Protection Using ORM
```


---

# Database Optimization


Implemented techniques:


```text
Database Indexing

Connection Pooling

Query Optimization

Pagination

Efficient Relationships
```


---

# Backup Strategy


Production backup approach:


```text
Regular PostgreSQL Backups

Point In Time Recovery

Persistent Volume Storage

Database Replication
```


---

# Summary


The database layer provides:


✅ Structured relational storage

✅ Secure data management

✅ Scalable schema design

✅ Migration support

✅ Audit tracking

✅ ML prediction storage

✅ Production-ready PostgreSQL architecture