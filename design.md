# Design Document: My Travel Souvenirs

1. **Objectives:** To create a structured catalog of travel souvenirs parsable by software agents.

2. **Target Audience:** Tourism analysis bots and personal archiving agents.

3. **Ontology Selection:**

   *   **Schema.org (`schema:CreativeWork`):** Selected as the parent class instead of schema:Product. This decision was made to correctly model souvenirs as cultural artifacts and crafted works rather than commercial merchandise.

   *   **Custom Ontology (`my:`):** Created to handle specific travel context which Schema.org lacks.
       *   **Class:** `my:Souvenir` (Subclass of `schema:CreativeWork`).
       *   **Properties:**
           *   `my:boughtInCity`: The name of the city where the souvenir was purchased.
           *   `my:tripYear`: The year the trip took place.
           *   `my:buyerName`: The name of the person who bought the item.
           *   `my:souvenirCategory`: The type of object (e.g., Keychain, Clothing).

4. **Competency Questions:**

   List of questions our queries answer:
   *   What souvenirs were purchased in a specific city? (e.g., "Paris")
   *   Which souvenirs were purchased in a specific year or time period? (e.g., "after 2020")
   *   What souvenirs belong to a specific category? (e.g., "Clothing")
   *   What items were purchased by a specific buyer? (e.g., "Alice")
   *   In which city was a specific souvenir purchased?
