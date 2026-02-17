-- Table to store patient demographics
CREATE TABLE IF NOT EXISTS patients (
    patient_id SERIAL PRIMARY KEY,
    gender VARCHAR(10),
    age_group VARCHAR(20),
    race VARCHAR(50)
);

-- Table for encounters (one row per hospital visit)
CREATE TABLE IF NOT EXISTS encounters (
    encounter_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id),
    admission_type VARCHAR(50),
    discharge_disposition VARCHAR(50),
    admission_source VARCHAR(50),
    time_in_hospital INTEGER,
    num_lab_procedures INTEGER,
    num_medications INTEGER,
    readmitted BOOLEAN
);

-- Table for clinical diagnoses
CREATE TABLE IF NOT EXISTS diagnoses (
    diag_id SERIAL PRIMARY KEY,
    encounter_id INTEGER REFERENCES encounters(encounter_id),
    diagnosis_code VARCHAR(20)
);

-- Table for target labels
CREATE TABLE IF NOT EXISTS outcomes (
    encounter_id INTEGER PRIMARY KEY REFERENCES encounters(encounter_id),
    readmission_30day BOOLEAN,
    readmission_90day BOOLEAN
);
