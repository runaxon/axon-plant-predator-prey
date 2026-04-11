from myelin import PatientLoader
import json

class MyPatientLoader(PatientLoader):
    default_id = ('lion-gazelle', 1)

    def load(self, patient_id):
        cohort, pid = patient_id
        with open(f'cohorts/{cohort}/{pid}.json') as f:
            data = json.load(f)
        return (data['alpha'], data['beta'], data['delta'], data['gamma'])