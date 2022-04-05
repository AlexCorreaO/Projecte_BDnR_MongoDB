//7. Per cada pacient els escàners (CTs) que s’ha fet. Mostra el ID del Pacient,
//device i la data del CT.
use cancer
db.CTScanners.aggregate([
    {$group: { _id: "$Nodules.PatientID",
             "Device": {$addToSet: "$Device"},
             "dataCT": {$addToSet: "$dataCT"}}},
 ])





 
