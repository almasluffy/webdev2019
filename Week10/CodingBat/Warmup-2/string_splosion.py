def string_splosion(str):
    s = ""
    for i in range(len(str)):
        s += str[:i+1]
    return s
