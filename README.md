# Healthcare Readmission Risk Platform

## Goal
Build an end-to-end healthcare machine learning system that predicts 30-day hospital readmission risk from clinical data.

This project is designed as a production-style portfolio piece:
- Data ingestion and cleaning
- SQL data modeling
- Feature engineering and ML modeling
- Experiment tracking
- API deployment
- Automated pipelines
- Clear documentation

## Why this project
Healthcare ML systems fail more from data and engineering problems than from model choice.  
This project focuses on building the full pipeline, not just training a model.

## Planned Architecture (High-Level)
Raw Data  
→ ETL (ingest, clean, validate)  
→ SQL Database  
→ Feature Engineering  
→ ML Training  
→ API Service  
→ Automated Pipelines  

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

## Status
Project initialized. Data engineering phase starting.
