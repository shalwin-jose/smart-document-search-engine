import os
import string
import math
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

query=input("Enter search term:").lower()
query=query.translate(str.maketrans("","",string.punctuation))
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

if not sorted_scores:
    print("no matching results")
else:
    print("\nSearch results")
    for name, score in sorted_scores:
        print(f"{name} 'n {score} matches")

