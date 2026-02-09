# Evaluation Report

## 1. Validation Methodology

### A. Semantic Validity (Primary)
The dataset was validated using `rdflib` and is compliant with standard Linked Data principles.
* **Result:** 0 Errors.
* **Conclusion:** The JSON-LD correctly implements the `schema:CreativeWork` class and the custom `my:Souvenir` extension with nested object properties (`my:buyer` -> `schema:Person`, `my:boughtIn` -> `schema:City`).

### B. Google Rich Results (Secondary)
The dataset remains compatible with **Google's Rich Results Test**.
* **Result:** The shift from simple strings to structured entities enhances the semantic richness without violating `CreativeWork` constraints.
* **Analysis:** This confirms that modeling the items as cultural artifacts (`CreativeWork`) with rich relationships is the correct semantic approach.

### C. Ontology Validation
The custom T-Box (`vocabulary.ttl`) was validated for Turtle syntax.
* **Result:** Valid Turtle syntax.
* **Structure:** The domain (`my:Souvenir`) and range (`schema:Person`, `schema:City`, `schema:Date`) definitions were verified to ensure logical consistency.

## 2. Query Testing & Competency Questions
The following SPARQL queries (see `queries.txt`) were executed to verify the Data Model answers the project's requirements:

* **CQ1: Select all souvenirs bought in 'Paris'**
    * *Query:* Traverses `my:boughtIn` node to match `schema:name` "Paris".
    * *Result:* Retrieves "Eiffel Tower Keychain".

* **CQ2: Select all souvenirs bought after 2020**
    * *Query:* Filters `my:tripDate` > "2020-12-31" (xsd:date comparison).
    * *Result:* Correctly retrieves items bought in recent years (e.g., Persian Rug (2025), Venetian Mask (2023), Eiffel Tower Keychain (2021), Wooden Clogs (2023), Dirndl or Lederhosen Hat (2024), Silk Scarf (2021)).

* **CQ3: Select all souvenirs that are "Clothing"**
    * *Query:* Filters `schema:category` by "Clothing".
    * *Result:* Retrieves "I <3 NY T-Shirt", "Dirndl or Lederhosen Hat", "Silk Scarf".

* **CQ4: Select name and city of souvenirs bought by "Alice"**
    * *Query:* Traverses `my:buyer` node for "Alice" and `my:boughtIn` node for city name.
    * *Result:* Retrieves "Persian Rug" (Tabriz), "Eiffel Tower Keychain" (Paris), "Wooden Clogs" (Amsterdam).
