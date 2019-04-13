def make_chocolate(small, big, goal):
    max = goal/5
    if(max <= big):
        goal -= max*5
    else:
        goal -= big*5
    if(goal <= small):
        return goal
    return -1