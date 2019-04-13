def front_times(str, n):
    s=""
    length = 3
    if(len(str)<3):
        length = len(str)
    front = str[:length]
    
    for i in range(n):
        s+=front
    return s