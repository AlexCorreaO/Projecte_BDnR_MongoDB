//5. Pacients amb més de dos nòduls. Mostra ID del Pacient, sexe, edat, diagnòstic del Pacient
db.Patients.find({Nodules: {$gt: 2}}).projection({PatientID:1,Age:1,Gender:1,DiagnosisPatient:1})
