def savefile(text, path):
    with open(path, "w") as f:
        f.write(text)

def filecont(path):
    with open(path, "r") as f:
        return f.read()

def getfilename(path):
    r = ""
    tmp = path
    for c in tmp[::-1]:
        if c == "/":
            break
        else:
            r += c
    return r[::-1]
