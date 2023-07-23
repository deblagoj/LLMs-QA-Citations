import os
from paperqa import Docs









docs = Docs()


import pickle

# save
with open("my_docs.pkl", "wb") as f:
    pickle.dump(docs, f)

answer = docs.query("What is ai?")
print(answer.formatted_answer)