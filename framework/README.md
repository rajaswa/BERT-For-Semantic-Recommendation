## Framework

1. Query : Input content-sentiment factors *alpha* & *beta*s
2. Query : Input Text
3. Query : Text Preprocessing
4. Query : Extract Noun Phrase for Content and Adjectives & Adverbs for Sentiment
5. Query : Map Noun Phrases, Adjectives & Adverbs into embedding space
6. Query : Find cosine similarities with respective entities of each entry in database
7. Query : Calculate score for each entry in database using cosine similarities and input factors.
8. Score = *alpha* * cosine<sub>NP</sub> + (1 - *alpha*) * [ *beta*<sub>1</sub> * *abs*(cosine<sub>ADJ</sub>) + *beta*<sub>2</sub> * *abs*(cosine<sub>ADV</sub>) ]
9. Select top-n (n=100) entries
10. Cluster the entries with their contextual embeddings with k-means clustering (k=10)
11. Find cosine similarity between cluster heads and the input query, and rank clusters accordingly
12. Select the top ranked clusters (n=1)
13. For ranking the entries within the top cluster, rank the cluster head as one, rank other entries in cluster according to the cosine similarity with the cluster head
14. Output the ranked entries as final recommendations

### Code Instructions

1. Download the CMU Book summary dataset
2. Run *book_summary.ipynb*
3. Run *phrase_extraction.ipynb*
4. 