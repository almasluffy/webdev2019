def sleep_in(weekday, vacation):
    if(weekday == False or vacation == True):
        return True
    else:
        return False


print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))
print(sleep_in(True, True))
