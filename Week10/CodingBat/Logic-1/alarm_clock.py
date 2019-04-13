def alarm_clock(day, vacation):
    if(day == 0 or day == 6):
        if(not vacation):
            return ("10:00")
        else:
            return("off")
    else:
        if(vacation):
            return ("10:00")
        else:
            return ("7:00")