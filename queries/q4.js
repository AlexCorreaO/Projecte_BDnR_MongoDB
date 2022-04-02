//4. Numero total d’homes i dones. Mostra sexe i número total.
db.Patients.aggregate([ {"$unwind":"$Gender"},{$group:{"_id" :"$Gender","count":{"$sum" :1}}}])
