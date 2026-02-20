import pandas as pd

RAW_DATA_PATH = "data/raw/diabetic_data.csv"

def basic_sanity_checks(df):
    print("\n=== Sanity Checks ===")

    # Check for impossible values
    if (df["time_in_hospital"] < 0).any():
        print("Found negative time_in_hospital values!")
    else:
        print("No negative time_in_hospital values found.")

    # Check for unexpected categories
    print("\nUnique gender values:")
    print(df["gender"].unique())

    print("\nUnique readmitted values:")
    print(df["readmitted"].unique())


def profile_data():
    df = pd.read_csv(RAW_DATA_PATH)

    print("=== Data shape ===")
    print(df.shape)

    print("\n=== Columns ===")
    print(df.columns.tolist())

    print("\n=== Missing values Counts ===")
    print(df.isna().sum().sort_values(ascending=False).head(10))

    print("\n=== Sample Rows ===")
    print(df.head(5))

    print("\n=== READMISSION VALUE COUNTS ===")
    print(df['readmitted'].value_counts(dropna=False))

    # ✅ Actually run sanity checks
    basic_sanity_checks(df)


if __name__ == "__main__":
    profile_data()
