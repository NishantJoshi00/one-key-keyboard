from serial import Serial
from create_trie import Node
import sys
import pickle

with open("trie.pkl", "rb") as f:
    start = pickle.load(f)


ser = Serial(sys.argv[1], int(sys.argv[2]))
sent = ' '*10

def get(data):
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
    if notd:
        return ''
    if triv.val == None:
        return ''
    else:
        return triv.val

try:
    count = 0
    maxi = 200
    char = 0
    # status = 0
    full = ''
    cur = ''
    red = 0
    while True:
        data = int(ser.read())
        if red < maxi:
            red += 1
        
        if data == char:
            count += 1
            if data == 0 and count > 100:
                sent += cur
                full = ''
            if data == 1 and count > 100:
                print(" "* 70, end='\r')
                if sent[-1] != ' ':
                    sent = sent[:-1]
                full = ''
                cur = ''
                char = 0

        else:
              
            if char == 1 and count < 20:
                full += '.'
            if char == 1 and count > 20:
                if count > 100:
                    sent = sent[:-1]
                    full = ''
                    char = 0
                    red = 0
                    cur = ''
                    continue
                else:
                    full += '-'
            count = 0
            char = data
        cur = get(full)
        print("{}{}".format(sent, cur), end='\r')
except:
    print()
    print("::Error::")
finally:
    ser.close()

