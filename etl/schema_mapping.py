SCHEMA_MAPPING = {
    "patients": {
        "gender": "gender",
        "age_group": "age",
        "race": "race"
    },
    "encounters": {
        "time_in_hospital": "time_in_hospital",
        "num_lab_procedures": "num_lab_procedures",
        "num_medications": "num_medications",
        "admission_type": "admission_type_id",
        "discharge_disposition": "discharge_disposition_id",
        "admission_source": "admission_source_id"
    },
    "outcomes": {
        "readmission_30day": "readmitted"
    }
}
