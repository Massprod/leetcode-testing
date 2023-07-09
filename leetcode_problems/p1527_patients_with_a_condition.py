
# SQL schema:
# DROP TABLE IF EXISTS patients;
# Create table If Not Exists Patients (patient_id int, patient_name varchar(30), conditions varchar(100));
# Truncate table Patients;
# insert into Patients (patient_id, patient_name, conditions) values ('1', 'Daniel', 'YFEV COUGH');
# insert into Patients (patient_id, patient_name, conditions) values ('2', 'Alice', '');
# insert into Patients (patient_id, patient_name, conditions) values ('3', 'Bob', 'DIAB100 MYOP');
# insert into Patients (patient_id, patient_name, conditions) values ('4', 'George', 'ACNE DIAB100');
# insert into Patients (patient_id, patient_name, conditions) values ('5', 'Alain', 'DIAB201');
# --------------------
# Find the patient_id, patient_name and conditions of the patients who have Type I Diabetes.
# Type I Diabetes always starts with DIAB1 prefix.
# Return the result table in any order.

# SQL query:
# SELECT *
# FROM patients
# WHERE
# conditions LIKE 'DIAB1%'
# OR conditions LIKE '% DIAB1%';
# ------------
# Failed commit, because they didn't explicitly say that it should be separated from any other condition.
