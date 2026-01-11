# Data Flow Description

## Step 1: Data Ingestion
Clinical data is sourced from a CSV file representing legacy healthcare systems.

---

## Step 2: Data Transformation
The Python-based Translator reads CSV rows and converts them into:
- Patient resources
- Observation resources

Each resource is assigned a UUID.

---

## Step 3: Semantic Validation
FHIR profiles created using FSH enforce:
- Correct data types
- Mandatory fields
- Valid references

---

## Step 4: Data Persistence
Validated FHIR resources are uploaded to a HAPI FHIR Server
running in a Docker container.

---

## Step 5: Outcome
Standardized, interoperable FHIR resources are stored
and ready for downstream consumption.
