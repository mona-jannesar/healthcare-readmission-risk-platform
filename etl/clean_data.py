import pandas as pd

RAW_DATA_PATH = "data/raw/diabetic_data.csv"
PROCESSED_PATH = "data/processed"

def clean_and_process():
    df = pd.read_csv(RAW_DATA_PATH)

    # Drop rows missing patient identifier
    #subset tells pandas which columns to look at when deciding whether to drop a row
    df = df.dropna(subset=["patient_nbr"])

    #normalize
    df["gender"] = df["gender"].replace({"Unknown/Invalid": "None"})

    #filter out rows without valid readmission status
    df = df[df["readmitted"].isin(["<30", ">30", "NO"])]

    #Creat outcome lables
    #use astype(int) to convert boolean values to 0 and 1 which is faster than using apply
    # and lambda functions which can be slower for large datasets by doning loops in Python rather than leveraging pandas' optimized vectorized operations
    df["readmission_30day"] = (df["readmitted"] == "<30").astype(int)
    df["readmission_90day"] = (df["readmitted"] == ">30").astype(int)

    #map schema columns (renaming)

    patinets_df = df[["patient_nbr", "gender", "age", "race"]].copy()
    patinets_df = patinets_df.drop_duplicates(subset=["patient_nbr"])   

    encounters_df = df[["patient_nbr", "time_in_hospital", "num_lab_procedures", "num_medications",
                        "admission_type_id", "discharge_disposition_id", "admission_source_id"]].copy()
    
    outcomes_df = df[["patient_nbr", "readmission_30day", "readmission_90day"]].copy()  

    #Write cleaned data to rocessed folder
    patinets_df.to_csv(PROCESSED_PATH + "/patients.csv", index=False)
    encounters_df.to_csv(PROCESSED_PATH + "/encounters.csv", index=False)
    outcomes_df.to_csv(PROCESSED_PATH + "/outcomes.csv", index=False)

    print("Data cleaning and processing complete. Processed files save")  

if __name__ == "__main__":
    clean_and_process()
    








