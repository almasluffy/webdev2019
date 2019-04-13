def near_ten(num):
    if (num==10 or num==1):
        return True
    elif (num<10):
        return False
    elif ((num+2)%10==0 or ((num-2)%10==0)):
        return True
    elif ((num+1)%10==0 or ((num-1)%10==0)):
        return True
    else:
        return False