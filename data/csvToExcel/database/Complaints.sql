INSERT INTO MedicalRecords (PatientID, RECORDID)
SELECT PatientID, PatientID
FROM Patients;

SELECT * FROM MedicalRecords;

DELETE FROM MEDICALRECORDS;

