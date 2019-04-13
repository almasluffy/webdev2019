def caught_speeding(speed, is_birthday):
    bd = 0
    if(is_birthday):
        bd = 5
    if(speed <= 60 + bd):
        return (0)
    elif(speed > 60 + bd and speed <= 80 + bd):
        return 1
    else:
        return 2