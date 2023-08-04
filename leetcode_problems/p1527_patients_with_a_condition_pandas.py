import pandas as pd


# Write a solution to find the patient_id, patient_name,
#   and conditions of the patients who have Type I Diabetes.
# Type I Diabetes always starts with DIAB1 prefix.
# Return the result table in any order.
# +------------+--------------+--------------+
# | patient_id | patient_name | conditions   |
# +------------+--------------+--------------+
# | 1          | Daniel       | YFEV COUGH   |
# | 2          | Alice        |              |
# | 3          | Bob          | DIAB100 MYOP |
# | 4          | George       | ACNE DIAB100 |
# | 5          | Alain        | DIAB201      |
# +------------+--------------+--------------+


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # %DIAB1% and % DIAB1% <- correct regex.
    # But match() doesn't work with it.
    # Using .* <- any for any times.
    patients = patients[
        patients['conditions'].str.match(pat='DIAB1.*')
        |
        patients['conditions'].str.match(pat='.* DIAB1.*')
    ]
    return patients
