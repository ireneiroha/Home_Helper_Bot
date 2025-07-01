def match_string(substring, mstring):
    p = []
    for s in substring:
        if s in mstring:
            p.append(s)
    return p
