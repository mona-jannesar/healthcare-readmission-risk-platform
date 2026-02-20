# Healthcare Readmission Risk Platform

## Goal
Build an end-to-end healthcare machine learning system that predicts 30-day hospital readmission risk from clinical data.

## Summary 
This repository contains an end-to-end data science project built as a realistic production pipeline for predicting 30-day hospital readmission risk. The goal is to showcase strong skills in data engineering, SQL database design, machine learning, API deployment, experiment tracking, and automation — all of which are directly relevant to professional data science roles.

This project is designed as a production-style portfolio piece and emphasizes:

- Data ingestion and cleaning
- SQL data modeling
- Feature engineering and ML modeling
- Experiment tracking
- API deployment
- Automated pipelines
- Clear documentation

## Why this project
In real-world healthcare ML systems, failures usually come from data quality, pipeline design, and engineering gaps — not from the choice of model.
This project focuses on building a robust, reproducible ML pipeline rather than only training a model.

## Planned Architecture (High-Level)
Raw Data  
→ ETL (ingest, clean, validate)  
→ SQL Database  
→ Feature Engineering  
→ ML Training  
→ API Service  
→ Automated Pipelines 

## Tech Stack

- Python (pandas, scikit-learn, SQLAlchemy)
- PostgreSQL (or SQLite)
- FastAPI for serving predictions
- MLflow for experiment tracking
- Docker for containerization
- Great Expectations for data validation
- Airflow/Prefect for pipeline automation


## Repo Structure
- `data/` – raw and processed data  
- `sql/` – schema and queries  
- `etl/` – ingestion and cleaning  
- `modeling/` – training and evaluation  
- `api/` – prediction service  
- `pipelines/` – automation  
- `tests/` – tests  

## Roadmap (4 Months)
Month 1: Data ingestion, validation, SQL  
Month 2: Modeling and experiment tracking  
Month 3: API, Docker, pipelines  
Month 4: Production polish and documentation  

## How to Get Started

1. Clone the repo
2. Create and activate a Python env
3. Install dependencies
4. Run ETL scripts
5. Launch FastAPI service


## Project Status

✔️ Repository structure setup  
✔️ README with roadmap  
⏳ Data ingestion coming next  
🛠️ Future: modeling, deployment, pipelines

## Progress

### Day 1 – Project Foundation
- Created local project structure and initialized Git repository.
- Set up Python virtual environment and `requirements.txt` to make the project reproducible.
- Connected local repo to GitHub and pushed initial commit.
- Wrote project README with goal, architecture outline, and 4-month roadmap.

**Why this matters:**  
This establishes a clean, professional foundation. The project can be cloned and rebuilt on another machine, and the repo already communicates intent and scope to reviewers.

---

### Day 2 – Data Modeling (SQL Schema)
- Designed a normalized SQL schema for:
  - `patients` (demographics)
  - `encounters` (hospital visits)
  - `diagnoses` (clinical codes)
  - `outcomes` (readmission labels)
- Added foreign keys to enforce relationships between tables.
- Committed `sql/schema.sql` to version control.

**Why this matters:**  
Separating entities prevents duplicated patient data, reduces inconsistency, and makes joins and audits reliable. This structure mirrors real EHR databases and reduces data leakage risk in ML pipelines.

---

### Day 3 – Database Wiring (ETL Backbone)
- Set up local PostgreSQL database for the project.
- Added Python database connector dependency.
- Created an ETL initialization script to execute `sql/schema.sql` from Python.
- Verified tables were created successfully in the database.

**Why this matters:**  
This proves the system is wired end-to-end: Python can control the database schema. It makes the pipeline reproducducible and ready for real data ingestion instead of manual setup.


### Day 4 – Data Ingestion and Profiling

**Dataset:** Diabetes 130-US hospitals (Kaggle)

**Key Observations:**
- ~100k encounters, ~50 columns
- Target label `readmitted` has multiple categories (e.g., <30, >30, NO)
- Significant missingness in race and some diagnosis-related fields
- Categorical IDs used for admission/discharge types (require mapping)
- Strong class imbalance in readmission label


- Raw dataset downloaded to `data/raw/diabetic_data.csv`
- Ingestion script `etl/ingest.py` created
- Script prints:
  - dataset shape
  - column names
  - missing value counts

  **Schema Mapping Plan:**
- Raw columns mapped to normalized SQL schema via `etl/schema_mapping.py`
- Cleaning and normalization planned before loading into SQL

This step confirms we can load and inspect raw data programmatically.
source of data https://www.kaggle.com/datasets/brandao/diabetes?resource=download

