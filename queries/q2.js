//2.Número total de nòduls que s’han utilitzat per l’entrenament (train=1) de l’experiment 1 del mètode "Method2”.
db.Experiments.aggregate([
    {$unwind:"$Nodules"},
    {$match: {'Nodules.TrainTest':1,Repetition:1, MethodID :"Method2"}},
    {$count:'Nombre de Noduls'}
    ])
