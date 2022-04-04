from pymongo import MongoClient
import pandas as pd
import sys

################################## CARREGUEM EL FITXER EXCEL ###################################

df = pd.read_excel (sys.argv[2], sheet_name = None)
d_exp = df['MethodOutput']
d_train = df['Training']
d_cases = df['Cases']

################################## PARAMETRES DE CONNEXIO ###################################
mongoUser = ''
mongoPassword = ''
mongoDB = ''
Host = 'localhost' 
Port = 27017

###################################### CONNEXIO ##############################################

DSN = "mongodb://{}:{}".format(Host,Port)
conn = MongoClient(DSN)

############## CREEM LES COLLECTIONS I OMPLIM AMB LES DADES DE L'EXCEL ########################

bd = conn['cancer']

bd.Methods.drop()
bd.Experiments.drop()
bd.Nodules.drop()
bd.Patients.drop()
bd.CTScanners.drop()

met = bd.create_collection('Methods')
exp = bd.create_collection('Experiments')
nod = bd.create_collection('Nodules')
pac = bd.create_collection('Patients')
sca = bd.create_collection('CTScanners')


## COLLECTION METHODS
experiments = []
for index, row in d_exp.iterrows(): 
    experiments.append(row['Repetition'])
    if index == d_exp.shape[0]-1: 
        dades = {
                'MethodID':       row['MethodID'], 
                'FeatSelection':  row['FeatSelection'],  
                'FeatDescriptor': row['FeatDescriptor'], 
                'Classifier':     row['Classifier'],
                'Experiments':    experiments
                }
        met.insert_one(dades)  
        experiments = []
        
    elif row['MethodID'] != d_exp['MethodID'][index+1]:
        dades = {
                'MethodID':       row['MethodID'], 
                'FeatSelection':  row['FeatSelection'],  
                'FeatDescriptor': row['FeatDescriptor'], 
                'Classifier':     row['Classifier'],
                'Experiments':    experiments
                }
        met.insert_one(dades)  
        experiments = []

##COLLECTION EXPERIMENTS
for index, row in d_exp.iterrows(): 
    nodules = []
    for index2, row2 in d_train.iterrows(): 
        if (row['MethodID'] == row2['MethodID'] and row['Repetition'] == row2['ExperimentRepetition']):
            nodules.append({'PatientID':     row2['PatientID'], 
                             'NoduleID':     row2['NodulID'],
                             'RadDiagnosis': row2['RadiomicsDiagnosis'],
                             'TrainTest':    row2['Train']
                           })
    dades = {
              'MethodID':       row['MethodID'],
              'Repetition':     row['Repetition'], 
              'Train':          row['Train'], 
              'BenignPrec':     row['BenignPrec'],
              'BenignRec':      row['BenignRec'],
              'MalignPrec':     row['MalignPrec'],
              'MalignRec':      row['MalignRec'],
              'Nodules':        nodules
            }
    exp.insert_one(dades)    
    
##COLLECTION PATIENTS 
nodules = []   
for index, row in d_cases.iterrows():    
    nodules.append(row['NoduleID'])
    if index == d_cases.shape[0]-1: 
        dades = {
            'PatientID':        row['PatientID'], 
            'Age':              row['Age'], 
            'Gender':           row['Gender'],
            'DiagnosisPatient': row['DiagnosisPatient'],
            'Nodules':          nodules
            }
        pac.insert_one(dades) 
        nodules = []
    elif row['PatientID'] != d_cases['PatientID'][index+1]:
        dades = {
            'PatientID':        row['PatientID'], 
            'Age':              row['Age'], 
            'Gender':           row['Gender'],
            'DiagnosisPatient': row['DiagnosisPatient'],
            'Nodules':          nodules
            }
        pac.insert_one(dades) 
        nodules = []
        
##COLLECTION SCANNERS
nodules = []
patients = []
for index, row in d_cases.iterrows():  
    nodules.append(row['NoduleID'])
    patients.append(row['PatientID'])
                 
    if index == d_cases.shape[0]-1: 
        dades = {
                'CTID':             row['CTID'],
                'Device':           row['Device'],
                'dataCT':           row['dataCT'],
                'Resolution': {
                              'T':  row['ResolutionT'],
                              'TV': row['ResolutionTV'],
                              'TC': row['ResolutionTC']
                              },
                'PatientID':        patients,
                'NoduleID':         nodules
                }
        nodules = []
        patients = []
        sca.insert_one(dades)
        
    elif row['CTID'] != d_cases['CTID'][index+1]: 
        dades = {
                'CTID':             row['CTID'],
                'Device':           row['Device'],
                'dataCT':           row['dataCT'],
                'Resolution': {
                              'T':  row['ResolutionT'],
                              'TV': row['ResolutionTV'],
                              'TC': row['ResolutionTC']
                              },
                'PatientID':        patients,
                'NoduleID':         nodules
                }
        nodules = []
        patients = []
        sca.insert_one(dades)
        
##COLLECTION  NODULES    
for index, row in d_cases.iterrows():    
    dades = {
        'PatientID':         row['PatientID'], 
        'NoduleID':          row['NoduleID'],
        'DiagnosisNodule':   row['DiagnosisNodul'],
        'Position': {
                       'X': row['PositionX'],
                       'Y': row['PositionY'],
                       'Z': row['PositionZ']
                    },
        'Diameter':         row['Diameter (mm)'],
        }
    nod.insert_one(dades)        
