import csv
import uuid
import json

bundle = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": []
}

with open("../data/patient_observation.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        patient_id = str(uuid.uuid4())

        patient = {
            "resourceType": "Patient",
            "id": patient_id,
            "name": [{"text": row["name"]}],
            "gender": "male" if row["gender"] == "M" else "female"
        }

        observation = {
            "resourceType": "Observation",
            "id": str(uuid.uuid4()),
            "status": "final",
            "code": {"text": row["observation_code"]},
            "subject": {"reference": f"Patient/{patient_id}"},
            "valueString": row["observation_value"]
        }

        bundle["entry"].append({"resource": patient})
        bundle["entry"].append({"resource": observation})

print(json.dumps(bundle, indent=2))
