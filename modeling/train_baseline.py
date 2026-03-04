import  pandas as pd
import numpy as np
import psycopg2
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler #OneHotEncoder:Converts categorical variables (gender, race, age_group) into numeric vectors
from sklearn.compose import ColumnTransformer #Applies different transformations to different columns
from sklearn.pipeline import Pipeline #Pipeline: Chains preprocessing and modeling steps together so we can treat them as a single unit
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, average_precision_score

#Database Connection Parameters
DBNAME = "healthcare_readmission"
USER = "mona"

def load_features():
    conn = psycopg2.connect(
        dbname=DBNAME,
        user=USER
    )
    query = "SELECT * FROM ml_feature_view;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def train_baseline():
    df = load_features()

    print("\n=== Target Distribution (30-day) ===")
    print(df["readmission_30day"].value_counts(normalize=True))

    X = df.drop(columns=["readmission_30day", "readmission_90day"])
    y = df["readmission_30day"] 

    categorical_cols = ["gender", "age_group", "race"]
    numerical_cols = ["time_in_hospital", "num_medications", "num_lab_procedures"] 


    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", "passthrough", numerical_cols)                                                                          
        ]
    )

    model = LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42)

    pipe = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ])  

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    pipe.fit(X_train, y_train)

    y_pred_proba = pipe.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_pred_proba)

    pr_auc = average_precision_score(y_test, y_pred_proba)
    print(f"PR-AUC: {pr_auc:.4f}")

    print("\nPredicted probability summary:")
    print(np.percentile(y_pred_proba, [0, 25, 50, 75, 90, 95, 99]))

    print(f"ROC AUC (30_day readmission): {auc:.4f}")
    print("Classification Report:")
# 🔽 ADD THIS BLOCK

    for t in [0.5, 0.3, 0.2, 0.1]:
        print(f"\n=== Threshold: {t} ===")
        y_pred_custom = (y_pred_proba >= t).astype(int)
        print(classification_report(y_test, y_pred_custom))


if __name__ == "__main__":
    train_baseline()
