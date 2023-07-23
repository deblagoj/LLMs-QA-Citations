import os
from paperqa import Docs





os.environ['OPENAI_API_KEY'] = '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'




docs = Docs()


import pickle

# save
with open("my_docs.pkl", "wb") as f:
    pickle.dump(docs, f)

answer = docs.query("What is ai?")
print(answer.formatted_answer)