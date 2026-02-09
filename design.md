# Design Document: My Travel Souvenirs

1. **Objectives:** To create a structured catalog of travel souvenirs parsable by software agents.

2. **Target Audience:** Tourism analysis bots and personal archiving agents.

3. **Ontology Selection:**

   *   **Schema.org (`schema:CreativeWork`):** Selected as the parent class instead of schema:Product. This decision was made to correctly model souvenirs as cultural artifacts and crafted works rather than commercial merchandise.

   *   **Custom Ontology (`my:Souvenir`):** Extends CreativeWork to add travel-specific context...

4. **Competency Questions:**

   List of questions our queries answer:
   *   What souvenirs were purchased in a specific city? (e.g., "Paris")
   *   Which souvenirs were purchased in a specific year or time period? (e.g., "after 2020")
   *   What souvenirs belong to a specific category? (e.g., "Clothing")
   *   What items were purchased by a specific buyer? (e.g., "Alice")
   *   In which city was a specific souvenir purchased?
