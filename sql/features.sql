-- Create a flattened view Combining patients, encounters, and outcomes for feature extraction
CREATE or REPLACE VIEW ml_feature_view AS
SELECT
    p.patient_id, p.gender, p.age_group, p.race, e.time_in_hospital, e.num_medications, e.num_lab_procedures,
    o.readmission_30day, o.readmission_90day
FROM patients p
JOIN encounters e ON p.patient_id = e.patient_id
JOIN outcomes o ON e.encounter_id = o.encounter_id;