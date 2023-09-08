def typist(s):
    upper = False
    key_strokes = len(s)
    for l in s:
        if l.isupper() and not upper:
            key_strokes += 1
            upper = True
        elif l.islower() and upper:
            key_strokes +=1
            upper = False
    return key_strokes