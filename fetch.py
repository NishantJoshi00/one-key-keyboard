import pickle
from create_trie import Node

with open("trie.pkl", "rb") as f:
    start = pickle.load(f)

data = input()
triv = start
notd = False
for i in data.strip():
    if i == '.' and triv.dotin():
        triv = triv.dot
    elif i == '-' and triv.dashin():
        triv = triv.dash
    else:
        notd = True
        break 
if not notd:
    print("Output: {}".format(triv.val))