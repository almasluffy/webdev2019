def squirrel_play(temp, is_summer):
    limit = 90
    if(is_summer):
        limit = 100
    if(temp >= 60 and temp <= limit):
  	    return True
    else:
        return False