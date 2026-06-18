from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

# 1. Our four test documents
docs = [
    "physics is awesome", 
    "football is all about goal scoring", 
    "quantum mechanics is cool", 
    "soccer is a great sport"
]

# 2. Build the TF-IDF Matrix
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(docs)

# 3. Compress into Semantic 2D Space
svd = TruncatedSVD(n_components=2, random_state=42)
semantic_matrix = svd.fit_transform(tfidf_matrix)

# 4. THE NEW STEP: Process a tricky search query
query = ["striker and goal"]

# Notice we use .transform(), NOT .fit_transform()
# The axes are already calibrated, we just want to measure the query
query_tfidf = vectorizer.transform(query)
query_semantic = svd.transform(query_tfidf)

# 5. Measure the angle between the query and all documents
scores = cosine_similarity(query_semantic, semantic_matrix)[0]

print("Semantic Search Results for: 'striker and goal'\n")
for i, score in enumerate(scores):
    print(f"Document {i+1} ({docs[i]}): Match Score = {score:.4f}")