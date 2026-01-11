# System Architecture

## Overview
This project implements an end-to-end HL7 FHIR interoperability pipeline
using containerized infrastructure, semantic rulebooks, and data translators.

---

## Architecture Components

### 1. Source System
- Legacy clinical data in CSV format
- Represents non-standardized healthcare data

### 2. Translator Layer
- Implemented using Python
- Converts CSV data into FHIR-compliant JSON
- Handles UUID generation and resource linking

### 3. Rulebook Layer
- FHIR profiles defined using FHIR Shorthand (FSH)
- Compiled using SUSHI
- Ensures semantic integrity and validation

### 4. FHIR Server
- HAPI FHIR R4 Server
- Deployed using Docker
- Stores and validates FHIR resources

---

## Architecture Benefits
- Modular design
- Standards-based interoperability
- Reusable and scalable components
