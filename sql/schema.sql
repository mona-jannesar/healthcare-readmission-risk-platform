-- Table to store patient demographics
CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other') OR gender IS NULL),
    age_group VARCHAR(20),
    race VARCHAR(50)
);

-- Table for encounters (one row per hospital visit)
CREATE TABLE encounters (
    encounter_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id),
    admission_type VARCHAR(50),
    discharge_disposition VARCHAR(50),
    admission_source VARCHAR(50),
    time_in_hospital INTEGER CHECK (time_in_hospital >= 0),
    num_lab_procedures INTEGER CHECK (num_lab_procedures >= 0),
    num_medications INTEGER CHECK (num_medications >= 0),
    readmitted BOOLEAN
);

-- Table for clinical diagnoses
CREATE TABLE diagnoses (
    diag_id SERIAL PRIMARY KEY,
    encounter_id INTEGER REFERENCES encounters(encounter_id),
    diagnosis_code VARCHAR(20)
);

-- Table for target labels
CREATE TABLE outcomes (
    encounter_id INTEGER PRIMARY KEY REFERENCES encounters(encounter_id),
    readmission_30day BOOLEAN,
    readmission_90day BOOLEAN
);
-- Indexes to speed up joins on foreign keys
-- I added indexes on foreign keys used in joins because feature extraction and cohort queries rely heavily on joins. This prevents full table scans as the dataset grows and reflects production performance considerations.
CREATE INDEX IF NOT EXISTS idx_encounters_patient_id 
ON encounters(patient_id);

CREATE INDEX IF NOT EXISTS idx_diagnoses_encounter_id 
ON diagnoses(encounter_id);
