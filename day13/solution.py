def is_anagram(s,t):
    ss = sorted(s)
    ts = sorted(t)

    return ss == ts


print(is_anagram("salt","salt"))