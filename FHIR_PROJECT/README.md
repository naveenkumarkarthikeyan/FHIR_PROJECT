## \# FHIR Interoperability Project

## 

## \## Project Overview

## This project demonstrates an end-to-end healthcare interoperability pipeline

## using HL7 FHIR R4 standards. The implementation covers infrastructure setup,

## FHIR profiling, data transformation, and standardized data storage.

## 

## ---

## 

## \## Modules Overview

## 

## \### 1. Infrastructure

## \- Dockerized HAPI FHIR R4 Server

## \- Ensures consistent, reproducible, and portable deployment

## \- Validates and stores FHIR resources

## 

## \### 2. Rulebook

## \- Custom FHIR profiles created using FHIR Shorthand (FSH)

## \- Compiled using SUSHI to generate StructureDefinition JSON

## \- Enforces semantic integrity and validation rules

## 

## \### 3. Translator

## \- Python-based translator for legacy CSV data

## \- Converts flat files into FHIR-compliant Patient and Observation resources

## \- Uses UUIDs and references to maintain data consistency

## 

## \### 4. Documentation

## \- Source to Target Mapping

## \- System Architecture explanation

## \- Data Flow description

## 

## ---

## 

## \## Documentation

## 

## \- \[Source to Target Mapping](Documentation/Source\_to\_Target\_Mapping.md)

## \- \[System Architecture](Documentation/Architecture.md)

## \- \[Data Flow](Documentation/Data\_Flow.md)

## 

## ---

## 

## \## Technologies Used

## \- HL7 FHIR R4

## \- HAPI FHIR Server

## \- Docker

## \- FHIR Shorthand (FSH)

## \- SUSHI

## \- Python

## 

## ---

## 

## \## Outcome

## The project successfully converts legacy healthcare data into standardized

## FHIR resources and stores them in a FHIR server, enabling interoperability

## and downstream system integration.

## 

