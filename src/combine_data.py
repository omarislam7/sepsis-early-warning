import pandas as pd
from pathlib import Path

data_path = Path("data")
patient_files = list(data_path.rglob("*.psv"))

print("Patient files:", len(patient_files))

all_patients = []

for file in patient_files:
    df = pd.read_csv(file, sep="|")
    df["PatientID"] = f"{file.parent.name}_{file.stem}"
    all_patients.append(df)

combined_df = pd.concat(all_patients, ignore_index=True)

print(combined_df.shape)
print(combined_df["PatientID"].nunique())

output = Path("data/processed/sepsis_combined.csv")
output.parent.mkdir(parents=True, exist_ok=True)

combined_df.to_csv(output, index=False)

print("CSV saved:", output.exists())