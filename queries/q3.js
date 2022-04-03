//3.Valor màxim, mínim i mitjà de BenignPrec agrupat per classificador (classifier). Mostra ID del mètode, MaxBenignPrec, MinBenignPrec, AvgBenignPrec.
db.Methods.aggregate([
{
   $lookup:
     {
       from: 'Experiments',
       localField: 'MethodID',
       foreignField: 'MethodID',
       as: 'MID'
     }
},
{$unwind: '$MID' },
{$group : {_id:'$Classifier',
    'MaxBenignPrec':{$max: "$MID.BenignPrec"},
    'MinBenignPrec':{$min: "$MID.BenignPrec"},
    'AvgBenignPrec':{$avg: "$MID.BenignPrec"}} }
])