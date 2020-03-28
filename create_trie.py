class Node:
    def __init__(self, current_val, val=None):
        self.sign = current_val
        self.val = val
        self.dash = None
        self.dot = None
    def add(self, node):
        if node.sign == '-' and self.dash == None:
            self.dash = node
            return 0
        if node.sign == '.' and self.dot == None:
            self.dot = node
            return 0
        else:
            return 1
    def dotin(self):
        if self.dot == None:
            return False
        return True
    def dashin(self):
        if self.dash == None:
            return False
        return True



start = Node("/")
# input .--. A
def add(dat):
    code, data = dat.strip().split(" ")
    # print(code, data)
    triv = start
    for i in code:
        if i == '.':
            if triv.dotin():
                triv = triv.dot
            else:
                triv.add(Node('.'))
                triv = triv.dot
        else:
            if triv.dashin():
                triv = triv.dash
            else:
                triv.add(Node('-'))
                triv = triv.dash
    triv.val = data
    print("registered..")
if __name__ == "__main__":
    print("Start entering the data from here")
    dat = input("-> ")
    while dat != 'quit':
        add(dat)
        dat = input("-> ")

    import pickle
    with open("trie.pkl", "wb") as f:
        pickle.dump(start, f)
