def cigar_party(cigars, is_weekend):
    if(cigars >= 40 and (cigars <= 60 or is_weekend)):
        return True
    else:
        return False
