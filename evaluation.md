# Evaluation Report

## 1. Validation Methodology

### A. Semantic Validity (Primary)
The dataset was validated using the official **Schema.org Validator** (https://validator.schema.org/).
* **Result:** 0 Errors, 0 Warnings.
* **Conclusion:** The JSON-LD correctly implements the `schema:CreativeWork` class and the custom `my:Souvenir` extension. The syntax is compliant with standard Linked Data principles.

### B. Google Rich Results (Secondary)
The dataset was tested against **Google's Rich Results Test** to check for commercial search eligibility.
* **Result:** The shift from `schema:Product` to `schema:CreativeWork` successfully resolved previous warnings regarding missing `offers` and `aggregateRating`.
* **Analysis:** This confirms that modeling the items as cultural artifacts (`CreativeWork`) rather than commercial merchandise (`Product`) is the correct semantic approach for this non-commercial catalog.

### C. Ontology Validation
The custom T-Box (`vocabulary.ttl`) was validated using the **W3C RDF Validator**.
* **Result:** Valid Turtle syntax.
* **Structure:** The domain (`my:Souvenir`) and range (`schema:Text`/`Integer`) definitions were verified to ensure logical consistency.

## 2. Query Testing & Competency Questions
The following SPARQL queries (see `queries.txt`) were executed to verify the Data Model answers the project's requirements:

* **CQ1: Which items were bought after a certain year?**
    * *Query:* Filters `my:tripYear > 2020`.
    * *Result:* Correctly retrieves items bought in recent years (e.g., Persian Rug (2025), Venetian Mask (2023), Eiffel Tower Keychain).

* **CQ2: Can we categorize souvenirs by type?**
    * *Query:* Filters by `my:souvenirCategory`.
    * *Result:* Searching for "Clothing" isolates the "I <3 NY T-Shirt".

* **CQ3: Who bought which items?**
    * *Query:* Groups items by `my:buyerName`.
    * *Result:* Successfully aggregates the collection by buyer, fulfilling the multi-user expansion requirement.
