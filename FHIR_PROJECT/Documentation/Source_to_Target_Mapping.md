# Source to Target Mapping (FHIR Project)

## 1. Overview
This document describes the mapping between source healthcare data (CSV format)
and target HL7 FHIR R4 resources implemented using a HAPI FHIR Server.

The objective is to demonstrate how legacy clinical data is transformed into
standardized FHIR resources to support interoperability.

---

## 2. Source System

**Source Type:** CSV file  
**Source Location:** Translator/data/patient_observation.csv  

### Source Fields
| Source Field | Description |
|-------------|------------|
| patient_id | Unique identifier of the patient |
| name | Patient full name |
| gender | Administrative gender |
| age | Patient age |
| observation_code | Clinical observation code |
| observation_value | Observation value |

---

## 3. Target System

**Standard:** HL7 FHIR R4  
**FHIR Server:** HAPI FHIR (Docker-based)

### Target Resources
- Patient (StructureDefinition-mta-patient)
- Observation (StructureDefinition-mta-observation)

---

## 4. Source to Target Mapping

### Patient Resource Mapping

| Source Field | Target Resource | FHIR Element |
|-------------|----------------|-------------|
| patient_id | Patient | Patient.id |
| name | Patient | Patient.name.text |
| gender | Patient | Patient.gender |
| age | Patient | Patient.extension (age) |

---

### Observation Resource Mapping

| Source Field | Target Resource | FHIR Element |
|-------------|----------------|-------------|
| observation_code | Observation | Observation.code.text |
| observation_value | Observation | Observation.valueString |
| patient_id | Observation | Observation.subject.reference |

---

## 5. Transformation Logic

- Source CSV is read using Python
- UUIDs are generated for FHIR resources
- Patient and Observation resources are linked using references
- Resources conform to FHIR profiles defined using FSH

---

## 6. Outcome

- Legacy CSV data successfully converted into FHIR resources
- Semantic integrity maintained using FHIR profiles
- Resources ready for upload and validation in HAPI FHIR Server
