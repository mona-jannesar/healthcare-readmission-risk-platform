import pandas as pd

RAW_DATA_PATH = "data/raw/diabetic_data.csv"
PROCESSED_PATH = "data/processed"

def clean_and_process():
    df = pd.read_csv(RAW_DATA_PATH)

    # Drop rows missing patient identifier
    #subset tells pandas which columns to look at when deciding whether to drop a row
    df = df.dropna(subset=["patient_nbr"])

    # ---- Normalize column names to match SQL schema (GLOBAL CONTRACT) ----
    df = df.rename(columns={
    "patient_nbr": "patient_id",
    "age": "age_group",
    "admission_type_id": "admission_type",
    "discharge_disposition_id": "discharge_disposition",
    "admission_source_id": "admission_source"
})

    #normalize
    df["gender"] = df["gender"].replace({"Unknown/Invalid": "None"})

    #filter out rows without valid readmission status
    df = df[df["readmitted"].isin(["<30", ">30", "NO"])]

    #Creat outcome lables
    #use astype(int) to convert boolean values to 0 and 1 which is faster than using apply
    # and lambda functions which can be slower for large datasets by doning loops in Python rather than leveraging pandas' optimized vectorized operations
    df["readmission_30day"] = (df["readmitted"] == "<30").astype(int)
    df["readmission_90day"] = (df["readmitted"] == ">30").astype(int)
    df["readmitted"] = df["readmitted"].isin(["<30", ">30"])

    # Split normalized dataframe into schema tables
    patients_df = df[["patient_id", "gender", "age_group", "race"]].copy()
    patients_df = patients_df.drop_duplicates(subset=["patient_id"]) 


    encounters_df = df[[
        "encounter_id",
        "patient_id",
        "admission_type",
        "discharge_disposition",
        "admission_source",
        "time_in_hospital",
        "num_lab_procedures",
        "num_medications",
        "readmitted"
    ]].copy()
    
    outcomes_df = df[[
        "encounter_id",
        "readmission_30day",
        "readmission_90day"
    ]].copy()

    #Write cleaned data to rocessed folder
    patients_df.to_csv(PROCESSED_PATH + "/patients.csv", index=False)
    encounters_df.to_csv(PROCESSED_PATH + "/encounters.csv", index=False)
    outcomes_df.to_csv(PROCESSED_PATH + "/outcomes.csv", index=False)

    print("Data cleaning and processing complete. Processed files save")  

if __name__ == "__main__":
    clean_and_process()
    








