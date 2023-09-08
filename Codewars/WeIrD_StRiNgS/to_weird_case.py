def to_weird_case(words):
    index = 0
    result = ""
    for letter in words:
        if letter == ' ':
            index = 0
            result += ' '
            continue
        if index % 2 == 0:
            result += letter.upper()
        else:
            result += letter.lower()
        index +=1
    return result