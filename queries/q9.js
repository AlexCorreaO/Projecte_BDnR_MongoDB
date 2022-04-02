//9. Modificar la ResolutionTV aumentant-la un 20% dels escàners que es van
//realitzar amb DataCT = 18/11/2018 
//db.CTScanners.updateMany({'dataCT':ISODate("2018-11-18")}, {$set: {'Resolution.TV' : 120 }})
db.CTScanners.updateMany({'dataCT':ISODate("2018-11-18")}, {$mul: {'Resolution.TV':1.2}})

db.CTScanners.find({'dataCT':ISODate("2018-11-18")})