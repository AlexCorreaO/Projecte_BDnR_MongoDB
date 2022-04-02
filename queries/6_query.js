db.Experiments.find().limit(4).sort( { Repetition: -1 }).projection({MethodID:1,Repetition:1})
