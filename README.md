For the final evaluation of the queries, I first used [JSON-LD Playground](https://json-ld.org/playground/) to convert the JSON-LD to N-Quads, then used [RDFShape](https://rdfshape.weso.es/dataQuery) to test the queries.

```N-Quads
<https://themn.github.io/semantic-souvenir-catalog/#souvenir1> <http://schema.org/genre> "Accessory" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir1> <http://schema.org/image> "https://themn.github.io/semantic-souvenir-catalog/photos/paris.jpg" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir1> <http://schema.org/name> "Eiffel Tower Keychain" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/CreativeWork> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#Souvenir> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir1> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#boughtIn> _:b4 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir1> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#buyer> _:b5 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir1> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#tripDate> "2021-06-12" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir2> <http://schema.org/genre> "Clothing" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir2> <http://schema.org/image> "https://themn.github.io/semantic-souvenir-catalog/photos/new_york.jpg" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir2> <http://schema.org/name> "I <3 NY T-Shirt" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/CreativeWork> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#Souvenir> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir2> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#boughtIn> _:b6 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir2> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#buyer> _:b7 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir2> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#tripDate> "2019-11-05" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir3> <http://schema.org/genre> "Decor" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir3> <http://schema.org/image> "https://themn.github.io/semantic-souvenir-catalog/photos/amsterdam.jpg" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir3> <http://schema.org/name> "Wooden Clogs" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/CreativeWork> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#Souvenir> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir3> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#boughtIn> _:b8 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir3> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#buyer> _:b9 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir3> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#tripDate> "2023-04-20" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir4> <http://schema.org/genre> "Decor" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir4> <http://schema.org/image> "https://themn.github.io/semantic-souvenir-catalog/photos/moscow.jpg" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir4> <http://schema.org/name> "Matryoshka Nesting Dolls" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/CreativeWork> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#Souvenir> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir4> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#boughtIn> _:b10 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir4> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#buyer> _:b11 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir4> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#tripDate> "2019-08-14" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir5> <http://schema.org/genre> "Homeware" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir5> <http://schema.org/image> "https://themn.github.io/semantic-souvenir-catalog/photos/tokyo.jpg" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir5> <http://schema.org/name> "Kintsugi-Style Ceramic Cup" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/CreativeWork> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#Souvenir> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir5> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#boughtIn> _:b12 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir5> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#buyer> _:b13 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir5> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#tripDate> "2020-01-25" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir6> <http://schema.org/genre> "Clothing" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir6> <http://schema.org/image> "https://themn.github.io/semantic-souvenir-catalog/photos/munich.jpg" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir6> <http://schema.org/name> "Dirndl or Lederhosen Hat" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir6> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/CreativeWork> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir6> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#Souvenir> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir6> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#boughtIn> _:b14 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir6> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#buyer> _:b15 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir6> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#tripDate> "2024-10-05" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir7> <http://schema.org/genre> "Clothing" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir7> <http://schema.org/image> "https://themn.github.io/semantic-souvenir-catalog/photos/bangkok.jpg" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir7> <http://schema.org/name> "Silk Scarf" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir7> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/CreativeWork> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir7> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#Souvenir> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir7> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#boughtIn> _:b16 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir7> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#buyer> _:b17 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir7> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#tripDate> "2021-12-10" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir8> <http://schema.org/genre> "Homeware" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir8> <http://schema.org/image> "https://themn.github.io/semantic-souvenir-catalog/photos/tabriz.jpg" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir8> <http://schema.org/name> "Persian Rug" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir8> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/CreativeWork> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir8> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#Souvenir> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir8> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#boughtIn> _:b0 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir8> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#buyer> _:b1 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir8> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#tripDate> "2025-03-15" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir9> <http://schema.org/genre> "Accessory" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir9> <http://schema.org/image> "https://themn.github.io/semantic-souvenir-catalog/photos/venice.jpg" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir9> <http://schema.org/name> "Venetian Mask" .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir9> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/CreativeWork> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir9> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#Souvenir> .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir9> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#boughtIn> _:b2 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir9> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#buyer> _:b3 .
<https://themn.github.io/semantic-souvenir-catalog/#souvenir9> <https://themn.github.io/semantic-souvenir-catalog/vocabulary.ttl#tripDate> "2023-09-02" .
_:b0 <http://schema.org/name> "Tabriz" .
_:b0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/City> .
_:b1 <http://schema.org/name> "Alice" .
_:b1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> .
_:b10 <http://schema.org/name> "Moscow" .
_:b10 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/City> .
_:b11 <http://schema.org/name> "Bob" .
_:b11 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> .
_:b12 <http://schema.org/name> "Tokyo" .
_:b12 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/City> .
_:b13 <http://schema.org/name> "Bob" .
_:b13 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> .
_:b14 <http://schema.org/name> "Munich" .
_:b14 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/City> .
_:b15 <http://schema.org/name> "Bob" .
_:b15 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> .
_:b16 <http://schema.org/name> "Bangkok" .
_:b16 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/City> .
_:b17 <http://schema.org/name> "Carl" .
_:b17 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> .
_:b2 <http://schema.org/name> "Venice" .
_:b2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/City> .
_:b3 <http://schema.org/name> "Bob" .
_:b3 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> .
_:b4 <http://schema.org/name> "Paris" .
_:b4 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/City> .
_:b5 <http://schema.org/name> "Alice" .
_:b5 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> .
_:b6 <http://schema.org/name> "New York" .
_:b6 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/City> .
_:b7 <http://schema.org/name> "Bob" .
_:b7 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> .
_:b8 <http://schema.org/name> "Amsterdam" .
_:b8 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/City> .
_:b9 <http://schema.org/name> "Alice" .
_:b9 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> .
```
