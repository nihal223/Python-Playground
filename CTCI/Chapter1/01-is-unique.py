# with additional data structure
def is_unique_ds(s):
    # ASCII charset is 128
    if len(string) > 128:
        return False

    letters = {}
    for char in s:
        if char in letters:
            return False
        letters[char] = True

    return True

# without additional data structure
def is_unique_no_ds(s):
    # ASCII charset is 128
    if len(string) > 128:
        return False

    sorted_s = sorted(s)
    for i, char in enumerate(sorted_s[:-1]):
        if sorted_s[i] == sorted_s[i+1]:
            return False

    return True


if __name__  == '__main__':
    string = "welgwengiwgnwipenbwieb"
    res1 = is_unique_ds(string)
    res2 = is_unique_no_ds(string)
    print(res1,res2)