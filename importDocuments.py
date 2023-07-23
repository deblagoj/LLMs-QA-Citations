import os
os.environ['OPENAI_API_KEY'] = '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'


from paperqa import Docs






def list_files_in_folder(folder_path):
    file_paths = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

# Example usage:
folder_path = "/Users/blagojdelipetrev/Code/my_reports/"
file_paths_list = list_files_in_folder(folder_path)
print(file_paths_list)

# get a list of paths

docs = Docs(index_path=None)
#docs = Docs()
for d in file_paths_list:
    docs.add(d)


import pickle

# save
with open("my_docs.pkl", "wb") as f:
    pickle.dump(docs, f)
print("Docs object pickled.")

# load
with open("my_docs.pkl", "rb") as f:
    docs = pickle.load(f)
print("Docs object unpickled.")

answer = docs.query("What is ai?")
print(answer.formatted_answer)