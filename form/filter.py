def check_sqli(str):
    substrings = ['sle', 'hex', ' ']
    str = str.lower()
    for substring in substrings:
        if substring in str:
            return True
    return False
