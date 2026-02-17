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



