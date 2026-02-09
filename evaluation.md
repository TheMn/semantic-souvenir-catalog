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

* **CQ1: Select all souvenirs bought in 'Paris'**
    * *Query:* Filters `my:boughtInCity` by "Paris".
    * *Result:* Retrieves "Eiffel Tower Keychain".

* **CQ2: Select all souvenirs bought after 2020**
    * *Query:* Filters `my:tripYear > 2020`.
    * *Result:* Correctly retrieves items bought in recent years (e.g., Persian Rug (2025), Venetian Mask (2023), Eiffel Tower Keychain (2021), Wooden Clogs (2023), Dirndl or Lederhosen Hat (2024), Silk Scarf (2021)).

* **CQ3: Select all souvenirs that are "Clothing"**
    * *Query:* Filters `my:souvenirCategory` by "Clothing".
    * *Result:* Retrieves "I <3 NY T-Shirt", "Dirndl or Lederhosen Hat", "Silk Scarf".

* **CQ4: Select name and city of souvenirs bought by "Alice"**
    * *Query:* Filters `my:buyerName` by "Alice" and selects name and city.
    * *Result:* Retrieves "Persian Rug" (Tabriz), "Eiffel Tower Keychain" (Paris), "Wooden Clogs" (Amsterdam).
