def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return (b.endswith(a) or a.endswith(b))