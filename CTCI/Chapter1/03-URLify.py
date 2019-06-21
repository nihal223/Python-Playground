def URLify(s, n):
    print(s)
    trimmed_s = s[:n]
    for i, char in enumerate(trimmed_s):
        if char == ' ':
            trimmed_s[i]= '%20'
    return trimmed_s

if __name__ == '__main__':
    # Using lists because strings are immutable
    s1 = list('much ado about nothing      ')
    n = 22
    res = URLify(s1, n)
    print(res)