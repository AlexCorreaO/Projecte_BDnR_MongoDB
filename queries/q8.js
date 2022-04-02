//8. Mostrar els pacients que tenen tots els seus nóduls amb diagnosis = “Benign” i
//el seu recompte
use cancer
db.Nodules.aggregate([
    {$group: { _id: "$PatientID",
            "Recompte": {$sum:1},
             "DiagnosisNodule": {$addToSet: "$DiagnosisNodule"}}},
    {$match: {DiagnosisNodule: ['Benign']}},
    {$project: {DiagnosisNodule:0}}//, Device:1, dataCT:1, PatientID:1}}
 ])
   