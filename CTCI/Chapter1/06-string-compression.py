def string_compress(s):
    # ASCII charset
    letters  = [0 for _ in range(128)]
    s_compressed = ''

    for i in range(len(s)):
        if i != 0 and s[i] == s[i-1]:
            letters[ord(s[i])] += 1
            if i ==len(s) - 1:
                s_compressed += s[i - 1]
                s_compressed += str(letters[ord(s[i - 1])] + 1)
        else:
            if i != 0:
                s_compressed += s[i-1]
                s_compressed += str(letters[ord(s[i-1])] + 1)
                letters = [0 for _ in range(128)]

    if len(s_compressed) > len(s):
        return s

    return s_compressed


if __name__ == '__main__':
    s = 'abcdef'
    res = string_compress(s)
    print(res)