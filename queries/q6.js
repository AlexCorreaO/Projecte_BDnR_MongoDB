//6. Mostrar els 4 mètodes amb més repeticions de l’experiment. Mostra el ID del Mètode i número de repeticions de l’experiment.
db.Experiments.find().limit(4).sort( { Repetition: -1 }).projection({MethodID:1,Repetition:1})
