import os
import string
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity


def get_search_results(user_query, search_type="exact"):
    folder_path="documents"
    if search_type == "semantic":
        docs = []
        filenames = []

        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith(".txt"):
                    file_path = os.path.join(folder_path, filename)
                    with open(file_path, "r", encoding="utf-8") as file:
                        docs.append(file.read().lower())
                        filenames.append(filename)

        if not docs:
            return []

        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(docs)
        
        n_comp = min(2, len(docs) - 1) if len(docs) > 1 else 1
        svd = TruncatedSVD(n_components=n_comp, random_state=42)
        semantic_matrix = svd.fit_transform(tfidf_matrix)
        
        query_tfidf = vectorizer.transform([user_query])
        query_semantic = svd.transform(query_tfidf)
        
        scores = cosine_similarity(query_semantic, semantic_matrix)[0]

        results = []
        for idx, score in enumerate(scores):
            if score > 0.01: 
                results.append((filenames[idx], round(score, 4)))
        return sorted(results, key=lambda x: x[1], reverse=True)

    if search_type=="semantic":

        return [("Semantic logic coming soon!", 0.0)]
    elif search_type=="exact":
        stop_words={"is","the","a","in","an","and","of","to","what","which","who","whom","this","that"}

        folder_path="documents"

        documents={}
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                file_path=os.path.join(folder_path,filename)
                with open(file_path, "r",encoding="utf-8") as file:
                    content=file.read().lower()
                    content=content.translate(str.maketrans("","",string.punctuation))
                    words=content.split()

                    word_freq={}
                    for w in words:
                        word_freq[w]=word_freq.get(w, 0) + 1

                    documents[filename]=word_freq

        doc_frequency={}
        for word_freq in documents.values():
            for word in word_freq:
                doc_frequency[word]= doc_frequency.get(word, 0)+1

        total_docs=len(documents)
        idf={}
        for word, df in doc_frequency.items():
            idf[word]=math.log(total_docs/df)

        query=user_query.lower().translate(str.maketrans("","",string.punctuation))
        query_words={
        word for word in query.split()
        if word not in stop_words
        }
        scores={}
        for name, word_freq in documents.items():
            total_score=0
            for word in query_words:
                total_score+=word_freq.get(word, 0) * idf.get(word, 0)
            if total_score > 0:
                scores[name]=total_score

        sorted_scores=sorted(scores.items(),key=lambda x: x[1],reverse=True)
        return sorted_scores
