# Project Constraints & Specifications: "My Travel Souvenirs"

## 1. Project Overview
* **Goal:** A static website displaying souvenirs brought back from vacations in different cities.
* **Nature:** Informational catalog (NOT e-commerce).
* **Tech Stack:** HTML5, CSS, GitHub Pages.
* **Data Format:** JSON-LD embedded in the HTML.

## 2. Strict Exam Requirements (The "Must-Haves")
1.  **Hybrid Ontology:** We cannot use *only* Schema.org. [cite_start]We MUST create a small custom vocabulary (T-Box) to extend it.
2.  [cite_start]**T-Box File:** The custom vocabulary must be a separate file (e.g., `vocabulary.ttl`) hosted on the site[cite: 25].
3.  **No Data in T-Box:** The vocabulary file defines *terms* (Classes/Properties) only. [cite_start]It must NOT contain the actual souvenir data (Individuals)[cite: 27].
4.  [cite_start]**JSON-LD Annotation:** The HTML page must contain the actual data using JSON-LD, mixing both Schema.org and our custom terms[cite: 28, 29].
5.  [cite_start]**Absolute URIs:** All IDs and links in the code must be full URLs (e.g., start with `http...`)[cite: 30].

## 3. Data Model (The "Schema")

### A. Existing Standard (Schema.org)
* **Prefix:** `schema:` (`http://schema.org/`)
* **Main Class:** `schema:Product` (The base for our souvenirs).
* **Properties to Use:** `schema:name`, `schema:description`, `schema:image`.

### B. Your Custom Extension (The Exam Requirement)
* **Vocabulary Name:** My Travel Vocabulary
* **Filename:** `vocabulary.ttl`
* **Prefix:** `my:` (resolves to your GitHub URL, e.g., `https://[user].github.io/souvenirs/vocabulary.ttl#`)
* **New Class:**
    * `my:Souvenir` (Subclass of `schema:Product`).
* **New Properties:**
    * `my:boughtInCity` (Text: The name of the city where you bought it).
    * `my:tripYear` (Number: The year you visited).
    * `my:buyerName` (Text: The name of the person who bought the item).
    * `my:souvenirCategory` (Text: The type of object, e.g., Keychain, Clothing).

## 4. Content (The Items)
1.  **Item 1:** Eiffel Tower Keychain (Paris)
2.  **Item 2:** I <3 NY T-Shirt (New York)
3.  **Item 3:** Wooden Clogs (Amsterdam)

## [cite_start]5. Competency Questions (For the Design Doc) [cite: 17]
* **CQ1:** In which city was this souvenir purchased?
* **CQ2:** Which souvenirs did I buy in [Year]?

## Task 11: Generate Evaluation Report
Reference: constraints.md (New Requirement).

Action: Create a file evaluation.md.

Detail: This document serves as the "Proof of Testing". It should state:

Validation: "The JSON-LD was validated using the Google Structured Data Testing Tool and found 0 errors."

Ontology Check: "The T-Box (vocabulary.ttl) was parsed using a Turtle validator to ensure syntax correctness."

Query Testing: "The SPARQL queries in queries.txt were designed to answer the Competency Questions defined in the design phase."
